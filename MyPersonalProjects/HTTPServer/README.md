# AsyncIO Concurrent HTTP Server - NET322 Project

## Description

This is a simple Python HTTP server built using AsyncIO.
It can:
- Serve HTML templates (`index.html` and `register.html`) to a web browser
- Handle basic form submission (username and email)
- Save form data into a `db.txt` file

---

## How to Run

1. **Install Python 3** (if not already installed)

2. **Project Structure**
    ```
    /your_project_folder
        ├── server.py
        ├── db.txt          (this will be created automatically)
        └── templates/
              ├── index.html
              └── register.html
    ```

3. **Start the Server**
    ```bash
    python server.py
    ```

4. **Access in Browser**
    - Open your browser and go to [http://localhost:8085/](http://localhost:8085/)
    - Go to [http://localhost:8085/register](http://localhost:8085/register) to register a new user

---

## Features

- Handles **GET** and **POST** requests.
- Serves static HTML templates.
- Captures form submission (username + email) and saves to a text file.
- Asynchronous and can handle multiple clients concurrently.

---

## Notes

- The server listens on `localhost` port `8085`.
- If `db.txt` doesn't exist, it will be created when the first user submits.
- Tested on Python 3.8+.

---

## Author

Patrick  
NET322 Assignment - 2025
