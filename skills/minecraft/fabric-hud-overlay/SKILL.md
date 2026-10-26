---
name: fabric-hud-overlay
description: "Render a HUD element or world overlay in a Fabric client mod for Minecraft 26.x, register a keybinding, and read vanilla debug flags (such as F3+G chunk borders) through public API instead of a mixin. Use for HUDs, overlays, toggle keys, or when tempted to add a mixin just to read a vanilla flag."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["Slime-Chunk-Finder-Helper-Mod", "easy-building-minecraft-mod"]
  origin: derived
  language: en
  scope: generic
---

# Fabric HUD / overlay

## Steps

1. **HUD element**: register with `HudElementRegistry.addLast(id, renderer)` from the client entrypoint. Keep the renderer cheap; cache anything computed per chunk or per tick.
2. **Keybinding**: create it with `InputConstants.Type.KEYBOARD` and a key such as `InputConstants.KEY_K`, register it in the client entrypoint and poll `consumeClick()` in a client tick event.
3. **Read vanilla flags without a mixin**: before writing a mixin to reach a flag (for example the F3+G chunk-borders state), inspect the public API:

   ```bash
   javap -classpath <minecraft-jar> -public <fully.qualified.Class>
   ```

   If a public getter exists, call it. A mixin is the last resort, not the first.
4. **Honest states**: when information may be unavailable (for example the world seed in multiplayer), show three explicit states - known, unknown, unavailable - instead of guessing.
5. **Slime-chunk example**: a chunk is a slime chunk when `WorldgenRandom.seedSlimeChunk(chunkX, chunkZ, seed, 987234911L).nextInt(10) == 0`. Draw those chunks in green on the chunk-border overlay.

## Pitfalls

- Reading the seed on a server that does not share it: show "unknown", never a wrong answer.
- Doing world queries every frame: cache per chunk and refresh on chunk change.
- Hard-coding the HUD position: expose it in the mod config (see `fabric-client-config-modmenu`).

## Checklist

- [ ] HUD renders with no exception when not in a world.
- [ ] Keybind appears in Controls and works.
- [ ] No mixin where a public API exists.
- [ ] Multiplayer states are explicit.

## Provenance

`Slime-Chunk-Finder-Helper-Mod` (HUD, keybind, slime formula, `javap` technique), `easy-building-minecraft-mod` (overlay rendering).
