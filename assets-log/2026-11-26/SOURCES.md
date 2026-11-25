# 2026-11-26 투어디에 쓴 그림 자료와 출처

이 폴더는 2026년 11월 26일(KST) 투어디 작업에서 앱에 넣은 그림 자료의 **원본과 출처, 만든 방법**을 남긴 기록입니다. 나중에 저작권·출처 문의가 왔을 때 대조하려고 원본 파일과 SHA-256 해시를 함께 둡니다.

- 기록한 날짜: 2026-11-26 (KST)
- 앱 반영 위치: 투어디 아티팩트 `img/` 폴더 (아래 `derived/`와 같은 파일)

## 1. 직접 만든 지도 시안 (사용자 제작)

| 원본 파일 | 설명 | 앱에서 쓴 파일 | SHA-256 (원본) |
|---|---|---|---|
| `originals/design-jp-base.png` (896x1200) | 일본 지도 시안 3번 — 파란 윤곽선 | `derived/rg-jp-base.webp` (WebP 변환만) | `23108c4b6bf98311235746df46cf41185ac2f7dbb5df8180e7d0313ce8cccd38` |
| `originals/design-jp-night.png` (896x1200) | 일본 지도 시안 1번 — 야경 (03:13까지 야경 테마로 사용, 이후 NASA Black Marble로 교체) | `derived/rg-jp-night-design.webp` (WebP 변환만) | `7b1506dac6ea60cf1fac37c14984fb50c5fe98ca0337ff9c7acba01733e9efee` |
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

## 3. NASA 야경 사진 (Black Marble 2016 Color) — 03:13 추가

- 자료: NASA Earth Observatory — *Earth at Night (Black Marble) 2016 Color Maps*, Suomi NPP VIIRS (NASA Earth Observatory images by Joshua Stevens, using Suomi NPP VIIRS data from Miguel Román, NASA GSFC)
- 받은 곳: https://earthobservatory.nasa.gov/features/NightLights/page3.php
- 이용 조건: 위 2번과 같음 (NASA Earth Observatory Image Use Policy, 필수 표기 "NASA")
- 앱 표기: 야경 지도 오른쪽 위에 "NASA Black Marble"
- 일본 야경 테마는 이 사진으로 교체함 (이전: 사용자 시안 1번)

| 받은 원본 | 크기 | SHA-256 | 보관·사용 |
|---|---|---|---|
| BlackMarble_2016_D1.jpg (21600x21600) | 39,122,860 B | `449fdd6b2f6eec087f56b5a0dcee5ab3213ea0ade75ec746f38cea76f3acd442` | 용량이 커서 저장소에 넣지 않음 · 일본·한국·국내 야경에 사용 |
| BlackMarble_2016_C1.jpg (21600x21600) | 59,097,456 B | `446fcc72755ebc3625f96d39f2bcb247016038b74c90c655a65991e6de71b3b5` | 저장소에 넣지 않음 · 아직 쓰지 않음 (유럽 지역 여행용) |
| BlackMarble_2016_A1.jpg (업로드 중 8000x8000으로 줄어든 사본) | 2,590,891 B | `dac7c198fbf2c48f027c6aaf69ee3cf5156b993c3226856c81759fa9abe3720e` | `originals/nasa-blackmarble-2016-A1-8000x8000.jpg` · 미국 야경 |
| BlackMarble_2016_B1.jpg (〃) | 2,512,901 B | `fdab28a9ccbab45e170fa91dbeba53b56562a9e729af1b096a30a57e61b68c4c` | `originals/nasa-blackmarble-2016-B1-8000x8000.jpg` · 미국 야경 |
| BlackMarble_2016_3km.jpg (업로드 중 8000x4000으로 줄어든 사본) | 1,676,318 B | `bad11f716f4dc099114836c27650ce0e88b4a2cb2837a062d4a3c9217a0be74b` | `originals/nasa-blackmarble-2016-global-8000x4000.jpg` · 세계 지도·지구본 |
| BlackMarble_2016_A2.jpg (〃 8000x8000) | 539,061 B | `033058a3e7278030260796b6e688da0f0994a72039910c53a9c1d8aeaa71cf5c` | 받기만 하고 쓰지 않음 |
| BlackMarble_2016_B2.jpg (〃) | 1,751,557 B | `4b88072aaf7f769197123338588d6792413d5b178da6213bb4a5414fd751a532` | 〃 |
| BlackMarble_2016_C2.jpg (〃) | 995,488 B | `e48f1795ed18829490768d528321c04da033b5efa699988495bf17101fe12109` | 〃 |
| BlackMarble_2016_D2.jpg (〃) | 1,093,399 B | `6af9304c14a5861f7ca3232dfd72fb9842ae7cb3b4637d3a1837b740af9d66a8` | 〃 |

만든 파일 (위성 사진과 같은 틀·투영으로 다시 그리고 밝기를 약간 올림: 값×1.12+4):

