# Codex x Antigravity Shared Setup

## Shared Root
- `C:\Users\82109\.gemini\antigravity`

## Shared Folders
- `skills`: Codex custom skills storage
- `plugins`: shared plugin assets storage
- `workflows`: shared workflow documents/storage

## Active Links
- `C:\Users\82109\.codex\skills\antigravity` -> `...\antigravity\skills`
- `C:\Users\82109\.codex\plugins` -> `...\antigravity\plugins`
- `C:\Users\82109\.codex\workflows` -> `...\antigravity\workflows`

## MCP Sync Source of Truth
- Edit: `C:\Users\82109\.gemini\antigravity\mcp_config.json`
- Synced target: `C:\Users\82109\.codex\config.toml` (`[mcp_servers.*]` sections)

## Auto Sync
- Scheduled task: `Antigravity-Codex-Sync`
- Interval: every 15 minutes (user session scope)
- Trigger command:
  - `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\82109\.gemini\antigravity\sync_codex_global.ps1 -Quiet`

## Manual Sync
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\82109\.gemini\antigravity\sync_codex_global.ps1
```

## Skill Folder Format
```text
skills/
  my-skill/
    SKILL.md
    scripts/...
    assets/...
```
- Use `my-skill` as the skill name in chat.

## Beginner Guide
- `C:\Users\82109\.gemini\antigravity\ANTIGRAVITY_BEGINNER_GLOBAL_SHARE_GUIDE.md`
