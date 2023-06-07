from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import requests

# Generate a random encryption key
key = get_random_bytes(16)

# Encrypt the data
def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return b64encode(cipher.iv + ciphertext).decode()

# Decrypt the data
def decrypt_data(encrypted_data):
    encrypted_data = b64decode(encrypted_data)
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    return decrypted_data.decode()

# Simulate sending encrypted data via phone number
def send_data(phone_number, encrypted_data):
    url = 'https://example.com/send-data'
    payload = {
        'phone_number': phone_number,
        'encrypted_data': encrypted_data
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Data sent successfully!")
    else:
        print("Failed to send data.")

# Example usage
data_to_transfer = "Sensitive data"
encrypted_data = encrypt_data(data_to_transfer)

# Simulate sending encrypted data to a phone number
phone_number = "+911234567890"
send_data(phone_number, encrypted_data)

# Simulate receiving encrypted data on the other end
received_encrypted_data = "encrypted_data_received_from_phone_number"

# Decrypt the received data
decrypted_data = decrypt_data(received_encrypted_data)
print("Decrypted data:", decrypted_data)
