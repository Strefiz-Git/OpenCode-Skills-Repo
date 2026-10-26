---
name: resilient-external-tool-runner
description: "Wrap an external tool or flaky network step (such as yt-dlp) in Python with classified failures, bounded exponential-backoff retries, per-item debug logs, a master log, an auto-created config file, an outdated-version warning and a single-file PyInstaller build."
license: MIT
compatibility: opencode
metadata:
  category: python
  source: ["Spotify_Playlist_Download_x64"]
  origin: derived
  language: en
  scope: generic
---

# Resilient external tool runner

## Ingredients

1. **Version check**: warn when the tool is outdated (most yt-dlp failures are fixed by updating).
2. **Config auto-created** on first run with commented defaults.
3. **Failure classification**: network, rate limit, not found, DRM/protected, unknown. Each class has a policy.
4. **Bounded retries** with exponential backoff and a hard cap.
5. **One result record per item** (`ok`, `failed`, `skipped`, reason).
6. **Two logs**: a per-item debug log and a master summary log.
7. **Use the tool's hooks/API** rather than parsing its stdout.

## Pattern

```python
import time

def run_with_retries(job, max_tries=4, base_delay=2.0):
    for attempt in range(1, max_tries + 1):
        try:
            return job()
        except Exception as exc:
            kind = classify(exc)
            if kind in ("drm", "not_found"):      # retrying cannot help
                raise
            if attempt == max_tries:
                raise
            time.sleep(base_delay * 2 ** (attempt - 1))
```

## Rules

- Classify DRM/protected content and **report it**; never retry it.
- Cap retries; an unbounded loop hides a real outage.
- Logs must say which item, which attempt, which class of failure.

## Packaging and versioning

- `pyinstaller --onefile` for a single executable.
- Do not commit installers, ffmpeg or build output (one source repo reached ~428 MB because of this).
- One script plus git tags; move old versions to `archive/`.

## Checklist

- [ ] A failing item never stops the batch.
- [ ] Summary log lists every item with its reason.
- [ ] Repo contains no binaries or build output.

## Provenance

`Spotify_Playlist_Download_x64`.
