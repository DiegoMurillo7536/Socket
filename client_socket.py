import socket

# Crear un socket de cliente TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
server_address = ("localhost", 7536)
client_socket.connect(server_address)

try:
    # Enviar números
    minimun_number = int(input("Ingrese el número mínimo:n"))
    maximun_number = int(input("Ingrese el número máximo: "))
    number_to_guess = int(input("Ingrese el número a adivinar: "))
    numbers = f"{minimun_number},{maximun_number},{number_to_guess}"
    client_socket.sendall(numbers.encode())
    # Esperar respuesta
    data = client_socket.recv(1024)
    print(f"Recibido del servidor: {data.decode()}")

finally:
    # Cerrar el socket
    client_socket.close()
