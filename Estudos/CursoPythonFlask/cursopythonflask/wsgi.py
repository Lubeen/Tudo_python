"""
Protocolo wsgi espera que voce tenha uma função chamada application
Ela precisa de um callback uma função recebendo outra e chamar uma função que diz que começou a resposta e não para start_response


"""

def application(environ, start_response):
    body = b'<h1>Hello</h1>' 
    status = '200 OK'
    headers = [("Content-Type", "text/html")]
    start_response(status, headers)
    return [body]

#gunicorn wsgi:application
#O flask fala esse protocolo que o wsgi entende

from http.server import BaseHTTPRequestHandler, HTTPServer

class Index(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello</h1>')
    
app = HTTPServer(('localhost', 8000), Index)
app.serve_forever()