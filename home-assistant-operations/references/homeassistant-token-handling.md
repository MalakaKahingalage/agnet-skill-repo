# Home Assistant Token Handling (LLAT)

## Storage Convention
Store Home Assistant Long-Lived Access Tokens (LLAT) in gopass at:
`infra/homeassistant-api-token`

## Exposure Safeguards
If a token is pasted in cleartext during a session:
1. Use it strictly for the required setup/audit operation.
2. Recommend rotating/revoking the token in Home Assistant.
3. Re-store the replacement token in gopass.

## Safe Insert Command
```bash
printf '%s' "$TOKEN" | gopass insert -f -m infra/homeassistant-api-token
```
