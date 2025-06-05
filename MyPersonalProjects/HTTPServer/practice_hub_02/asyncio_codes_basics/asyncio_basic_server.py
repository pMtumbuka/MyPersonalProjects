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
    print("Server Running on {}: Port {}...".format(host_addr, port_num))
    async with server:
        await server.serve_forever()

asyncio.run(main())


'''

try:
    while True:
        data = await reader.read(100)
        if not data:
            break
        writer.write(data)
        await writer.drain()
except asyncio.CancelledError:
    logger.debug("Connection cancelled.")
except ConnectionResetError:
    logger.warning("Connection reset by client.")
except BrokenPipeError:
    logger.warning("Client disconnected before message could be sent.")
except asyncio.TimeoutError:
    logger.warning("Client took too long to respond.")
except Exception as e:
    logger.exception(f"Unhandled error: {e}")
finally:
    writer.close()
    await writer.wait_closed()


'''