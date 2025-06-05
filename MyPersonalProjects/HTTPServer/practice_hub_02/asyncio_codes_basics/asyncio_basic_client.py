import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print("Connection from {}".format(addr))
    while data := await reader.read(100):
        print("Received: {}".format(data.decode()))
        writer.write(data)
        await writer.drain()
    print("Closing connection")
    writer.close()

async def main():
    host_addr = "localhost"
    port_num = 54321
    server = await asyncio.start_server(handle_client, host_addr, port_num, reuse_address=True)
    # server = await asyncio.start_server(handle_client, 'localhost', 12345)
    async with server:
        await server.serve_forever()

asyncio.run(main())