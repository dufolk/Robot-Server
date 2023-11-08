from src.services import ServerService
import socketserver

if __name__ == '__main__':
    host = 'localhost'
    port = 9999
    server = socketserver.ThreadingTCPServer((host, port), ServerService)
    print('server started')
    server.serve_forever()