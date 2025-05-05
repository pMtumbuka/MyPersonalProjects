import urllib.request
import urllib.parse

url = "http://localhost:8090"
data = {
    "name": "Patrick",
    "message": "Hello from the client!"
}

# Encode data to application/x-www-form-urlencoded
encoded_data = urllib.parse.urlencode(data).encode("utf-8")

req = urllib.request.Request(url, data=encoded_data, method="POST")
req.add_header("Content-Type", "application/x-www-form-urlencoded")

with urllib.request.urlopen(req) as response:
    response_text = response.read().decode()
    print("Server response:\n", response_text)
