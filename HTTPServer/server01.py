from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hola desde HTTP Server !")
        return


try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Iniciado httpserver en puerto ', PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
