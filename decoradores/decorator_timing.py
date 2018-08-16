import time


def timing_function(some_function):
    """
    Resultados el tiempo que tarda una función ejecutar.
    """
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Tiempo que tardó en ejecutar la función: %s" % str((t2 - t1))

    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 100000)):
        num_list.append(num)

    print("La suma de los números es:" + str(sum(num_list)))


print(my_function())
