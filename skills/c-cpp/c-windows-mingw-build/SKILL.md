---
name: c-windows-mingw-build
description: "Build a small C program for Windows with MinGW gcc from a PowerShell script, and embed binary files (images, data) into the executable with objcopy."
license: MIT
compatibility: opencode
metadata:
  category: c-cpp
  source: ["Bk_Query"]
  origin: derived
  language: en
  scope: generic
---

# C on Windows with MinGW

## Build script shape (`build.ps1`)

```powershell
$ErrorActionPreference = "Stop"
gcc -Wall -Wextra -o app.exe main.c data.o -lm
if ($LASTEXITCODE -ne 0) { throw "gcc failed" }
```

## Embed a binary file

```powershell
if (-not (Test-Path data.o) -or (Get-Item data.bin).LastWriteTime -gt (Get-Item data.o).LastWriteTime) {
    objcopy -I binary -O pe-x86-64 --binary-architecture i386 data.bin data.o
}
```

Reference the symbols from C:

```c
extern const unsigned char _binary_data_bin_start[];
extern const unsigned char _binary_data_bin_end[];
extern const unsigned char _binary_data_bin_size[];   /* address is the size */
```

Link `data.o`. Regenerate it only when the source file changes.

## Pitfalls

- The symbol name derives from the file path: build from the file's folder or the names change.
- Always check `$LASTEXITCODE`; PowerShell does not stop on native command failure by itself.
- Keep `-Wall -Wextra` on.

## Checklist

- [ ] Build script fails loudly.
- [ ] Embedded data object is rebuilt only when needed.

## Provenance

`Bk_Query`.
