import asyncio
import urllib.parse
import os

TEMPLATES_DIR = 'templates'
DB_FILE = 'db.txt'

async def handle_client(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received request from {addr}")

    if not message:
        writer.close()
        await writer.wait_closed()
        return

    headers = message.split('\r\n')
    request_line = headers[0]
    method, path, _ = request_line.split()

    print(f"Method: {method}, Path: {path}")

    if method == 'GET':
        if path == '/':
            await serve_file(writer, 'index.html')
        elif path == '/register':
            await serve_file(writer, 'register.html')
        else:
            await send_404(writer)

    elif method == 'POST' and path == '/submit':
        body = message.split('\r\n\r\n', 1)[1]
        post_data = urllib.parse.parse_qs(body)
        username = post_data.get('username', [''])[0]
        email = post_data.get('email', [''])[0]

        if username and email:
            with open(DB_FILE, 'a') as f:
                f.write(f"{username} {email}\n")

            # After writing, maybe redirect back to home
            response = ('HTTP/1.1 303 See Other\r\n'
                        'Location: /\r\n\r\n')
            writer.write(response.encode())
        else:
            await send_400(writer)

    else:
        await send_405(writer)

    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def serve_file(writer, filename):
    file_path = os.path.join(TEMPLATES_DIR, filename)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        response = ('HTTP/1.1 200 OK\r\n'
                    'Content-Type: text/html\r\n'
                    'Connection: close\r\n\r\n' +
                    content)
    except FileNotFoundError:
        response = ('HTTP/1.1 404 Not Found\r\n'
                    'Content-Type: text/html\r\n'
                    'Connection: close\r\n\r\n'
                    '<h1>404 Not Found</h1>')
    writer.write(response.encode())

async def send_404(writer):
    response = ('HTTP/1.1 404 Not Found\r\n'
                'Content-Type: text/html\r\n'
                'Connection: close\r\n\r\n'
                '<h1>404 Not Found</h1>')
    writer.write(response.encode())

async def send_400(writer):
    response = ('HTTP/1.1 400 Bad Request\r\n'
                'Content-Type: text/html\r\n'
                'Connection: close\r\n\r\n'
                '<h1>400 Bad Request</h1>')
    writer.write(response.encode())

async def send_405(writer):
    response = ('HTTP/1.1 405 Method Not Allowed\r\n'
                'Content-Type: text/html\r\n'
                'Connection: close\r\n\r\n'
                '<h1>405 Method Not Allowed</h1>')
    writer.write(response.encode())

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8085)
    print("Server started on http://127.0.0.1:8085")
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
