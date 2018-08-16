import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

mi_socket.connect((local_hostname, 31790))

mensaje = input("yo: ")

mi_socket.send(str(mensaje).encode("utf-8"))

mi_socket.close()
