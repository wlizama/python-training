import socket

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(local_hostname)

print("Working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

server_address = (ip_address, 31790)
print("Starting up on %s port %s" % server_address)
mi_socket.bind(server_address)

mi_socket.listen(2)

while True:
    print("waiting for a connection")

    con, adrr = mi_socket.accept()

    try:
        print("Connection from", adrr)
        while True:
            data = con.recv(64)
            if data:
                print("data: %s" % data)
            else:
                print("No more data")
                break
    finally:
        con.close()

