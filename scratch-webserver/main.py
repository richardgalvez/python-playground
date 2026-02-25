import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server socket will re-use a local address immediately after the socket is closed rather than wait for the default timeout.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to IP address to tell server where to listen for a request. In this case, listen for all incoming requests from external clients.
server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Web Server Started -- Listening on port {SERVER_PORT}.")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)
    headers = request.split('\n')
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == 'GET':
        if path == '/':
            f_input = open('index.html')
            content = f_input.read()
            f_input.close()

            # Two empty lines are required so it doesn't think we're specifying only the headers.
            response = 'HTTP/1.1 200 OK\n\n' + content

        elif path == '/book':
            f_input = open('book.json')
            content = f_input.read()
            f_input.close()

            response = 'HTTP/1.1 200 OK\n\n' + content

    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\n'

    client_socket.sendall(response.encode())
    client_socket.close()
