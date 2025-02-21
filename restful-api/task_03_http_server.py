from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        if self.path == "/":
            response = {"message": "Hello, this is a simple API!"}
        elif self.path == "/data":
            response = {"name": "John", "age": 30, "city": "New York"}
        elif self.path == "/status":
            response = {"status": "OK"}
        elif self.path == "/info":
            response = {"version": "1.0", "description": "A simple API built with http.server"}
        else:
            self.send_response(404) 
            response = {"error": "Endpoint not found"}

        self.wfile.write(json.dumps(response).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()