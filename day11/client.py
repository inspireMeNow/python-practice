import socket
import ssl

host = 'localhost'
port = 8888
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile="cert/cert.pem")
# context.check_hostname=False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=host) as s:
        s.connect((host, port))

        # send data to the server
        s.send(b'Hello, world!')

        # receive data from the server
        data = s.recv(1024)
        print(data.decode())

        # close the connection
        s.close()


