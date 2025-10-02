### 3) `.github/PULL_REQUEST_TEMPLATE.md`
```markdown
## Summary
<!-- What change is this PR introducing? One or two sentences. -->

## Scope / Pages
- [ ] Home (`/`)
- [ ] About (`/about`)
- [ ] Projects (`/projects`)
- [ ] Skills (`/skills`)
- [ ] Contact (`/contact`)
- [ ] Infra / CI / Ops

## How to Test
1. Run `pytest -q`
2. Start app and verify routes:
   - `curl -f http://localhost:8080/healthz`
   - Open `http://localhost:8080/`
3. (If container) `docker build .` then `docker run -p 8080:8080 ...`

## Risk & Rollback
- **Risk:** <!-- low/medium/high and why -->
- **Rollback:** Re-deploy previous image tag via Helm: