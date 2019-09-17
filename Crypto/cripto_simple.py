from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

inp = input("Ingrese texto a encriptar:")

inp_encript = f.encrypt(inp.encode("UTF-8"))

print("Mensaje encriptado:\n%s" % inp_encript)