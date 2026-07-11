# 감기 림월드 모드 소개 페이지

GitHub Pages에 올리면, **하루 1회 스팀 워크샵 통계(구독자·방문자·즐겨찾기)가 자동 갱신**되는 정적 사이트입니다. 링크만 보내면 누구 화면에서든 이미지·숫자가 그대로 뜹니다.
https://gamgis.github.io/RimworldMods/

## 구성

| 파일 | 역할 |
|------|------|
| `index.html` | 페이지 본체. `mods.json` + `stats.json`을 읽어 렌더링 |
| `mods.json` | 6개 모드의 고정 정보(제목·설명·태그·이미지 경로) |
| `stats.json` | 구독자/방문자/즐겨찾기 수. **자동 갱신됨 (직접 안 건드려도 됨)** |
| `update_stats.py` | 스팀 API를 긁어 `stats.json`을 새로 씀 |
| `.github/workflows/update.yml` | 매일 자동 실행 + Pages 배포 |
| `images/` | 각 모드 썸네일 (`mechbaby.jpg`, `cozy.jpg`, `gravship.jpg`, `mechlovers.jpg`, `spa.jpg`, `mechmilk.jpg`) |

**매일 알아서** 최신 숫자로 갱신됩니다. 손댈 것 없음.

## 모드 추가/수정

- 문구·태그를 고치려면 `mods.json`만 편집.
- 모드를 추가하려면 `mods.json`의 `mods` 배열에 항목을 하나 더 넣고, 같은 ID로 `images/`에 썸네일을 추가. 통계는 다음 자동 실행 때 알아서 붙습니다.
