# Ready Repo Reference
First fully analyzed and pattern-extracted repo for immediate adoption.

## Selected: openclaw
**Why:** Gateway + channel architecture is the highest-impact pattern for backend.

### Core Pattern
Personal AI assistant gateway connecting models, tools, messaging channels.

### Architecture
```
OpenClaw
├── Gateway (control plane)
│   ├── Session management
│   ├── Tool registry
│   ├── Event bus
│   └── Channel adapters
├── Channels
│   ├── WhatsApp
│   ├── Telegram
│   ├── Slack
│   ├── Discord
│   ├── Google Chat
│   ├── Signal
│   └── iMessage
└── Skills/Plugins
    ├── Self-extending capabilities
    └── ClawHub marketplace
```

### Key Code Patterns
1. Channel abstraction layer
2. Tool registration/discovery
3. Session state management
4. Event-driven architecture
5. Plugin marketplace

### Adoption Status
- [ ] Backend channel abstraction
- [ ] Multi-platform messaging
- [ ] Skill marketplace
- [ ] Gateway control plane

## Next Ready Repos
1. browser-use - Browser automation
2. MetaGPT - SOP-based multi-agent
3. planning-with-files - Persistent planning
4. screenpipe - Local memory capture
