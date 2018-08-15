import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.connect(('localhost', 3179))

mensaje = str(input(":"))

mi_socket.send(bytearray(mensaje))
respuesta = mi_socket.recv(1024)

print(repr(respuesta))
mi_socket.close()
