from time import sleep


def sleep_decorator(function):
    """
    Limita qué tan rápido es el llamado a una funcion.
    """
    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)

    return wrapper


@sleep_decorator
def print_number(num):
    return num


print(print_number(123))

for num in range(1, 6):
    print(print_number(num))
