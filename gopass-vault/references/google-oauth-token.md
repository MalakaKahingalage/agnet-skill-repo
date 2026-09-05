# Google OAuth Token Hydration & Management

When Google Workspace access is needed (Drive, Sheets, Gmail API), the OAuth token is stored in gopass at `infra/google-oauth-token` and hydrated to disk at `~/.hermes/google_token.json`.

## Re-authentication Flow (Fixing `invalid_grant`)

1. Revoke existing local state:
   ```bash
   python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --revoke || true
   ```

2. Request auth URL:
   ```bash
   python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-url
   ```

3. Exchange code for fresh token:
   ```bash
   python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --auth-code "<URL_OR_CODE>"
   ```

4. Store new token in gopass:
   ```bash
   ~/.local/bin/gopass insert -f infra/google-oauth-token < ~/.hermes/google_token.json
   ~/.local/bin/gopass sync
   ```
