import os
import sys
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import GOOGLE_CREDENTIALS_PATH

VENV_NAME = "venv"
CREDENTIALS_DIR = "credentials"


def create_venv():
    if not os.path.isdir(VENV_NAME):
        print("[BUILD] Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", VENV_NAME], check=True)
    else:
        print("[BUILD] Virtual environment already exists.")


def install_requirements():
    pip_path = os.path.join(VENV_NAME, "Scripts" if os.name == "nt" else "bin", "pip")

    if os.path.isfile("requirements.txt"):
        print("[BUILD] Installing dependencies...")
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
    else:
        print("[WARNING] requirements.txt not found. Skipping dependency installation.")


def check_credentials():
    print("[INFO] Checking credentials...")

    if not os.path.isdir(CREDENTIALS_DIR):
        print(f"[ERROR] '{CREDENTIALS_DIR}/' folder not found.")
        return False

    creds_path = os.path.join(CREDENTIALS_DIR, GOOGLE_CREDENTIALS_PATH)

    if not os.path.isfile(creds_path):
        print(f"[ERROR] '{GOOGLE_CREDENTIALS_PATH}' not found inside '{CREDENTIALS_DIR}/'.")
        return False

    print("[BUILD] Credentials check passed.")
    return True


def main():
    create_venv()
    install_requirements()

    if not check_credentials():
        print("[FAIL] Build failed due to missing credentials.")
        sys.exit(1)

    print("[SUCCESS] Build completed successfully.")


if __name__ == "__main__":
    main()