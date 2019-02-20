"""
Repositorio    https://github.com/dbader/schedule
Documentación  https://schedule.readthedocs.io/en/stable
"""

import schedule
import time


def tarea(msg):
    print("Ejecutando tarea", msg, time.time())


def pollTareas():
    schedule.every(5).seconds.do(tarea, "cada 5 segundos")
    schedule.every(10).seconds.do(tarea, "cada 10 segundos")
    schedule.every().wednesday.at("12:45").do(tarea, "cada miércoles a las 12:45 am")
    schedule.every().day.at("12:50").do(tarea, "cada día a las 12:50")

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    pollTareas()