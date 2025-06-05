
import asyncio
# import socket
# import sys
# import os

async def greet():
    print("Hello")
    await asyncio.sleep(1)  # Pauses for 1 second without blocking
    print("World")

async def main():
   
   await greet() 
   
   await asyncio.gather(greet(), greet())  # run concurrently
    
if __name__ == "__main__":
    
    # main()NOT recommended for asyncio
    
    asyncio.run(main()) # first way of sunning this
    
    # second way of running this, getting the event loop manually
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())
    
    # testig testing using an abstraction with the gather() function
    # asyncio.run(asyncio.gather(main())

'''

Let's count what happens:

    In main():

        await greet()  # runs greet() normally

        await asyncio.gather(greet(), greet())  # runs two greet() coroutines concurrently

    Each call to main() results in:

        Hello (first greet())

        1-second pause

        World (first greet() ends)

        Two more Hello prints immediately (from gather(...))

        1-second pause

        Two World prints (from gather(...))

    So one main() call = 5 prints:

Hello
World
Hello
Hello
World
World

'''

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