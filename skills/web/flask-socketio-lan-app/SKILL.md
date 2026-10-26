---
name: flask-socketio-lan-app
description: "Build or maintain a Flask + Flask-SocketIO + vanilla-JS real-time app (chat, WebRTC voice, file uploads) that runs on a local network with JSON-file storage and Jinja2 templates."
license: MIT
compatibility: opencode
metadata:
  category: web
  source: ["SocialCord"]
  origin: derived
  language: en
  scope: generic
---

# Flask + Socket.IO LAN app

## Stack

Python 3, Flask, Flask-SocketIO, Jinja2, vanilla JS, Socket.IO client, WebRTC with a STUN server, JSON files for storage, self-signed certificate (browsers require HTTPS for microphone access).

## Layout

```
app/
  __init__.py  routes_*.py  socket_events.py
  api/v1/routes.py
  models/        # JSON-backed models
  templates/  static/
```

## Patterns

- **REST for CRUD, sockets for live events.** Creating a server or channel is an HTTP call; message delivery and presence are socket events.
- **Event names carry a prefix** (`sc:`) so project events never collide with library events.
- **WebRTC signalling over sockets**: offer, answer and ICE candidates are relayed by the server, which never touches media.
- **Uploads**: limit to 20 MB, store under a server-owned path, never trust the client file name.

## Gotchas seen in the project

- `activeServerId` declared twice in the front-end script silently breaks selection.
- `$()` is a `getElementById` helper: a missing element fails silently, so check ids after template edits.
- Clicking a voice channel must call `selectChannel` first, or the UI state and the voice session disagree.

## Checklist

- [ ] HTTPS enabled for voice.
- [ ] Every socket event has a prefix and a documented payload.
- [ ] Upload size and name validated server-side.
- [ ] Template ids match the JS selectors.

## Provenance

`SocialCord`.
