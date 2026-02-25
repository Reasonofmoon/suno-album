# Agentation + MCP Quickstart (MoonWorkspace)

이 문서는 `MoonWorkspace` 기준으로 Agentation을 실제 프로젝트에 붙이고, 빌드까지 검증하는 최소 절차입니다.

## 1) 적용 대상 앱 준비

- 전제: React 18+ 앱
- 앱 루트(예: `C:\path\to\your-react-app`)에서 진행

## 2) Agentation 설치 및 UI 삽입

```powershell
npm install -D agentation
```

앱 엔트리(예: `src/App.tsx`)에 삽입:

```tsx
import { Agentation } from "agentation";

export default function App() {
  return (
    <>
      <YourApp />
      <Agentation />
    </>
  );
}
```

옵션: copy 대신 서버로 전송하려면

```tsx
<Agentation endpoint="http://localhost:4747" />
```

## 3) MCP 서버 연결

```powershell
npm install -g agentation-mcp
claude mcp add agentation -- npx agentation-mcp server
agentation-mcp doctor
```

서버 실행:

```powershell
agentation-mcp server
```

기본 동작:
- HTTP: `http://localhost:4747`
- MCP tools: 세션/annotation 조회, acknowledge, resolve, reply, watch

## 4) Webhook 연결 (선택)

```powershell
$env:AGENTATION_WEBHOOK_URL="https://your-server.example.com/agentation-webhook"
agentation-mcp server
```

여러 webhook:

```powershell
$env:AGENTATION_WEBHOOKS="https://a.example.com/hook,https://b.example.com/hook"
agentation-mcp server
```

## 5) 빌드 검증

앱 루트에서:

```powershell
npm run build
```

검증 체크:
- build 성공
- 브라우저에서 우하단 Agentation 툴바 표시
- annotation 생성 후 copy 또는 endpoint 전송 확인
- MCP 서버에서 session/annotation 확인

## 6) Codex/Claude 작업 루프 예시

1. 페이지에서 요소 클릭 후 annotation 작성
2. MCP 사용 시: 에이전트에게 `address my feedback` 또는 `fix annotation 3`
3. 에이전트가 수정 후 `resolve` 처리
4. 필요 시 `watch` 루프로 신규 annotation 자동 처리

## 7) 주의사항

- 라이선스: `PolyForm-Shield-1.0.0` (사내 정책 확인 필요)
- 저장소: 기본 SQLite (`~/.agentation/store.db`)
- 모바일은 공식 지원 대상이 아님(문서 기준)

