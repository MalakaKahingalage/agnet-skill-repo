---
name: home-assistant-operations
description: Connect to Home Assistant, verify reachability, inspect entities, assess system health, and operate devices through the HA API. Use when managing Home Assistant instances, checking entity statuses, running automations, or operating home devices.
version: 1.0.0
tags: [home-assistant, smart-home, iot, automation, api]
---

# Home Assistant Operations

Use this skill when connecting to Home Assistant, verifying reachability, inspecting entities, assessing system health, or operating the house through the Home Assistant API.

## When to load

- User asks whether the agent can connect to Home Assistant
- User provides a Home Assistant URL, hostname, IP, or long-lived access token
- User wants an inventory of devices, entities, or automations
- User wants a health check, update audit, or unavailable-entity report
- User wants to control lights, covers, media players, scenes, scripts, or other HA services

## Core Workflow

1. **Find the Instance**
   - If the host is unknown but on the same LAN, probe TCP `8123`.
   - Prefer a hostname if reverse DNS reveals one (e.g. `ha.home`), keeping IP as fallback.

2. **Verify Unauthenticated Reachability First**
   - Check `http://<host>:8123/` for the frontend (`200 OK`).
   - Check `http://<host>:8123/api/` without auth (`401 Unauthorized` expected).
   - Proves the instance is reachable before spending time on auth troubleshooting.

3. **Use Long-Lived Access Token (LLAT) for Authenticated Probes**
   - Include token header: `Authorization: Bearer <token>`
   - `GET /api/` $\rightarrow$ confirms API is running
   - `GET /api/config` $\rightarrow$ returns HA version, timezone, location metadata

4. **Inventory System Entities**
   - `GET /api/states`
   - Group entities by domain (`light`, `cover`, `media_player`, `automation`, `camera`, etc.).

5. **Perform Health Audit**
   - Identify `update.*` entities in `on` state.
   - Identify `unavailable` or `unknown` state entities.
   - Report actionable issues rather than raw dumps.

6. **Execute Control Operations**
   - `POST /api/services/<domain>/<service>` with target `entity_id` payload.

## Token Handling & Storage

- Store HA Long-Lived Access Tokens in gopass at `infra/homeassistant-api-token`.
- Avoid leaking tokens in chat history. If a token was pasted in prose, recommend rotating it after operations complete.

## Verification Checklist

Before reporting completion, verify:
- Host/port is reachable
- Authenticated `GET /api/` succeeds
- `GET /api/config` returns system info
- `GET /api/states` returns active entity map
