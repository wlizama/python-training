from datetime import date, datetime, time
import locale

hoy = date.today()
fecha_nacimiento = date(1993, 6, 4)
dias_desde = hoy - fecha_nacimiento

print("Hoy es {}, han pasado {} dias desde que nací en {}".format(
    hoy, dias_desde, fecha_nacimiento))
# Hoy es 2018-07-16, han pasado 9173 days, 0:00:00 dias desde que nací en 1993-06-04

print("\n")

print("Trabajando con la localización")
locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())
formateado = hoy.strftime("%m-%d-%y. %d %b %Y es %A. hoy es %d de %B.")
print(formateado)
# 07-16-18. 16 jul 2018 es lunes. hoy es 16 de julio.

print("\n")
print("datetime.now()")
print(datetime.now())


print("\n")
print("hh:mm:ss")
print(time.hour, time.minute, time.second)
