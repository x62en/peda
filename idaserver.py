

import SocketServer,threading
import idc, idaapi

lock = threading.RLock()

SocketServer.ThreadingTCPServer.allow_reuse_address = True

class Handler(SocketServer.BaseRequestHandler):
    def handle(self):
        with lock:
            data = self.request.recv(1024)
            # print '[+] %s' % data
            try: self.request.sendall(repr(eval(data)))
            except SyntaxError: pass

server = SocketServer.TCPServer(('127.0.0.1', 31337), Handler)

thread = threading.Thread(target=server.serve_forever)
thread.daemon = True
thread.start()
