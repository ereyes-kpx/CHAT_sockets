import socket

def start_client():
    # Configurar el host y el puerto del servidor al que nos conectaremos
    host = 'localhost'
    port = 12345

    # Crear un objeto socket
    # AF_INET para IPv4, SOCK_STREAM para TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        client_socket.connect((host, port))
        print(f"Conectado al servidor en {host}:{port}")
        print("Escribe tus mensajes. Escribe 'salir' para terminar.")

        while True:
            # Obtener entrada del usuario
            message = input("Tú: ")

            if message.lower() == 'salir':
                break

            # Enviar el mensaje al servidor
            # Es necesario codificar el string a bytes antes de enviar
            client_socket.send(message.encode('utf-8'))

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que esté ejecutándose.")
    except socket.error as e:
        print(f"Error de socket: {e}")
    finally:
        # Cerrar el socket del cliente
        client_socket.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    start_client()
