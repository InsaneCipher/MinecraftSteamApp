import subprocess
import sys
import time
import os
import psutil

CONFIG_FILE = "config.txt"
DEFAULT_LAUNCHER_PATH = r"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"


def create_default_config():
    """Create a default config.txt if it doesn't exist."""
    with open(CONFIG_FILE, "w") as f:
        f.write("# Minecraft Steam Bridge App - Config\n")
        f.write("# Set the full path to your Minecraft Launcher .exe below\n")
        f.write(f"launcher_path={DEFAULT_LAUNCHER_PATH}\n")
    print(f"Config file created: {CONFIG_FILE}")
    print("Please check the path is correct then relaunch the app.")


def read_config():
    """Read the launcher path from config.txt."""
    with open(CONFIG_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if line.startswith("launcher_path="):
                return line.split("=", 1)[1].strip()
    return None


def validate_path(path):
    """Check the path exists and points to a .exe file."""
    if not path:
        print("Error: No launcher_path found in config.txt.")
        return False
    if not path.lower().endswith(".exe"):
        print(f"Error: Path does not point to a .exe file:\n  {path}")
        return False
    if not os.path.exists(path):
        print(f"Error: File not found at path:\n  {path}")
        return False
    return True


def is_launcher_running():
    """Check if the Minecraft launcher process is running."""
    process_name = "Minecraft.exe"
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and process_name.lower() == proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def main():
    # Create config if it doesn't exist
    if not os.path.exists(CONFIG_FILE):
        create_default_config()
        time.sleep(5)
        sys.exit(0)

    # Read and validate the path from config
    launcher_path = read_config()
    if not validate_path(launcher_path):
        time.sleep(5)
        sys.exit(1)

    # Launch Minecraft
    subprocess.Popen([launcher_path])

    # Wait for the process to start
    time.sleep(5)
    for _ in range(30):
        if is_launcher_running():
            break
        time.sleep(1)

    # Stay alive while launcher is running
    while is_launcher_running():
        time.sleep(3)

    sys.exit(0)


if __name__ == "__main__":
    main()
