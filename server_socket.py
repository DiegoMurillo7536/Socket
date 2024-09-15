import socket
import random

# Crear un socket de servidor TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la dirección y puerto
server_address = ("localhost", 7537)
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)
print(f"Servidor escuchando en {server_address}")

def guess_number(minimun, maximun, number_to_guess):
    successes_counter = 0
    
    while successes_counter < 3:
        random_number = random.randint(minimun, maximun)
        
        if random_number == number_to_guess:
            print(f"El número {random_number} es el correcto")
            return True
        elif random_number < number_to_guess:
            print(f"El número {random_number} es menor que el número que se quiere adivinar")
            minimun = random_number +1
        elif random_number > number_to_guess:
            print(f"El número {random_number} es mayor que el número que se quiere adivinar")
            maximun = random_number -1
        
        successes_counter += 1
        print(f"Llevas {successes_counter} desacierto(s)")
    
    print(f"Perdiste, el número a adivinar era {number_to_guess}")
    return False

shifts_successes_quantity = 0
shifts_failures_quantity = 0

connection_status = True

while connection_status:
    # Esperar a que un cliente se conecte
    print("Esperando conexión de un cliente...")
    connection, client_address = server_socket.accept()
    
    try:
        print(f"Conexión establecida con: {client_address}")

        # Recibir los datos en fragmentos
        data = connection.recv(1024)
        if data:
            received_message = data.decode()
            print(f"Recibido: {received_message}")

            if received_message == "0,0,0":
                    connection_status = False
                    connection.close()
                    break
            # Separar los números usando el delimitador
            numbers_str = received_message.split(",")
            
            if len(numbers_str) >= 3:
                minimun_number = int(numbers_str[0])
                maximun_number = int(numbers_str[1])
                number_to_guess = int(numbers_str[2])
                print(f"Números recibidos: Min={minimun_number}, Max={maximun_number}, Adivinar={number_to_guess}") 
            
                if guess_number(minimun_number, maximun_number, number_to_guess):
                    shifts_successes_quantity += 1
                else:
                    shifts_failures_quantity += 1
                # Imprimir los contadores
                print(f"La cantidad de turnos exitosos es {shifts_successes_quantity}")
                print(f"La cantidad de turnos fallidos es {shifts_failures_quantity}")
               
            else:
                print("No se recibieron suficientes números.")

            # Responder al cliente
            connection.sendall(b"Mensaje recibido")
               
        else:
            print("No hay más datos del cliente")
   
    finally:
        if received_message == "0,0,0":
        # Cerrar la conexión
            connection.close()
