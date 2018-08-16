def fibonacci(num):
    a, b = 0, 1

    while a < num:
        print(a, end=" ")
        a, b = b, a + b

    print()


if __name__ == '__main__':
    numero = int(input("Ingresar número para calcular serie Fibonacci: "))
    fibonacci(numero)
