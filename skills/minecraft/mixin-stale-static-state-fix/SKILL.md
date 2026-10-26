---
name: mixin-stale-static-state-fix
description: "Fix crashes in a third-party Minecraft mod caused by static state that survives leaving a world (NullPointerException when Minecraft.player becomes null) with a tiny companion mixin on Minecraft.tick, built per loader."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["fix-easybuilding", "easy-building-minecraft-mod"]
  origin: derived
  language: en
  scope: generic
---

# Fix stale static state with a companion mixin

**Symptom:** after leaving a world, the other mod throws a `NullPointerException` on `Minecraft.player` because a static holder (a plane mode, a selection, a cache) still points at the old session.

## Fix

Write a tiny mod that clears the stale state when there is no player:

```java
@Mixin(Minecraft.class)
public abstract class MinecraftMixin {
    @Inject(method = "tick()V", at = @At("HEAD"), require = 0, remap = false)
    private void companion$clearStale(CallbackInfo ci) {
        Minecraft mc = (Minecraft) (Object) this;
        if (mc.player == null) PlaneMode.clear();
    }
}
```

- `require = 0` keeps the mod loading if the target changes between versions.
- Keep the mixin **one method, one purpose**. Do not patch the other mod; call its public `clear()`.
- One source tree per loader: `src/fabric/java` and `src/neoforge/java`, sharing the same logic.
- A small `build.ps1` that runs `javac` and `jar` is enough when Gradle is overkill.

## Checklist

- [ ] Reproduce the crash first (leave the world, re-enter).
- [ ] Companion mod loads without the broken mod present.
- [ ] Both loaders build.
- [ ] Report the bug upstream and note the version the fix targets.

## Provenance

`fix-easybuilding` (the fix) and `easy-building-minecraft-mod` (the affected mod).
