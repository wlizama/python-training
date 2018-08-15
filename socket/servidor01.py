import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind(('localhost', 3179))
mi_socket.listen(5)

while True:
    con, adrr = mi_socket.accept()
    print("Conexion establecida")
    print(adrr)

    peticion = con.recv(1024)
    print(repr(peticion))

    # con.send(b"Hola desde Server Socket!!!")
    con.close()
