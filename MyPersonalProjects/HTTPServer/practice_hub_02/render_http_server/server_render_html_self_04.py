import asyncio
from aiohttp import web
import aiofiles
import os

# Ensure the templates directory exists
os.makedirs('templates', exist_ok=True)

async def handle_index(request):
    # Serve the index.html file
    async with aiofiles.open('templates/index.html', mode='r') as f:
        content = await f.read()
    return web.Response(text=content, content_type='text/html')

async def handle_register(request):
    # Serve the register.html file
    async with aiofiles.open('templates/register.html', mode='r') as f:
        content = await f.read()
    return web.Response(text=content, content_type='text/html')

async def handle_submit(request):
    # Handle form submission
    data = await request.post()
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    
    if username and email:
        # Write to db.txt
        async with aiofiles.open('db.txt', mode='a') as f:
            await f.write(f"{username} {email}\n")
        
        # Return a success response (could redirect to index.html in a real app)
        return web.Response(
            text=f"Registration successful! Username: {username}, Email: {email}",
            content_type='text/plain'
        )
    else:
        return web.Response(
            text="Invalid form submission - both username and email are required",
            content_type='text/plain',
            status=400
        )

async def init_app():
    # Create application and setup routes
    app = web.Application()
    app.router.add_get('/', handle_index)
    app.router.add_get('/register', handle_register)
    app.router.add_post('/submit', handle_submit)
    
    # Save the HTML files to templates directory if they don't exist
    if not os.path.exists('templates/index.html'):
        async with aiofiles.open('templates/index.html', mode='w') as f:
            await f.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Home | NET322</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
    }

    .hero {
        background-image: url('../assets/networking_background.jpg');
        background-size: cover;
        background-position: center;
        color: #fff;
        text-align: center;
        padding: 100px 20px;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 20px;
    }

    .hero .btn {
        padding: 10px 20px;
        background-color: #4caf50;
        color: #fff;
        border: none;
        border-radius: 5px;
        font-size: 1.2rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-decoration: none;
    }

    .hero .btn:hover {
        background-color: #45a049;
    }

    .chevron-down {
        margin-top: 20px;
        font-size: 2rem;
        animation: blink 1s infinite;
    }

    @keyframes blink {
        0% {
            opacity: 0.2;
        }
        50% {
            opacity: 1;
        }
        100% {
            opacity: 0.2;
        }
    }
</style>
</head>
<body>

<div class="hero">
    <h1>NET322: Network Programming & Applications Development</h1>
    <a href="#explore" class="btn">Explore</a>
    <i class="fas fa-chevron-down chevron-down"></i>
</div>

<!-- Add more sections/content here -->

</body>
</html>''')

    if not os.path.exists('templates/register.html'):
        async with aiofiles.open('templates/register.html', mode='w') as f:
            await f.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>User Registration | NET322</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .container {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    h2 {
        text-align: center;
    }

    input[type="text"],
    input[type="email"],
    input[type="submit"] {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
    }

    input[type="submit"] {
        background-color: #4caf50;
        color: white;
        cursor: pointer;
    }

    input[type="submit"]:hover {
        background-color: #45a049;
    }
</style>
</head>
<body>

<div class="container">
    <h2>User Registration Form</h2>
    <form action="/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <input type="submit" value="Submit">
    </form>
</div>

</body>
</html>''')

    return app

def main():
    # Configure and start the server
    app = init_app()
    web.run_app(app, port=8085)

if __name__ == '__main__':
    main()