# Minecraft Steam Bridge App 🎮

A lightweight Windows utility that lets you launch Minecraft through Steam and have it correctly show as "Playing" in your Steam status — no more games showing as closed the moment the launcher hands off to the game.

---

## The Problem

When you add Minecraft directly to Steam, Steam launches the Minecraft Launcher and immediately sees it close (because the launcher exits after starting the game). This means Steam stops showing you as playing within seconds of launching.

## The Fix

`Minecraft Steam Bridge App` sits in between. You point Steam at this app instead. It launches the Minecraft Launcher, then watches for it to close — keeping itself alive the entire time so Steam correctly shows you as playing for your whole session.

---

## Download

👉 **[Download the latest release](../../releases/latest)** — grab `minecraft_steam.exe`, no install needed.

---

## Requirements

- Windows 10/11
- Minecraft Launcher installed via the **Xbox app / Microsoft Store** (the default install location is `C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe`)

> If your Minecraft Launcher is installed somewhere else, see [Custom Install Path](#custom-install-path) below.

---

## Setup

1. Download `minecraft_steam.exe` from the [Releases](../../releases/latest) page
2. Place it anywhere on your PC (e.g. `C:\Games\mc-steam-bridge\`)
3. Open Steam and go to **Library → Add a Game → Add a Non-Steam Game**
4. Click **Browse** and select `minecraft_steam.exe`
5. Click **Add Selected Programs**

That's it. Launch Minecraft from Steam and your status will show correctly.

🎨 Customising Your Steam Entry (Name, Icon, Artwork)
Want Minecraft to look proper in your Steam library with the right icon, cover art, and hero image? This YouTube video walks through the full customisation process — just follow along but use minecraft_steam.exe as your target instead of Minecraft.exe:
[📺 Add Minecraft To Steam Library by Tinox412](https://www.youtube.com/watch?v=yk2vDgGguV8)

---

## Custom Install Path

If your Minecraft Launcher isn't in the default `C:\XboxGames\` location, you'll need to build from source and update the path yourself.

1. Clone the repo and open `minecraft_steam.py`
2. Update this line to match your launcher path:
```python
LAUNCHER_PATH = r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"
```
3. Follow the [Build from Source](#build-from-source) steps below

---

## Build from Source

**Requirements:** Python 3.8+

```bash
# Clone the repo
git clone https://github.com/InsaneCipher/MinecraftSteamApp.git
cd MinecraftSteamApp

# Install dependencies
pip install pyinstaller psutil

# Build the .exe
pyinstaller --onefile --noconsole minecraft_steam.py
```

Your `.exe` will be in the `dist/` folder.

---

## How It Works

1. `minecraft_steam.exe` launches `Minecraft.exe` directly
2. It waits for the `Minecraft.exe` process to appear
3. It polls every 3 seconds to check if the launcher is still running
4. When you close the Minecraft Launcher, the bridge exits automatically

Steam sees `minecraft_steam.exe` running the entire time — so your "Playing" status stays active throughout your session.

---

## FAQ

**Does this affect game performance?**
No. The bridge process is tiny and only checks the process list every 3 seconds.

**Does this work with mods / Forge / Fabric?**
Yes — it just watches the launcher. Whatever you launch from inside the launcher works normally.

**Will my friends see me playing "Minecraft" or "mc-steam-bridge"?**
They'll see whatever name you gave the shortcut in Steam. Just name it "Minecraft" when adding it.

**Does this work with other launchers like Prism or CurseForge?**
Not out of the box, but it's easy to adapt — just change `LAUNCHER_PATH` and `LAUNCHER_PROCESS` in the source to match your launcher's `.exe`.

---

## Contributing

PRs are welcome! Some ideas for improvements:
- Auto-detect the launcher install path
- Support for multiple launchers (Prism, CurseForge, etc.)
- A simple GUI for first-time setup

---

## License

MIT — do whatever you want with it.
