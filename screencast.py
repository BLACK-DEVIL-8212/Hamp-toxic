import socket
import pyautogui

# Set up the server
HOST = '127.0.0.1'  # IP address of the server
PORT = 4444  # Port number to use
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
time.sleep(2)
print(f"Server started on {HOST}:{PORT}")

# Accept a client connection
conn, addr = s.accept()
print('Connected by', addr)

try:
    while True:
        # Capture the screen image
        screenshot = pyautogui.screenshot()
        # Resize the image if needed
        # screenshot = screenshot.resize((800, 600))

        # Convert the image to bytes
        image_bytes = screenshot.tobytes()

        # Send the image size first
        size = len(image_bytes).to_bytes(4, byteorder='big')
        conn.sendall(size)

        # Send the image data
        conn.sendall(image_bytes)
finally:
    # Close the connection
    conn.close()
    s.close()
