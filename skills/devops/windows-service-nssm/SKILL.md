---
name: windows-service-nssm
description: "Run a Node or other long-lived program as an auto-starting Windows service with NSSM, with rotating stdout/stderr logs, plus install, check and uninstall PowerShell scripts."
license: MIT
compatibility: opencode
metadata:
  category: devops
  source: ["Discord-Easy-Music-Bot"]
  origin: derived
  language: en
  scope: generic
---

# Windows service with NSSM

## install-service.ps1 shape

```powershell
#Requires -RunAsAdministrator
$name = "MyBot"
if (Get-Service $name -ErrorAction SilentlyContinue) {
    nssm stop $name; nssm remove $name confirm      # idempotent
}
npm run build
nssm install $name "cmd.exe" "/c npm start"
nssm set $name AppDirectory $PWD
nssm set $name AppEnvironmentExtra "NODE_ENV=production"
nssm set $name AppStdout "$PWD\logs\out.log"
nssm set $name AppStderr "$PWD\logs\err.log"
nssm set $name AppRotateFiles 1
nssm set $name AppRotateSeconds 86400
nssm set $name AppRotateBytes 10485760
nssm set $name Start SERVICE_AUTO_START
nssm start $name
```

## Rules

- **Idempotent**: stop and remove before installing.
- Run `npm start` through `cmd /c`.
- Rotate logs daily and by size.
- Run PowerShell as Administrator.
- Ship `check-service.ps1` and `uninstall-service.ps1` next to the installer.
- Secrets stay in `.env`, not in the service definition.
- Check NSSM's licence before redistributing it.

## Checklist

- [ ] Install can be run twice safely.
- [ ] Logs rotate.
- [ ] Service starts after a reboot.

## Provenance

`Discord-Easy-Music-Bot`.
