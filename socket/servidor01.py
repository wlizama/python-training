import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

mi_socket.bind((local_hostname, 31790))
mi_socket.listen(5)

while True:
    con, adrr = mi_socket.accept()
    print("Conexion establecida {}".format(adrr))

    peticion = con.recv(1024)
    print(str(peticion))

    con.close()
