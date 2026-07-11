# 감기 림월드 모드 소개 페이지

GitHub Pages에 올리면, **하루 1회 스팀 워크샵 통계(구독자·방문자·즐겨찾기)가 자동 갱신**되는 정적 사이트입니다. 링크만 보내면 누구 화면에서든 이미지·숫자가 그대로 뜹니다.

## 구성

| 파일 | 역할 |
|------|------|
| `index.html` | 페이지 본체. `mods.json` + `stats.json`을 읽어 렌더링 |
| `mods.json` | 6개 모드의 고정 정보(제목·설명·태그·이미지 경로) |
| `stats.json` | 구독자/방문자/즐겨찾기 수. **자동 갱신됨 (직접 안 건드려도 됨)** |
| `update_stats.py` | 스팀 API를 긁어 `stats.json`을 새로 씀 |
| `.github/workflows/update.yml` | 매일 자동 실행 + Pages 배포 |
| `images/` | 각 모드 썸네일 (`mechbaby.jpg`, `cozy.jpg`, `gravship.jpg`, `mechlovers.jpg`, `spa.jpg`, `mechmilk.jpg`) |

## 올리는 법 (한 번만)

1. GitHub에서 새 저장소(repository) 생성 — 예: `rimworld-mods`
2. 이 폴더의 파일 전부를 그 저장소에 올림 (드래그 업로드 또는 git push)
3. 저장소 **Settings → Pages** →
   - Source를 **GitHub Actions**로 설정
4. **Settings → Actions → General** 맨 아래 *Workflow permissions* →
   - **Read and write permissions** 체크 → Save
5. **Actions** 탭 → `Update workshop stats & deploy` → **Run workflow** 로 첫 실행
6. 몇 분 뒤 `https://<사용자명>.github.io/rimworld-mods/` 로 접속되면 완성.
   이 주소를 공유하면 됩니다.

이후에는 **매일 알아서** 최신 숫자로 갱신됩니다. 손댈 것 없음.

## 이미지 넣기

`images/` 폴더에 아래 6개 파일명으로 넣으면 자동으로 잡힙니다:

- `mechbaby.jpg` — Mechanoid Baby
- `cozy.jpg` — Cozy Companions
- `gravship.jpg` — Gravship Garden
- `mechlovers.jpg` — Mechanoid Lovers
- `spa.jpg` — Special Production Adjuster
- `mechmilk.jpg` — Mechanoid Milk *(이미 포함됨)*

이미지가 없는 항목은 모드 이름이 박힌 대체 그래픽이 자동으로 표시되므로, 나중에 하나씩 채워도 됩니다.

## 모드 추가/수정

- 문구·태그를 고치려면 `mods.json`만 편집.
- 모드를 추가하려면 `mods.json`의 `mods` 배열에 항목을 하나 더 넣고, 같은 ID로 `images/`에 썸네일을 추가. 통계는 다음 자동 실행 때 알아서 붙습니다.
