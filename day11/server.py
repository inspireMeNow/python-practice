import socket
import ssl

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile='cert/cert.pem', keyfile='cert/key.pem')
    server_socket = ssl_context.wrap_socket(server_socket, server_side=True)
    server_socket.bind(('127.0.0.1', 8888))

    server_socket.listen(10)

    while True:
        ssl_client_socket, address = server_socket.accept()
        data = ssl_client_socket.recv(1024)
        print("Client 's Message: ", str(address), data.decode())

        response = "Received!"
        ssl_client_socket.send(response.encode())

except KeyboardInterrupt:
    ssl_client_socket.close()
    server_socket.close()
    ssl_client_socket.shutdown()
    server_socket.shutdown()
