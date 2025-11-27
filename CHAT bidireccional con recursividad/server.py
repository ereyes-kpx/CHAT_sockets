import socket


#definimos una funcion recursiva que administre el uso de mensajes
def man_msg(client_socket):
    # Recibir datos del cliente
    # 1024 es el tamaño dl buffer (bytes)
    data = client_socket.recv(1024)

    #si no hay datos significa que el cliente cerro la conexion 
    if not data:
        return

    # decodifica los byte a string para mostrar el mensaje
    message = data.decode('utf-8')
    print(f"client dice: {message}")

    message = input("tu: ")

    
    #codificamos el string a utf - 8 para que pase a bytes
    client_socket.send(message.encode('utf-8'))
    man_msg(client_socket)

def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        print(f" Server iniciado en {host}:{port}")
    except socket.error as e:
        print(f"Error al vincular el socket: {e}")
        return
    
    #escucha la conexion entrante
    #el parametro 1 es el que nos indica la cantidad maxima de interacciones
    server_socket.listen(1)
    print("esperando conexiones")

    #Aceptar la conexion con el cliente
    # accept() bloquea la ejecucion del codigo hasta que llegue una conexion
    # Retorna un nuevo objeto socket para la conexion y la direccion del cliente
    client_socket, addr = server_socket.accept()
    print(f"Cliente conectado desde {addr}")

    try:
        man_msg(client_socket)
            
    except ConnectionResetError:
        print("la conexion fu forzosamente cerrada por el cliente")
    finally:
        #cerrar la conexion con el cliente y el socket del servidor
        client_socket.close()
        server_socket.close()
        print("servidor cerrado")

if __name__ == "__main__":
    start_server()