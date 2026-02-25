# Codex Handoff: Repomix x NotebookLM Capabilities (2026-02-16)

## 목적
Antigravity가 `Repomix + NotebookLM` 조합을 사용할 때, "무엇을 할 수 있는지"를 빠르게 재사용 가능한 형태로 전달.

## 1) Repomix로 할 수 있는 것
- 대규모 레포를 AI 입력 친화 단일 문서로 패키징 (`xml|markdown|json|plain`).
- `--include`, `--ignore`로 기능 단위 컨텍스트 분리.
- `--compress`, `--remove-comments`, `--remove-empty-lines`로 토큰 절감.
- `.gitignore` 기반 노이즈 파일 자동 제외.
- 결과적으로 LLM에 전달할 컨텍스트를 "작고 정확하게" 만들 수 있음.

## 2) NotebookLM(nlm CLI)로 할 수 있는 것
- 업로드한 소스만 근거로 질의응답(근거 기반 맥락 유지).
- 노트북별 지식 분리(예: 디버깅/보안/아키텍처 전용 노트북).
- 소스 검색/요약/재질의로 리서치 비용과 토큰 사용량 절감.
- 마인드맵 생성으로 구조 이해 가속 (`nlm mindmap create`).

## 3) 함께 쓸 때의 실전 효용
- 신규 코드베이스 온보딩 시간 단축.
- 대규모 프로젝트 토큰 비용 절감.
- "파일 시스템 전수 탐색" 대신 "근거 저장소 질의" 중심 워크플로우 가능.
- 구현 에이전트가 필요한 정보만 정확히 끌어와 할루시네이션/맥락 드리프트 감소.

## 4) 최소 실행 플로우 (CLI)
```powershell
# auth
nlm login

# repomix 패키징
npx -y repomix . --style markdown --compress --remove-comments --remove-empty-lines --output .\artifacts\repomix-pack.md

# notebook 생성
nlm notebook create "project-context"
nlm notebook list -t

# 소스 업로드
nlm source add <NOTEBOOK_ID> --file .\artifacts\repomix-pack.md --title "repomix pack" --wait

# 질의/시각화
nlm query notebook <NOTEBOOK_ID> "이 코드베이스의 핵심 흐름을 요약해줘"
nlm mindmap create <NOTEBOOK_ID> --title "architecture" -y
```

## 5) 운영 규칙 제안
- 전체 레포 1개 + 기능별 분할 팩(N개) 동시 운영.
- prompt에는 원문 전체 대신 NotebookLM 질의 결과를 넣기.
- 민감정보/비밀키는 패키징 전 필수 필터링.
- 상태 확인 순서: `nlm login --check` -> `nlm notebook list -t` -> `nlm source list <id>`.

## 전달 메모
현재 환경에서 `nlm` CLI는 설치되어 있으나 인증 만료 상태를 확인함.
재사용 시 첫 단계는 `nlm login` 재인증.
