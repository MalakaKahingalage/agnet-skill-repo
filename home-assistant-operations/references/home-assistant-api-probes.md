# Home Assistant API Probe Checklist

## Discovery & Network
- Probe local subnet for TCP `8123` when the HA host IP/hostname is unknown.
- Preserve both reverse DNS hostname (e.g. `ha.home`) and IP address in reports.

## Reachability & Auth Verification
- `GET /` $\rightarrow$ `200 OK` (frontend reachable)
- `GET /api/` without token $\rightarrow$ `401 Unauthorized` (confirms HA API service is active)
- `GET /api/` with bearer token $\rightarrow$ `200 OK` (authenticated API confirmed)

## Standard Probe Endpoints
1. `GET /api/` — API liveness check
2. `GET /api/config` — HA version, timezone, location metadata
3. `GET /api/states` — Full entity inventory & state scan
4. `POST /api/services/<domain>/<service>` — Service execution
