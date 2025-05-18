# Brute-Force PIN Verification Tool

This project is a simple Python-based brute-force tool to find a correct 3-digit PIN by interacting with a custom server through raw HTTP POST requests over a socket connection.

## 🔍 Technical Approach (7 points)

To solve this challenge, the script follows these key steps:

### 1. Identify the Server's Address and Port
The server address and port are defined as:
- `HOST = '127.0.0.1'`
- `PORT = 8888`

This sets up the target destination for all POST requests.

### 2. Understand the HTTP Protocol and Craft a Valid POST Request
The tool builds a manual HTTP POST request using socket communication. The request includes:
- A `POST` request line to `/verify`
- Necessary headers like `Host`, `Content-Type`, and `Content-Length`
- A request body formatted as `magicNumber=PIN`

This is done using raw string concatenation and sent via a TCP socket using Python's `socket` module.


