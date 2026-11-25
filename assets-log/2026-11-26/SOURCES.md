# 2026-11-26 투어디에 쓴 그림 자료와 출처

이 폴더는 2026년 11월 26일(KST) 투어디 작업에서 앱에 넣은 그림 자료의 **원본과 출처, 만든 방법**을 남긴 기록입니다. 나중에 저작권·출처 문의가 왔을 때 대조하려고 원본 파일과 SHA-256 해시를 함께 둡니다.

- 기록한 날짜: 2026-11-26 (KST)
- 앱 반영 위치: 투어디 아티팩트 `img/` 폴더 (아래 `derived/`와 같은 파일)

## 1. 직접 만든 지도 시안 (사용자 제작)

| 원본 파일 | 설명 | 앱에서 쓴 파일 | SHA-256 (원본) |
|---|---|---|---|
| `originals/design-jp-base.png` (896x1200) | 일본 지도 시안 3번 — 파란 윤곽선 | `derived/rg-jp-base.webp` (WebP 변환만) | `23108c4b6bf98311235746df46cf41185ac2f7dbb5df8180e7d0313ce8cccd38` |
| `originals/design-jp-night.png` (896x1200) | 일본 지도 시안 1번 — 야경 | `derived/rg-jp-night.webp` (WebP 변환만) | `7b1506dac6ea60cf1fac37c14984fb50c5fe98ca0337ff9c7acba01733e9efee` |
| `originals/design-jp-relief-unused.png` (896x1200) | 일본 지도 시안 2번 — 종이 입체 지형 (앱에 쓰지 않음) | — | `90357eed0f4956ca6737c1aa9ff95a07adf75d870f100ab64052c713ae1bd77c` |

- 위 시안은 사용자가 준비해 대화에 올린 이미지입니다.
- `derived/mt-base*.webp`, `mt-night*.webp`(설정 화면 예시 사진)는 위 시안을 잘라 줄인 것이고, `mt-old*.webp`는 시안 3번을 흑백으로 바꿔 양피지 색으로 물들인 임시 그림입니다.

## 2. NASA 위성 사진 (Blue Marble: Next Generation, 2004년 7월)

- 자료: NASA Earth Observatory — *Blue Marble: Next Generation w/ Topography and Bathymetry*, July 2004
- 받은 곳: https://science.nasa.gov/earth/earth-observatory/blue-marble-next-generation/base-topography-bathymetry/
- 이용 조건: NASA Earth Observatory Image Use Policy — 저작권 표시가 없는 자료는 상업적 용도를 포함해 자유롭게 재게시·재사용 가능, 필수 표기는 "NASA" (https://earthobservatory.nasa.gov/ImageUse). NASA Images and Media Usage Guidelines (https://www.nasa.gov/multimedia/guidelines/index.html)도 함께 따름. NASA 로고·휘장은 쓰지 않았고, NASA의 보증으로 보이게 쓰지 않음.
- 앱 표기: 위성 지도 오른쪽 위에 "NASA Blue Marble"

| 받은 원본 | 크기 | SHA-256 | 보관 |
|---|---|---|---|
| `world.topo.bathy.200407.3x21600x21600.A1.jpg` | 54,085,715 B | `cda310b5a180c7a7da95a605bc3a3a3fa082ecf870e0d9ea48994813216bcb70` | 용량이 커서 저장소에 넣지 않음 (위 주소에서 같은 파일을 다시 받을 수 있음) |
| `world.topo.bathy.200407.3x21600x21600.B1.jpg` | 54,665,612 B | `15d8ceb55676e6b3e7fdcd72217d1edd665b5e7f7396c606e7b98c427b28558e` | 〃 |
| `world.topo.bathy.200407.3x21600x21600.D1.jpg` | 68,470,337 B | `47480a4e98289d830adc689c32356771a83cd55a003cdbf32db7ade2a6609b56` | 〃 |
| `world.topo.bathy.200407.3x21600x10800.jpg` (대화 업로드 과정에서 8000x4000으로 줄어든 사본) | 3,435,770 B | `b32c71111b978f2d21eddaeb4681ab373503e807a4cf0b7a301093a4f143ca4f` | `originals/nasa-bluemarble-200407-global-8000x4000.jpg` |

만든 파일 (모두 위 원본을 각 지도 투영에 맞춰 다시 그리고, 밝기를 85~90%로 낮춰 WebP로 저장. 오키나와·알래스카·하와이 상자는 같은 원본에서 따로 잘라 붙임):

| 파일 | 원본 | 투영 |
|---|---|---|
| `derived/rg-jp-sat.webp` | D1 | 메르카토르 (일본 기본 지도와 같은 틀) |
| `derived/rg-kr-sat.webp` | D1 | 메르카토르 (한국) |
| `derived/rg-us-sat.webp` | A1·B1 | 메르카토르 (미국 본토 + 알래스카·하와이 상자) |
| `derived/kr-sat.webp` | D1 | 국내 지도 좌표(kxy) |
| `derived/world-sat.webp` | Global | Equal Earth, 동경 150° 중심 (세계 평면 지도) |
| `derived/globe-sat-4096.webp` | Global | 정방형 4096x2048 (지구본 표면) |

## 3. 그 밖의 데이터

- 지구본의 나라 윤곽: 앱에 이미 있던 세계 지도 데이터(js/travel-map.js의 WMAP, 공개 데이터)를 위경도로 되돌려 쓴 것. 새 외부 자료 없음.
- 수속 효과음(js/checkin-sound.js): 외부 음원 없이 코드로 합성한 소리.

## 4. 파일 해시 (derived/)

```
0d375511bc0c853f4d7441ca3d0e14d0f415739d5ee754e4851cdc6e34bfecd9  globe-sat-4096.webp
7770ff1af607861636626036cef5954ae1ea7bcd39dc20c18606a2b07d58fdbf  kr-sat.webp
2c3155db711b132c5ddd889043b2ca3719be0804a6f584ced5248b416199edbe  mt-base-l.webp
3f5f3ee33caa8901ce96e8cf16884e5b118be7ebf35660d644e933d3fffff08a  mt-base.webp
7ca1931637174b2ba4cc80c67973430a6769c1d278dcd619aae134336764408a  mt-night-l.webp
040b1415a2812d49be6f69c8a65314124b1cdef8c2f75f70dc13b5ef558c5a32  mt-night.webp
21e93c7556257d926775a60e8e882c1e649c698065a49a430e96d3f70c7718b5  mt-old-l.webp
df65ebddd6964154841521d1a5903b6e96f2d71e5fdc32efd7a5602707cdb23c  mt-old.webp
5c325315dd0d373712ec3f52f54478c14efa3bb96aa2adab37221d646743332d  mt-sat-l.webp
e81255709557bd2b23b490d818fc2220a05d23117eae1a4ed2756bf811f12193  mt-sat.webp
f4ead3dbb0a379e95165af29561f2a2f778defaec57c2b7db0c4970829a3bd73  rg-jp-base.webp
1fe42d75edf5e373fa070e63b4f79706bf1dbee88929181cc5e48d8fef86fe02  rg-jp-night.webp
ca0c215bb5e59e3aa0a688e6466160d06b06beaefda4cd745ff305027efcf1c5  rg-jp-sat.webp
aee7517b6595d7837ca7ce38541a48d298be526dda2349dac206e1528c64faf4  rg-kr-sat.webp
96607ce22e0dfb7c05a50549506c25495638101016c06ca3eb336a44531593b5  rg-us-sat.webp
672c6677dc1cffec39affecea148c5beec63f7e294322925d8623412ae3cfb19  world-sat.webp
```
