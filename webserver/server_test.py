#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server_test.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote_plus  # https://stackoverflow.com/questions/33143504/how-can-i-encode-and-decode-percent-encoded-url-encoded-strings-in-python

_port = 8080

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global _port
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        # print("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        print(f"GET request \n{self.path}")
        self._set_response()
        with open('server_test.html', 'rb') as file: 
            self.wfile.write(file.read()) # Read the file and send the contents 

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #         str(self.path), str(self.headers), post_data.decode('utf-8'))
        print(f"POST request \n{post_data.decode('utf-8')}")
        print(f"({unquote_plus(post_data.decode('utf-8')[:62])})")
        self._set_response()

        payload = unquote_plus(post_data.decode('utf-8')[:62])
        idx = payload.find("=")
        if idx > 0:
            id = payload[:idx]
            val = payload[idx+1:]
        else:
            id = "-"
            val = "/"
        if "script" in payload or "<" in payload:
            id = "h4x"
            val = "lol fk u"

        with open('server_test.html', 'rb') as file: 
            self.wfile.write(file.read()) # Read the file and send the contents 
        self.wfile.write(f"{id} is {val}".encode('utf-8'))
        with open('server_test_pt2.html', 'rb') as file: 
            self.wfile.write(file.read()) # Read the file and send the contents

def run(server_class=HTTPServer, handler_class=S, port=8080):
    global _port
    _port = port
    # logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    # logging.info('Starting httpd...\n')
    print(f'Starting httpd on localhost:{_port}...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    # logging.info('Stopping httpd...\n')
    print('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()