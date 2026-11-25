import json,math,shapefile
from shapely.geometry import shape,Polygon,MultiPolygon,Point,box,mapping
from shapely.ops import unary_union,transform
from shapely.affinity import affine_transform
C=json.load(open('cities.json'))
def pathd(g):
    out=[]
    polys=[g] if g.geom_type=='Polygon' else list(getattr(g,'geoms',[]))
    for p in polys:
        if p.is_empty or p.geom_type!='Polygon':continue
        for ring in [p.exterior,*p.interiors]:
            cs=list(ring.coords)
            if len(cs)<3:continue
            out.append('M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in cs[:-1])+'Z')
    return ''.join(out)
def lined(g):
    out=[]
    gs=[g] if g.geom_type in('LineString','LinearRing') else list(getattr(g,'geoms',[]))
    for l in gs:
        if l.geom_type in('Polygon',):l=l.exterior
        if l.geom_type=='MultiLineString':
            for k in l.geoms:out.append('M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in k.coords))
            continue
        cs=list(l.coords)
        if len(cs)>1:out.append('M'+'L'.join(f'{x:.1f} {y:.1f}' for x,y in cs))
    return ''.join(out)
def build(feats,cities,pts,vb,name,extra={}):
    # feats: list of (geom in px)
    # 도시가 든 구역 → 그 도시 그룹, 없으면 가장 가까운 도시 그룹
    P=[]
    for g in feats:
        ids=[c['id'] for c in cities if g.buffer(0.5).contains(Point(pts[c['id']]))]
        if ids:grp=max(set(cities_g:=[next(x['g'] for x in cities if x['id']==i) for i in ids]),key=cities_g.count)
        else:
            cen=g.representative_point();grp=min(cities,key=lambda c:Point(pts[c['id']]).distance(cen))['g']
        P.append([g,grp,ids])
    groups=sorted(set(p[1] for p in P))
    gb=[]
    for gi in groups:
        u=unary_union([p[0].buffer(0.3) for p in P if p[1]==gi]).buffer(-0.3)
        gb.append(u.boundary.simplify(0.4))
    out={'vb':vb,'P':[[pathd(p[0]),p[1],','.join(p[2])] for p in P],'gb':lined(unary_union(gb)),'pts':{k:[round(v[0],1),round(v[1],1)] for k,v in pts.items()}}
    out.update(extra);return out
# ---------- 일본 ----------
r=shapefile.Reader('node_modules/jpn-atlas/build/polbnda_jpn.shp',encoding='utf-8')
by={}
for sr in r.iterShapeRecords():
    code=sr.record['adm_code'][:2];g=shape(sr.shape.__geo_interface__)
    if not g.is_valid:g=g.buffer(0)
    by.setdefault(code,[]).append(g)
S=60;K=math.cos(math.radians(36))
LO0,LA1=128.4,45.65
main=lambda x,y:(x,y)
def pj(lon,lat):return ((lon-LO0)*K*S,(LA1-lat)*S)
JPC=C['JP']['c'];oki=[c for c in JPC if c['g']==8]
IR=[548,716,842,880]   # 오키나와 상자 (x0,y0,x1,y1)
OL=(122.8,131.4,24.0,27.95);KI=math.cos(math.radians(26));SI=min((IR[2]-IR[0]-16)/((OL[1]-OL[0])*KI),(IR[3]-IR[1]-26)/(OL[3]-OL[2]))
def pji(lon,lat):return (IR[0]+8+(lon-OL[0])*KI*SI,IR[1]+18+(OL[3]-lat)*SI)
feats=[];
mainbox=box(128.4,30.9,146.2,45.65)
for code,gs in sorted(by.items()):
    u=unary_union(gs)
    if code=='47':
        g=transform(lambda x,y,z=None:pji(x,y),u)
    else:
        u=u.intersection(mainbox)
        if u.is_empty:continue
        g=transform(lambda x,y,z=None:pj(x,y),u)
    g=g.simplify(0.75,preserve_topology=True)
    g=MultiPolygon([p for p in (g.geoms if g.geom_type=='MultiPolygon' else [g]) if p.area>1.2]) if g.geom_type in('MultiPolygon','Polygon') else g
    if not g.is_empty:feats.append(g)
pts={c['id']:(pji(c['lon'],c['lat']) if c['g']==8 else pj(c['lon'],c['lat'])) for c in JPC}
W=round((146.2-LO0)*K*S);H=round((LA1-30.9)*S)
JP=build(feats,JPC,pts,[0,0,W,H],'JP',{'ins':[[IR[0],IR[1],IR[2]-IR[0],IR[3]-IR[1],'오키나와']]})
# ---------- 미국 ----------
us=json.load(open('us-states.geojson'));pts=json.load(open('us-pts.json'))
feats=[]
for f in us['features']:
    g=shape(f['geometry'])
    if not g.is_valid:g=g.buffer(0)
    g=g.simplify(0.8,preserve_topology=True)
    feats.append(g)
USd=build(feats,C['US']['c'],pts,[0,0,975,610],'US',{'ins':[]})
s='/* 일본 도도부현·미국 주 경계 (기본·네온 테마 국내 지도) — 일본: 국토지리원 지구지도 일본 2016(jpn-atlas), 미국: U.S. Census Bureau(us-atlas) */\nwindow.RGSHAPE='+json.dumps({'JP':JP,'US':USd},ensure_ascii=False,separators=(',',':'))+';\n'
open('/home/claude/art/js/rg-shapes.js','w').write(s);print(len(s),len(JP['P']),len(USd['P']),W,H)
