import socket

def start_server():
    # Configurar el host y el puerto
    # 'localhost' significa que el servidor se ejecutará en la misma máquina
    host = 'localhost'
    port = 12345

    # Crear un objeto socket
    # AF_INET indica que usaremos IPv4
    # SOCK_STREAM indica que usaremos TCP (protocolo orientado a conexión)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular el socket al host y puerto especificados
    try:
        server_socket.bind((host, port))
        print(f"Servidor iniciado en {host}:{port}")
    except socket.error as e:
        print(f"Error al vincular el socket: {e}")
        return

    # Escuchar conexiones entrantes
    # El parámetro 1 indica el número máximo de conexiones en cola
    server_socket.listen(1)
    print("Esperando conexiones...")

    # Aceptar la conexión del cliente
    # accept() bloquea la ejecución hasta que llega una conexión
    # Retorna un nuevo objeto socket para la conexión y la dirección del cliente
    client_socket, addr = server_socket.accept()
    print(f"Conexión establecida con: {addr}")

    try:
        while True:
            # Recibir datos del cliente
            # 1024 es el tamaño del buffer (bytes)
            data = client_socket.recv(1024)
            
            # Si no hay datos, significa que el cliente cerró la conexión
            if not data:
                break
            
            # Decodificar los bytes a string y mostrar el mensaje
            message = data.decode('utf-8')
            print(f"Cliente dice: {message}")
            
    except ConnectionResetError:
        print("La conexión fue cerrada forzosamente por el cliente.")
    finally:
        # Cerrar la conexión con el cliente y el socket del servidor
        client_socket.close()
        server_socket.close()
        print("Servidor cerrado.")

if __name__ == "__main__":
    start_server()
