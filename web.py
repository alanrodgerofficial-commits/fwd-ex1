from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
```html
<!DOCTYPE html>
<html>
<head>
    <title>Network Protocols</title>
</head>
<body>
    <h1>Network Protocols</h1>

    <p>HTTP - Hypertext Transfer Protocol</p>
    <p>HTTPS - Hypertext Transfer Protocol Secure</p>
    <p>FTP - File Transfer Protocol</p>
    <p>TCP - Transmission Control Protocol</p>
    <p>IP - Internet Protocol</p>
    <p>DNS - Domain Name System</p>
    <p>SMTP - Simple Mail Transfer Protocol</p>
    <p>SSH - Secure Shell</p>
</body>
</html>
```
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()