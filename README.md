# 로봇 밸류체인: 자동차 부품사의 진입 기회 — learn-robot-vc-ljy

자동차 부품사 재직자가 로봇 밸류체인 지도, 원가와 병목, 진입 경로를 배우고 자사의 진입 지점을 판단하는 약 1시간 강의다. 수업은 Claude Code 스킬 `/learn-robot-vc-ljy`가 진행한다 (Skills as Curriculum). 이 강의는 ljy가 course-forge로 직접 만들었다.

- **결과 대시보드**: https://jonglee46-bot.github.io/learn-robot-vc-ljy/
- **교재 PDF**: [docs/Robot_Value_Chain_Textbook.pdf](docs/Robot_Value_Chain_Textbook.pdf)
- **강의 덱 PDF**: [docs/Robot_Value_Chain_Deck.pdf](docs/Robot_Value_Chain_Deck.pdf)
- 처음이면 [GUIDE.md](GUIDE.md)부터. 기본 환경은 Claude 데스크톱 앱(Code 탭). VS Code는 GUIDE 부록 B

## 설치 — 한 줄

Claude Code 입력칸에 붙여 넣는다.

```
npx skills add jonglee46-bot/learn-robot-vc-ljy --agent claude-code --global --yes 를 실행해 줘
```

새 세션에서 `/learn-robot-vc-ljy`를 입력하면 수업이 시작된다.

## 블록

| Block | 주제 | 끝나면 생기는 것 |
|---|---|---|
| 0 | 준비 | 작업 폴더, 자료, env_check.txt (퀴즈 1문항) |
| 1 | 로봇 밸류체인 지도 | 휴머노이드 수량 표 (퀴즈 1문항) |
| 2 | 돈이 몰리는 곳과 병목 | BOM 차트 (퀴즈 1문항) |
| 3 | 부품사의 진입 기회와 공개 | 사내용 역량 점검표, 대시보드 주소 (퀴즈 1문항) |

## 수업 방식

| 구분 | 내용 |
|---|---|
| 목표 — AI Native | AI에게 맡기는 것이 기본인 방식으로 일한다 |
| 방법 — Skills as Curriculum | 스킬이 블록마다 설명 → 실습 → STOP → 확인·퀴즈를 진행한다 |
| 형식 — 자율학습 | 강사 없이 자기 속도로, 퀴즈로 스스로 점검한다 |

## 원본 강의와 데이터 출처

| 자료 | 출처 | 구분 |
|---|---|---|
| 교재·강의 덱 | 이 저장소의 `docs/` | ljy가 공개 자료로 작성 |
| 숫자 표 | `.claude/skills/learn-robot-vc-ljy/assets/lab/facts.csv` | 공개 자료에서 뽑은 값. 실적, 전망, 추정 표시 |
| 출처 표 | `.claude/skills/learn-robot-vc-ljy/assets/lab/sources.md` | 출처 34개의 기관, 발행일, 주소, 신뢰도 |

기업 사례는 학습용이며 투자 권유가 아니다.

## 개정 이력

| 날짜 | 바뀐 점 |
|---|---|
| 2026-10-31 | 첫 판 |

## 만든 방법

- `/course-forge`로 만들었다. 제작 기록(원본 요약·커리큘럼·검수 결과)은 `forge/`에 있다.
- 출처: 이 저장소의 교재와 `sources.md`
