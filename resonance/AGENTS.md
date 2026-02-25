# AGENTS.md — RESONANCE Local Rules

## Scope

These rules apply within:

- `projects/suno-album/resonance/`

## Boot Sequence (Codex)

At the start of each session/task in this folder:

1. Run:
   - `powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\dual_boot_sync.ps1`
2. Check generated inboxes:
   - `shared/codex_inbox.md`
   - `shared/antigravity_inbox.md`
3. If pending messages exist, process REQUEST/HANDOFF items before unrelated work.

## Trigger Mapping

If user says `RESONANCE_SYNC.md 읽어줘`, Codex should:

1. Run `tools/dual_boot_sync.ps1`.
2. Summarize newly detected SEQ messages for `CODEX` and `ANTIGRAVITY`.
3. Start required tasks from pending REQUEST/HANDOFF entries.

## Always-On Option

To keep both agents auto-detected in real time:

- `powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\tools\watch_sync.ps1`

This watcher:

- monitors `RESONANCE_SYNC.md` and `memoglobe/PROMETHEUS_SYNC.md`
- triggers `dual_boot_sync.ps1` automatically on updates
- updates both inbox files continuously

## Ownership and Safety

- Respect ownership map in `AGENT_PROTOCOL.md`.
- `RESONANCE_SYNC.md` is append-only.
- Shared files under `shared/*` require lock policy from `AGENT_PROTOCOL.md`.
