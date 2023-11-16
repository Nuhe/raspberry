import socket

# Configuración del servidor
host = '10.1.100.235'
port = 22

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Servidor escuchando en {host}:{port}")

# Esperar la conexión del cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida desde {client_address}")

# Recibir datos del cliente y responder
data = client_socket.recv(1024)
print(f"Datos recibidos: {data.decode('utf-8')}")

response = "¡Hola desde el servidor!"
client_socket.send(response.encode('utf-8'))

# Cerrar la conexión
client_socket.close()
server_socket.close()
