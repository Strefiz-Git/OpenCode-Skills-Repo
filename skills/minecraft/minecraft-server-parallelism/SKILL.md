---
name: minecraft-server-parallelism
description: "Plan or review a Minecraft server mod that spreads work across threads (worker pools, regionised ticking, offloading chunk IO, light or pathfinding) while keeping legacy mods safe."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["Minecraft-MultyCore-Mod"]
  origin: derived
  language: en
  scope: generic
---

# Minecraft server parallelism

## Hard truths

- There is **no switch** that makes a vanilla server use N cores. The server tick is single-threaded by design.
- The hard part is **ownership of mutable world state**, not the thread pool. Anything two threads can touch needs a rule.
- Mods that are not thread-safe must stay on the main thread (MultiCore keeps incompatible mods on core 1 and distributes vanilla work).

## Approach

1. **Classify work**: pure computation (safe to offload), IO (offload), world mutation (owned by one region/thread), third-party mod callbacks (main thread).
2. **Start with the cheap wins**: chunk IO, light, pathfinding snapshots, entity AI that reads immutable snapshots.
3. **Regionised ticking** only after the above, because it forces ownership rules on everything.
4. **Allow-list, not deny-list**, for mods that may run off-thread.
5. **Benchmark before and after** with two scenarios: S-A (many idle entities/chunks) and S-B (heavy redstone/TNT/mob farms); report ticks per second and 99th-percentile tick time.

## Prior art to read first

Folia, C2ME, Lithium, VMP, Moonrise. See `references/prior-art.md`.

## Checklist

- [ ] Every offloaded task has a documented thread-ownership rule.
- [ ] Legacy/incompatible mods verified to stay on the main thread.
- [ ] Benchmarks recorded for S-A and S-B, with the method in the repo.
- [ ] Config read once at startup; changing it needs a restart.

## Provenance

`Minecraft-MultyCore-Mod` (`docs/RESEARCH.md`, `docs/BENCHMARKS.md`, decisions D-003 to D-013).
