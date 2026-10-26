---
name: fabric-optional-server-payload
description: "Design a Fabric client mod that works on vanilla servers and only uses a custom network payload when the server also has the mod. Use when adding C2S or S2C packets, CustomPacketPayload records, PayloadTypeRegistry, ClientPlayNetworking.canSend, or deciding between client-only and client+server behaviour."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["RocketWithSpearMod", "Slime-Chunk-Finder-Helper-Mod", "Minecraft-MultyCore-Mod"]
  origin: derived
  language: en
  scope: generic
---

# Optional server payload for a Fabric client mod

A client mod must **never require** the server to have the mod. A custom payload is an enhancement that switches on only when the server advertises support.

## Rules

1. **Client-only first.** Every feature must have a vanilla-server fallback (use vanilla packets or local state). Ship the payload as an upgrade path.
2. **One `record` per packet** implementing `CustomPacketPayload`, with its own `TYPE` and `STREAM_CODEC`. Keep them in a `network/` package.
3. **Register the payload type on both sides** with `PayloadTypeRegistry` (`playC2S()` / `playS2C()`), even in a client-only jar, so `canSend` can answer.
4. **Gate every send** with `ClientPlayNetworking.canSend(Payload.TYPE)`; if it is false, take the vanilla path.
5. **Never trust the client on the server.** Validate every field (range, ownership, cooldown) before acting; the payload only *requests*.
6. **`fabric.mod.json` environment**: `"environment": "*"` when the same jar runs on both sides, `"client"` for a client-only mod.
7. **Version the protocol**: put a protocol number in the first payload (hello/handshake) so old and new builds degrade gracefully.

## Decision table

| Need | Client-only | Client + optional server |
|---|---|---|
| Read what the client already sees (HUD, overlays) | yes | not needed |
| Act on server state the client cannot see | no | yes, via S2C payload |
| Server must authorise an action | no | yes, C2S request + server validation |
| Work on a vanilla server | required | fallback path required |

## Checklist

- [ ] Mod starts and works on a vanilla server and on a server without the mod.
- [ ] Every `send` is behind `canSend`.
- [ ] Server handler validates input and runs on the server thread.
- [ ] Payload records are small, immutable and documented.

## Provenance

`RocketWithSpearMod` (optional server side), `Slime-Chunk-Finder-Helper-Mod` (client-only with honest states in multiplayer), `Minecraft-MultyCore-Mod` (server-side). The decision table is a synthesis, not copied from a file.
