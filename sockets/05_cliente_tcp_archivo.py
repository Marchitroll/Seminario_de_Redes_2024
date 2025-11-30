# Cliente TCP receptor de archivos
# Usar junto con: 04_servidor_tcp_archivo.py
# Primero ejecutar el servidor, luego este cliente

import socket
import os

def cliente_recibe_archivo():
    servidor_host = "127.0.0.1"  # Debe coincidir con 04_servidor_tcp_archivo.py
    servidor_puerto = 8080       # Puerto del servidor (debe coincidir con el del servidor)
    
    # Obtener el directorio donde está el script
    directorio_script = os.path.dirname(os.path.abspath(__file__))

    # Crear el socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        cliente_socket.connect((servidor_host, servidor_puerto))
        print(f"Conectado al servidor {servidor_host}:{servidor_puerto}")

        # Nombre del archivo donde se guardará lo recibido (ruta absoluta)
        archivo_guardado = os.path.join(directorio_script, "archivo_recibido.txt")

        # Abrir un archivo en modo escritura binaria para guardar los datos recibidos
        with open(archivo_guardado, "wb") as archivo:
            print(f"Recibiendo archivo desde el servidor y guardándolo como '{archivo_guardado}'...")

            # Recibir datos en bloques de 1024 bytes
            while True:
                datos = cliente_socket.recv(1024)  # Recibir hasta 1024 bytes
                if not datos:  # Si no hay más datos, salir del bucle
                    break
                archivo.write(datos)  # Escribir los datos recibidos exactamente como llegaron

        print(f"Archivo recibido y guardado como '{archivo_guardado}'.")

    except ConnectionError as e:
        print(f"Error de conexión: {e}")

    finally:
        # Cerrar la conexión con el servidor
        cliente_socket.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    cliente_recibe_archivo()
