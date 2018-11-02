import smtplib


def prompt(prompt):
    return input(prompt).strip()


fromaddr = prompt("From: ")
toaddrs = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break

    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP('localhost')  # mail server ip
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

"""
Simple
"""
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('super.email@receptor.com', 'super.email@emisor.net',
# """To: super.email@emisor.net
# From: super.email@receptor.com

# Super cuerpo del e-mail.
# """)
# server.quit()
#################################


"""
Con cuerpo HTML
"""
import email.message
import smtplib

SUBJECT = "Asuntillo desde Python"
FROM_ADDR = "correo@emisor.net"
FROM_ADDR_PASS = "unacontraseñaquenadiedesifrara"
TO_ADDR = "correo@destino1.com;correo@destino2.com"

body = """Este es el cuerpazo del <b>correo</b>"""

msg = email.message.Message()
msg["Subject"] = SUBJECT
msg["From"] = FROM_ADDR
msg["To"] = TO_ADDR
msg.add_header('Content-Type','text/html')
msg.set_payload(body)


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # mail server ip
server.login(FROM_ADDR, FROM_ADDR_PASS)
server.sendmail(msg["from"],msg["To"].split(";"), msg.as_string())
server.set_debuglevel(1)
server.quit()
