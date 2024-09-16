import socket
from utils import Utils

# Crear un socket de servidor TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la dirección y puerto
server_address = ("localhost", 7536)
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)
print(f"Servidor escuchando en {server_address}")


shifts_successes_quantity = 0
shifts_failures_quantity = 0

while True:
    # Esperar a que un cliente se conecte
    print("Esperando conexión de un cliente...")
    connection, client_address = server_socket.accept()
    print(f"Conexión establecida con: {client_address}")

    # Recibir los datos en fragmentos
    data = connection.recv(1024)
    if data:
        received_message = data.decode()
        print(f"Recibido: {received_message}")

        if received_message == "0,0,0":
            connection.send(b"Adios!")
            connection.close()
            break
        # Separar los números usando el delimitador
        numbers_str = received_message.split(",")

        if len(numbers_str) >= 3:
            minimun_number = int(numbers_str[0])
            maximun_number = int(numbers_str[1])
            number_to_guess = int(numbers_str[2])
            print(
                f"Números recibidos: Mínimo={minimun_number}, Máximo={maximun_number}, Adivinar={number_to_guess}"
            )

            if Utils.guess_number(minimun_number, maximun_number, number_to_guess):
                shifts_successes_quantity += 1
            else:
                shifts_failures_quantity += 1

            # Imprimir los contadores en el servidor
            print(f"La cantidad de turnos exitosos es {shifts_successes_quantity}")
            print(f"La cantidad de turnos fallidos es {shifts_failures_quantity}")

            # Responder al cliente
            message_to_send_to_client = f"Mensaje recibido. Intentos con exito: {shifts_successes_quantity},intentos fallidos:{shifts_failures_quantity}"
            connection.sendall(message_to_send_to_client.encode())