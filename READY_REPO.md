# Ready Repo Reference
First fully analyzed repo ready for immediate backend adoption.

## Selected: openclaw
**Why:** Gateway + channel abstraction + hook dispatch is highest-impact for backend.

### Architecture
```
OpenClaw
├── Gateway
│   ├── Hook dispatch (/hooks)
│   ├── Session lifecycle
│   └── Agent routing
├── Channels
│   ├── Telegram, WhatsApp, Discord, Slack
│   ├── Signal, iMessage, Google Chat
│   └── HTTP/Webhook
└── Tools/Plugins
    ├── Plugin SDK
    └── ClawHub marketplace
```

### Key Code Patterns
1. Hook dispatch with token auth
2. Channel abstraction layer
3. Session lifecycle state machine
4. Agent allowlist policy
5. Idempotency/header normalization
6. Delivery routing

### Adoption Target
- Backend gateway route `/hooks`
- Channel registry
- Agent/session policy
