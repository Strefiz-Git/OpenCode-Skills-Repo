---
name: android-core-app-split
description: "Structure a Kotlin project as a pure JVM :core module plus an Android :app module, test the core with Gradle, and verify the app by building the APK and measuring the screen on an emulator because it has no unit tests."
license: MIT
compatibility: opencode
metadata:
  category: mobile
  source: ["QrCodeGenerator"]
  origin: derived
  language: en
  scope: generic
---

# Android core/app split

## Layout

```
kotlin/
  build.gradle.kts  settings.gradle.kts
  gradlew  gradlew.bat  gradle/wrapper/
  core/       # pure JVM, all logic, all unit tests
  android/    # :app, UI only
```

## Rules

- **All logic lives in `:core`.** `:app` is a thin UI layer.
- `:app` has no `src/test`, so `:app:test` does not exist; do not run it.
- Verify the app by **building the APK and measuring the screen on an emulator** (the project keeps a `verificar-app.py` script for this).
- Pin the Java toolchain (21).
- Commit `gradle-wrapper.jar` with a comment explaining why.
- Cross-check core output with an independent reference (ZXing in the QR project).

## Commands

```bash
./gradlew :core:test
./gradlew :android:assembleDebug
```

## Checklist

- [ ] No Android imports in `:core`.
- [ ] `:core:test` green.
- [ ] APK builds and the screen was checked on an emulator.

## Provenance

`QrCodeGenerator` (Kotlin/Android stack).
