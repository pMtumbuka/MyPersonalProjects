"""

THE FOLLOWING CODE FOR THE HTTP SERVER IS A COMBINATION OF CHUNKS OF CODES 
THAT WERE SOURCED FROM DIFFERENT REFERENCES AS DISCRIBED IN GREAT DETAILS IN 
THE "references.txt" FILE ***(MOSTLY FROM PYTHON MODULE'S SOURCE CODES ON GITHUB)***

"""

import asyncio
import urllib.parse # imports URL form parsing tools 
import os # provides a portable way to interact with the operating system

TEMPLATES_FOLDER = "templates" # constant storing folder name for the given HTML templates. 
DB_TXT_FILE = "db.txt" # constant storing file name ("db.txt") for saving registration info.

# Asynchronuous function that handles each client connection, concurrently that is 
async def handle_connections(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    client_address = writer.get_extra_info("peername") 
    print("Received request from {}".format(client_address))

    # If no message received (empty), close the connection and stop processing.
    if not message:
        writer.close()
        await writer.wait_closed()
        return

    headers = message.split("\r\n")
    request_line = headers[0]
    method_used, path_to_files, _ = request_line.split()

    print("Method: {}, Path: {}".format(method_used, path_to_files))

    # using the GET method in HTTP to render the HTML TEMPLATES_FOLDER files to the page on the webbrowser
    if method_used == "GET":
        if path_to_files == "/": # render the index.html to the home page
            await serve_file_to_browser(writer, "index.html")
        elif path_to_files == "/register": # render the register.html file to the register page on the browser so the client can sign in or sign up 
            await serve_file_to_browser(writer, "register.html")
        else:
            await send_404_status_code(writer) # if the specified path does not exist, send_404_code "NOT FOUND" 

    # handling the form that the user has submitted via the POST request function to "/submit" directory
    elif method_used == 'POST' and path_to_files == "/submit":
        message_body = message.split("\r\n\r\n", 1)[1] # HTTP requests separate headers and body by \r\n\r\n. (putting them in the same column)
        data_to_post = urllib.parse.parse_qs(message_body) # Parse URL-encoded form body into a Python dictionary.
        
        # get the users name and email address upon submittion of the registration form in the web browser
        username = data_to_post.get("username", [""])[0] 
        email_address = data_to_post.get("email", [""])[0]

        # Check if both fields are filled. then write the contents to the "db.txt" file given
        if username and email_address:
            with open(DB_TXT_FILE, "a") as file_to_write_to: # open the file if given (it will close automatically with the "with...as" statement)
                file_to_write_to.write("{} {}\n".format(username, email_address)) # write the contents to the file 

            # After saving the users credentials, redirect back to home using the 303_status_code 
            # The server sends this response to direct the newly registered or signed in user to get the requested resource at another URI with a GET request. In this case the home page 
            redirection_response = ('HTTP/1.1 303 See Other\r\n'
                        'Location: /\r\n\r\n')
            writer.write(redirection_response.encode())
            await writer.drain() #  """Flush the write buffer.
        else:
            await send_400_status_code(writer) # if The server cannot or will not process the request due to something that is perceived to be a client/user error
            await writer.drain() #  """Flush the write buffer.
            
    else:
        await send_405_status_code(writer) # if The request method is known by the server but is not supported by the target resource, in this case this server file 
        await writer.drain() #  """Flush the write buffer.
        
    await writer.drain() #  """Flush the write buffer.
    writer.close() 
    await writer.wait_closed() # Close the connection and wait until it’s fully closed

# an asynchronuos function that Sends the requested HTML file (index or register).
async def serve_file_to_browser(writer, filename):
    
    # Join templates folder and filename to get full path by interacting with the operatig system to get the 2 directories on the system
    file_path = os.path.join(TEMPLATES_FOLDER, filename) 
    try:
        with open(file_path, "r") as file_to_write_to:
            file_content = file_to_write_to.read()
        ok_response = ('HTTP/1.1 200 OK\r\n'
                    'Content-Type: text/html\r\n'
                    'Connection: close\r\n\r\n' +
                    file_content) # read the user's credentials from the "db.txt" file and return an OK status code if successful
        writer.write(ok_response.encode())
        await writer.drain()
    
    except FileNotFoundError:
    #    not_found_response = ('HTTP/1.1 404 Not Found\r\n'
    #                'Content-Type: text/html\r\n'
    #                'Connection: close\r\n\r\n'
    #                '<h1>404 Not Found</h1>') # if the file is not found return an error {404 Not Found}
    #  writer.write(not_found_response.encode())
        await send_404_status_code(writer)
        await writer.drain() # """Flush the write buffer.

# 404 Not Found
# When The server cannot find the requested resource
async def send_404_status_code(writer):
    not_found_response = ('HTTP/1.1 404 Not Found\r\n'
                'Content-Type: text/html\r\n'
                'Connection: close\r\n\r\n'
                '<h1>404 Not Found</h1>')
    writer.write(not_found_response.encode())
    await writer.drain() #  """Flush the write buffer.

# 400 Bad Request
# When The server cannot or will not process the request due to something that is perceived to be a client error 
async def send_400_status_code(writer):
    bad_request_response = ('HTTP/1.1 400 Bad Request\r\n'
                'Content-Type: text/html\r\n'
                'Connection: close\r\n\r\n'
                '<h1>400 Bad Request</h1>')
    writer.write(bad_request_response.encode())
    await writer.drain() #  """Flush the write buffer.

# 405 Method Not Allowed
# When The request method is known by the server but is not supported by the target resource. in this case this server file 
async def send_405_status_code(writer):
    method_not_allowed_response = ('HTTP/1.1 405 Method Not Allowed\r\n'
                'Content-Type: text/html\r\n'
                'Connection: close\r\n\r\n'
                '<h1>405 Method Not Allowed</h1>')
    writer.write(method_not_allowed_response.encode())
    await writer.drain() #  """Flush the write buffer.

# start the asynchronuos server
async def main():
    asyncio_server = await asyncio.start_server(handle_connections, "localhost", 8085) #  """Start a socket server, call back for each client connected.
    print("The Server Is Running on http://localhost:8085")
    
    # the with statement will automatically close the server when it exits hence no neeed for manually calling the "close()" function on the asyncio_server 
    async with asyncio_server: 
        await asyncio_server.serve_forever()

# run the asyncio_server when the "server.py" module is run directly and NOT when it is Imported into others modules 
if __name__ == '__main__':
    asyncio.run(main())
