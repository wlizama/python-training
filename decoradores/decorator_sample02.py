"""
 Decorador con parametros
"""


def sum_decorator(exec_func_before=True):
    def fun_decorator(func):
        def before_func():
            print("Ejecutando acciones ANTES de llamar a función")

        def after_func():
            print("Ejecutando acciones DESPUES de llamar a función")

        def wrapper(*args, **kwargs):
            if exec_func_before:
                before_func()
            func(*args, **kwargs)
            after_func()

        return wrapper

    return fun_decorator


@sum_decorator(exec_func_before=False)
def suma_simple(num1, num2):
    print("Suma simple: {}".format(num1 + num2))


suma_simple(35, 80)
