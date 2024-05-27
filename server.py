from http import server
import webbrowser
url="http://localhost:8000"


class HTTPServer(server.SimpleHTTPRequestHandler) :
    def end_headers(self):
        self.send_my_headers()
        server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
    
    webbrowser.open(url)

if __name__ == '__main__':
    server.test(HandlerClass=HTTPServer)
    