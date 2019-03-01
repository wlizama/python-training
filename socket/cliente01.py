import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(local_hostname)

server_address = (ip_address, 31790)
mi_socket.connect(server_address)

print("Conneting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

while True:
    mensaje = input("yo: ")
    mi_socket.sendall(str(mensaje).encode("utf-8"))

mi_socket.close()
