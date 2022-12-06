import logging
import http.server
import socketserver
import getpass

class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message (self, format, *args):
        logging.info("%s - - [%s] %s\n"% (
            self.client_adress[0],
            self.log_date_time_string(),
    )
    )

logging.basicConfig(
    filename='/log/http-server.log',
    format= '%(asctime)s - %(lavelname)s - %(message)s,
    level=logging.INFO
    )

logging.getLogger().addHandler(logging.StreamHandler())
logging.info('inicializando...')
PORT = 8000

httpd = socketserver.TCPServer(("", PORT), MyHTTPHandler)
logging.info("executando a porta: %s", PORT)
logging.info("usuário: %s", getpass.getuser())
httpd.server_forever()