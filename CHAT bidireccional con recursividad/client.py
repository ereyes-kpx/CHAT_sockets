#samuel Esteban Reyes Uribe
#primero debemos importar la libreria de socket

import socket

#definimos la funcion que nos permite manejar mensaje igual que en el server
def man_msg(client_socket):

    message = input("tu: ")
    if message.lower() == 'salir':
        return

    #codificamos el string a utf - 8 para que pase a bytes
    client_socket.send(message.encode('utf-8'))
    # Recibir datos del cliente
    # 1024 es el tamaño dl buffer (bytes)
    data = client_socket.recv(1024)

    #si no hay datos significa que el cliente cerro la conexion 
    if not data:
        return

    # decodifica los byte a string para mostrar el mensaje
    message = data.decode('utf-8')
    print(f"servidor dice: {message}")

    man_msg(client_socket)
#definimos la funcion para iniciar el cliente
def start_client():
#aqui de primeras vamos a definir el host local y el puerto
    host = 'localhost'
    port = 12345


    #creamos el socket (AF_INET es para definir que sea en IPv4 y SOCK_STREAM para definir que es de tipo TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #vamos a tratar de crear una conexion
    try:
        #creamos la conexion
        client_socket.connect((host, port))
        print(f"conectado al servidor {host}:{port}")
        print("Escribe tu mensaje. Escribe 'salir' para salir del programa.")

        man_msg(client_socket)
    #en caso de que no se acepte la conexion
    except ConnectionRefusedError:
        print("no se pudo conectar con el servidor, asegurese que este este en ejecucion")

    #si hay un error lo imprime
    except socket.error as e:
        print(f"Error de socket: {e}")
    
    # cerramos el socket del cliente
    finally:
        client_socket.close()
        print("Conexion cerrada.")

if __name__== "__main__":
    start_client()