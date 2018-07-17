import smtplib

def prompt(prompt):
  return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
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

server = smtplib.SMTP('localhost') # mail server ip
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()



## Simple #######################
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('super.email@receptor.com', 'super.email@emisor.net',
# """To: super.email@emisor.net
# From: super.email@receptor.com

# Super cuerpo del e-mail.
# """)
# server.quit()
#################################