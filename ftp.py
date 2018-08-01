"""
	Conección a servidor FTP
	https://docs.python.org/3.7/library/ftplib.html
"""

from ftplib import FTP

# ftp://ftp.mx.debian.org
ftp = FTP("ftp.mx.debian.org") # conectarse al host, puerto predeterminado 

ftp.login()                    # "anonymous", "anonymous@"
ftp.cwd('debian')              # cambiar de directorio
print("## El directorio actual: {}".format(ftp.pwd()))

print("## Contiene los archivos: ")
ftp.retrlines('LIST')          # listar direcctorio

# Recuperar un archivo en modo de transferencia binaria.
# ftp.retrbinary('RETR README', open('README', 'wb').write)

archivo = "README.html"
tam = ftp.size(archivo)/1024

print("\n## El tamaño de: {} es {}kb".format(archivo, tam))

ftp.quit()