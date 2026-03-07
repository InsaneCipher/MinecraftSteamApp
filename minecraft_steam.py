import subprocess
import sys
import time
import psutil

# Path to the Minecraft Launcher exe (XboxGames install location)
LAUNCHER_PATH = r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"

# Process name to watch for
LAUNCHER_PROCESS = "Minecraft.exe"


def is_launcher_running():
    """Check if Minecraft.exe is currently running."""
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and LAUNCHER_PROCESS.lower() == proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def main():
    # Launch the Minecraft Launcher directly
    subprocess.Popen([LAUNCHER_PATH])

    # Wait a moment for the process to start
    time.sleep(5)

    # Wait until the launcher process is confirmed running (up to 30 seconds)
    for _ in range(30):
        if is_launcher_running():
            break
        time.sleep(1)

    # Stay alive as long as the launcher is open
    while is_launcher_running():
        time.sleep(3)

    # Launcher was closed — exit cleanly
    sys.exit(0)


if __name__ == "__main__":
    main()