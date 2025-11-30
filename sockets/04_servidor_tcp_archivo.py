import socket
import os

def servidor_envia_archivo():
    host = "127.0.0.1"  # Escucha solo en localhost (más seguro para desarrollo)
    puerto = 8080        # Puerto donde el servidor escuchará las conexiones
    
    # Obtener el directorio donde está el script
    directorio_script = os.path.dirname(os.path.abspath(__file__))

    # Crear el socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permitir reutilizar el puerto inmediatamente después de cerrar el servidor
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Asociar el socket al host y puerto
        servidor_socket.bind((host, puerto))
        print(f"Servidor iniciado en {host}:{puerto}")

        # Escuchar conexiones entrantes
        servidor_socket.listen(1)
        print("Esperando conexiones...")

        # Aceptar la conexión de un cliente
        conexion, direccion_cliente = servidor_socket.accept()

        # Mostrar en consola la IP y el puerto del cliente
        print(f"Cliente conectado desde {direccion_cliente[0]}:{direccion_cliente[1]}")

        # Nombre del archivo que se enviará (ruta absoluta)
        archivo_nombre = os.path.join(directorio_script, "archivo_enviado.txt")

        # Abrir el archivo y escribir en él antes de enviarlo (con encoding UTF-8)
        with open(archivo_nombre, "w", encoding="utf-8") as archivo:
            archivo.write(f"Conexion establecida con el cliente: {direccion_cliente[0]}:{direccion_cliente[1]}\n")
            archivo.write("Este archivo fue preparado por el servidor.\n")
            extra = input("Ingrese un mensaje extra: ")
            archivo.write(extra)

        # Enviar el archivo al cliente
        with open(archivo_nombre, "rb") as archivo:
            archivo_data = archivo.read(2048)    # Leer el primer bloque de hasta 2048 bytes

            # Bucle para enviar todo el archivo al cliente en bloques
            while archivo_data:  # Mientras haya datos en el archivo
                conexion.sendall(archivo_data)  # Enviar el bloque leído al cliente
                archivo_data = archivo.read(2048)  # Leer el siguiente bloque de hasta 2048 bytes

        print(f"Archivo enviado y registrado en {archivo_nombre}.")

        # Cerrar la conexión
        conexion.close()
        print(f"Conexión cerrada con {direccion_cliente[0]}:{direccion_cliente[1]}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        servidor_socket.close()
        print("Servidor cerrado.")

if __name__ == "__main__":
    servidor_envia_archivo()
