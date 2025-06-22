from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Welcome to the Home Page! i have edited the code now ')
        elif self.path == '/health':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Server is Healthy!')
        else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'404 Not Found')

# Define server address and port
server_address = ('0.0.0.0', 8000)  # '' means localhost
httpd = HTTPServer(server_address, SimpleHandler)
print("Server running on http://localhost:8000")
httpd.serve_forever()
