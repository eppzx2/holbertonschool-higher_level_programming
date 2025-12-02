#!/usr/bin/python3
"""
setting up a http server(hinthunter ;))
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """custom HTTP request handler"""

    def do_GET(self):
        """handle GET requests"""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            response = json.dumps(info).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(message.encode("utf-8"))
            return


def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
