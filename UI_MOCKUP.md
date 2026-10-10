# 🎨 UI Mockup: Ngrok Setup Screen

## Visual Layout

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    🔐 Secure File Transfer                                ║
║              Send files securely between laptops over the internet        ║
║                                                                           ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                                                                           ║
║                          🚇 Ngrok Setup Required                          ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │ ℹ️  Welcome! Before you can transfer files, we need to set up      │ ║
║  │    ngrok for secure tunneling.                                      │ ║
║  └─────────────────────────────────────────────────────────────────────┘ ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │ ▼ 📖 What is ngrok and why do I need it?                            │ ║
║  ├─────────────────────────────────────────────────────────────────────┤ ║
║  │                                                                      │ ║
║  │   Ngrok creates a secure tunnel so that files can be transferred   │ ║
║  │   over the internet between two laptops.                            │ ║
║  │                                                                      │ ║
║  │   Think of it as creating a temporary bridge between your computer  │ ║
║  │   and the internet that only works for this app.                    │ ║
║  │                                                                      │ ║
║  │   It's safe, free, and takes just 2 minutes to set up!             │ ║
║  │                                                                      │ ║
║  └─────────────────────────────────────────────────────────────────────┘ ║
║                                                                           ║
║  📝 Setup Steps:                                                         ║
║                                                                           ║
║  Step 1: Create a free ngrok account                                    ║
║  • Go to: ngrok.com                                                      ║
║  • Click "Sign up" (it's free!)                                          ║
║  • Use Google/GitHub or email to sign up                                 ║
║                                                                           ║
║  Step 2: Get your authentication token                                   ║
║  • After signing up, you'll see your dashboard                           ║
║  • Look for "Your Authtoken" section                                     ║
║  • Click "Copy" to copy your token                                       ║
║                                                                           ║
║  ┌───────────────────────────────────────────────────────────────────┐  ║
║  │                                                                    │  ║
║  │  [Image: Ngrok Dashboard with token highlighted]                  │  ║
║  │  Find your token in the ngrok dashboard                            │  ║
║  │                                                                    │  ║
║  └───────────────────────────────────────────────────────────────────┘  ║
║                                                                           ║
║  Step 3: Paste your token below                                          ║
║                                                                           ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                                                                           ║
║  Paste your ngrok auth token here:                                       ║
║  ┌──────────────────────────────────────────────────────────┐           ║
║  │ •••••••••••••••••••••••••••••••••••••••••••••••••••••   │ [🚀 Config]║
║  └──────────────────────────────────────────────────────────┘           ║
║                                                                           ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │ ▼ ❓ Need Help?                                                      │ ║
║  ├─────────────────────────────────────────────────────────────────────┤ ║
║  │                                                                      │ ║
║  │ Common Issues:                                                       │ ║
║  │                                                                      │ ║
║  │ 1. "Invalid token" error:                                           │ ║
║  │    • Make sure you copied the ENTIRE token                          │ ║
║  │    • Check for any extra spaces                                     │ ║
║  │                                                                      │ ║
║  │ 2. "Ngrok command not found":                                       │ ║
║  │    • Download from: https://ngrok.com/download                      │ ║
║  │                                                                      │ ║
║  │ Video Tutorial: [How to get ngrok token]                            │ ║
║  │                                                                      │ ║
║  └─────────────────────────────────────────────────────────────────────┘ ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │ ▼ ⚙️ Advanced: Already configured ngrok via command line?          │ ║
║  ├─────────────────────────────────────────────────────────────────────┤ ║
║  │                                                                      │ ║
║  │ If you've already configured ngrok using:                           │ ║
║  │ ngrok config add-authtoken YOUR_TOKEN                               │ ║
║  │                                                                      │ ║
║  │ [✓ I've already configured ngrok]                                   │ ║
║  │                                                                      │ ║
║  └─────────────────────────────────────────────────────────────────────┘ ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## Success State

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    🔐 Secure File Transfer                                ║
║              Send files securely between laptops over the internet        ║
║                                                                           ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                                                                           ║
║                          🚇 Ngrok Setup Required                          ║
║                                                                           ║
║  [Previous content above...]                                             ║
║                                                                           ║
║  Paste your ngrok auth token here:                                       ║
║  ┌──────────────────────────────────────────────────────────┐           ║
║  │ •••••••••••••••••••••••••••••••••••••••••••••••••••••   │ [🚀 Config]║
║  └──────────────────────────────────────────────────────────┘           ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │ ✅ Ngrok configured successfully!                                    │ ║
║  └─────────────────────────────────────────────────────────────────────┘ ║
║                                                                           ║
║  ┌─────────────────────────────────────────────────────────────────────┐ ║
║  │ ℹ️  🎉 You're all set! Click the button below to start using the   │ ║
║  │    app.                                                              │ ║
║  └─────────────────────────────────────────────────────────────────────┘ ║
║                                                                           ║
║                      [🚀 Start Using App]                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## Main App with Settings

```
╔══════════════════════════════╦════════════════════════════════════════════╗
║ 🔐 Secure File Transfer      ║                                            ║
║ Send files securely...       ║         📤 Send a File Selected            ║
║                              ║                                            ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║                                            ║
║                              ║  Choose a file to send                     ║
║ Choose Your Action           ║  ┌──────────────────────────────────────┐ ║
║                              ║  │  [Browse files]                       │ ║
║ ⦿ 📤 Send a File             ║  └──────────────────────────────────────┘ ║
║ ○ 📥 Receive a File          ║                                            ║
║                              ║                                            ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║                                            ║
║                              ║                                            ║
║ How it works:                ║                                            ║
║                              ║                                            ║
║ To Send:                     ║                                            ║
║ 1. Click 'Send a File'       ║                                            ║
║ 2. Upload your file          ║                                            ║
║ 3. Click 'Start Sharing'     ║                                            ║
║ 4. Share URL and key         ║                                            ║
║                              ║                                            ║
║ To Receive:                  ║                                            ║
║ 1. Click 'Receive a File'    ║                                            ║
║ 2. Enter URL and key         ║                                            ║
║ 3. Click 'Download File'     ║                                            ║
║ 4. Save your file            ║                                            ║
║                              ║                                            ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║                                            ║
║                              ║                                            ║
║ ▼ ⚙️ Settings                ║                                            ║
║ ├─────────────────────────   ║                                            ║
║ │ Ngrok Configuration        ║                                            ║
║ │ ✅ Ngrok is configured     ║                                            ║
║ │    and ready               ║                                            ║
║ │                            ║                                            ║
║ │ [🔄 Reconfigure Token]     ║                                            ║
║ │                            ║                                            ║
║ │─────────────────────────   ║                                            ║
║ │ About                      ║                                            ║
║ │ Secure File Transfer v1.0  ║                                            ║
║ │ Encrypted P2P file sharing ║                                            ║
║ └─────────────────────────   ║                                            ║
║                              ║                                            ║
╚══════════════════════════════╩════════════════════════════════════════════╝
```

## Color Scheme

### Used in the App:

**Info Boxes (Blue):**
```
┌────────────────────────────┐
│ ℹ️  Information message    │
└────────────────────────────┘
```

**Success (Green):**
```
┌────────────────────────────┐
│ ✅ Success message         │
└────────────────────────────┘
```

**Warning (Yellow/Orange):**
```
┌────────────────────────────┐
│ ⚠️  Warning message        │
└────────────────────────────┘
```

**Error (Red):**
```
┌────────────────────────────┐
│ ❌ Error message           │
└────────────────────────────┘
```

**Primary Button:**
```
[🚀 Primary Action]  ← Blue/Accent color
```

**Secondary Button:**
```
[Secondary Action]  ← Gray
```

## Interactive Elements

### Expandable Sections:
```
Before Click:
▼ Section Title
├─ Content shown

After Click:
▶ Section Title
(Content hidden)
```

### Input Fields:
```
Label:
┌────────────────────────────┐
│ [User types here]          │
└────────────────────────────┘
```

### Password Fields:
```
Label:
┌────────────────────────────┐
│ •••••••••••••••••••••      │
└────────────────────────────┘
```

## Responsive Design

### Desktop (Wide):
- Sidebar on left (30%)
- Main content on right (70%)
- All elements visible

### Mobile (Narrow):
- Sidebar collapses to hamburger menu
- Main content full width
- Sections stack vertically

## Animation & Feedback

### Loading State:
```
⏳ Configuring ngrok...
(Spinning loader)
```

### Success State:
```
✅ Success message
(Balloons animation 🎈)
```

### Error State:
```
❌ Error message
(Shake animation)
```

## Accessibility

✅ Clear labels for all inputs
✅ Help text for complex fields
✅ High contrast colors
✅ Keyboard navigation support
✅ Screen reader friendly
✅ Focus indicators visible

## User Flow Visualization

```
[Open App]
    ↓
Is ngrok configured?
    ↓
   NO ─→ [Setup Screen]
    │        ↓
    │   [Follow Steps]
    │        ↓
    │   [Enter Token]
    │        ↓
    │   [Click Configure]
    │        ↓
    │   [Success?]
    │        ↓
    │    YES ┘
    ↓
   YES
    ↓
[Main App Screen]
    ↓
[Select Send or Receive]
    ↓
[Use App Features]
```

---

This mockup shows exactly what users will see when they first run the app!
