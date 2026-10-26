---
name: fabric-known-good-baseline
description: "Reuse a known-good Fabric build baseline (Minecraft 26.3, Loom, Gradle wrapper, Java 25, Fabric API, Mod Menu versions) taken from a sibling mod that already compiles."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["Minecraft-MultyCore-Mod", "RocketWithSpearMod", "Slime-Chunk-Finder-Helper-Mod", "easy-building-minecraft-mod", "ScreenMine", "OtimizedTNT"]
  origin: derived
  language: en
  scope: generic
---

# Known-good Fabric baseline

Starting a new mod from scratch wastes time on version mismatches. **Copy the build files from a sibling mod that already compiles** and change only the identity (mod id, package, name).

## Procedure

1. Pick the newest sibling that builds (`Slime-Chunk-Finder-Helper-Mod`, `RocketWithSpearMod`, `Minecraft-MultyCore-Mod`).
2. Copy `gradlew`, `gradlew.bat`, `gradle/wrapper/*` (including `gradle-wrapper.jar`), `build.gradle`, `gradle.properties`, `settings.gradle`.
3. Edit `gradle.properties` (`mod_version`, `maven_group`, `archives_base_name`) and `fabric.mod.json`.
4. Run the wrapper build once before writing any code.
5. Commit `gradle-wrapper.jar` and explain why in a `.gitignore` comment (`!gradle/wrapper/gradle-wrapper.jar`).

## What the baseline pins

| Item | Value seen in the repos |
|---|---|
| Minecraft | 26.3 |
| Java toolchain | 25 |
| Build plugin | Fabric Loom |
| Mod Menu (optional) | 21.0.0 |
| Fabric API | the version matching 26.3 in the sibling `gradle.properties` |

Always re-read the sibling files for exact versions; these values change with each Minecraft release.

## Checklist

- [ ] Wrapper build passes before any feature work.
- [ ] Toolchain versions are pinned, not "latest".
- [ ] `gradle-wrapper.jar` is committed.

## Provenance

`Minecraft-MultyCore-Mod`, `RocketWithSpearMod`, `Slime-Chunk-Finder-Helper-Mod`, `easy-building-minecraft-mod`, `ScreenMine`, `OtimizedTNT` (decision D-008 in the Slime mod: copy the wrapper from a mod that already builds).