```
1ce495b34848dbce1d9329a046c0f3adc0bf18b519387ee67c4e97a78051bd96  rg-jp-night.webp
31847e9fc049d41cf27a6a0baf584c38f884705a27da9e282dc04187499b468b  rg-kr-night.webp
e2eae219c9e46eff3debc79f82b231691fdbe8f71d77ef4289a4c747b246c491  rg-us-night.webp
35976e1fb82880bf4e2d71bdcc2c9eacc9aff816b84e40a43006104a923f69f1  kr-night.webp
5973ec71879ff118eae6b9b08924708fef31bef6e499d50e1bb0e9832223b26f  world-night.webp
b893ff130b019c885c55c88aa19057425972ec74b3a39f67b6ab6d06cee71f39  globe-night-4096.webp
6a5fed617046c2c6b3910c316ddf37b35db3d38c675d35fe5cd9d65da9afcd52  mt-night.webp
3ad4ce91dc2e5c5549d8f6beb940ee0e4114de774eef55fcf1c258cc48f04c3e  mt-night-l.webp
```

## 4. 그 밖의 데이터

- 지구본의 나라 윤곽: 앱에 이미 있던 세계 지도 데이터(js/travel-map.js의 WMAP, 공개 데이터)를 위경도로 되돌려 쓴 것. 새 외부 자료 없음.
- 수속 효과음(js/checkin-sound.js): 외부 음원 없이 코드로 합성한 소리.

## 5. 파일 해시 (derived/, 처음 기록 시점)

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

## 야경 밝기 낮춤 (2026-11-26 03:2x KST)
같은 NASA Black Marble 원본에서 만든 야경 지도의 밝은 부분을 눌러 줌 (밝은 곳 압축 `1.1L/(1+0.85L)`, 채도 90%, 감마 1.12).
| 파일 | SHA-256 |
|---|---|
| derived/kr-night-dim.webp | 987dd743a6c2ee5e74bdc1dca4b5d379135202bab7dd0d8e92700bc51ed2186d |
| derived/rg-kr-night-dim.webp | 80e7f465b209074583fb79cf324fd11967327ea67ebb1a1496789add3d57a9e9 |
| derived/rg-jp-night-dim.webp | 9af2cd2783f809065aa4dc8540d0866db3d59aa195fb9f0e66e17e8a4c5b3cb0 |
| derived/rg-us-night-dim.webp | 1b506791402c7beeb1c52f08876e23365be34a6d164814619ad4565ce3a2cc2a |
| derived/world-night-dim.webp | 1ac856a13dbb46af323857c9e67aafd825323c2b19395d1504aff4875d7c917e |
| derived/globe-night-4096-dim.webp | 18c6d0ca6db4ddfc2ce37d536f8f33d3a76fe11fcdb526c60f93f727c9696004 |

## 기차 도착 효과음 (2026-11-26 03:3x KST)
- 원본: originals/train-passing-by.mp3 — 사용자가 직접 받아 온 파일 (저작권 없는 효과음). 출처 URL·라이선스: **확인 필요**
  - SHA-256: daf9fcecfcaa1968270244a9ddafff7966c6b950c453b64cb7ea8be55bf26ed8
- 가공본: derived/arr-train.mp3 — 0.72초부터 2.6초만 잘라냄, 저역통과 2.6kHz/4.2kHz + 고역 -3dB(먹먹하게), 앞 0.12초·뒤 1.0초 페이드, 음량 -18 LUFS
  - SHA-256: 325d51046522ceb07252ca3f5a8bc400c51300c83d5faa4617389a5b1798c1ee
  - 앱 경로: sounds/arr-train.mp3 (도착 화면 · 기차/KTX/무궁화호 등 모든 철도)

## 버스 도착 효과음 (2026-11-26 03:5x KST)
| 원본 | 출처 | 라이선스 | SHA-256 |
|---|---|---|---|
| originals/29610__dobroide__20070117puff.wav | https://freesound.org/people/dobroide/sounds/29610/ ("20070117.puff.wav" by dobroide) | CC BY 4.0 — 앱 안 저작자 표시 필요(설정 → 소리 아래에 표시함) | d2166c39df344e3f6169dafc2d33adc41650c32abed8fecb9c6b902cd64350f6 |
| originals/380320__zombiechick__bus-door.wav | https://freesound.org/people/zombiechick/sounds/380320/ ("bus door" by zombiechick) | CC0 | 4a27772fa1deeec1530002a757ff2ffb6e0ea348ceeef9ba754a9c0b265450b7 |
- 라이선스는 2026-11-26 freesound 페이지에서 확인
- 가공본 derived/arr-bus.mp3 (SHA-256 926e13a36c75781a22541c6be243fe14ef05719695b8b0394b9d58ab24b7bc9d)
  - puff: 미끄러지듯 올라가는 고주파 휘슬음(약 3.8–4kHz, 7.6–7.9kHz 등)을 프레임별 스펙트럼 억제로 제거, 0–1.15초만 사용
  - bus door: 1.30–2.70초(문 덜컥 부분)만 사용, 0.75초 뒤에 겹침
  - 합친 뒤 저역통과 3.2k/5k + 고역 -2dB(먹먹하게), -19 LUFS, 리미터. 길이 2.2초
