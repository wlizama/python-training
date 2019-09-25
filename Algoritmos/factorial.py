
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    num = int(input("Número a calcular: "))
    f = factorial(num)
    print(f"El factorial de {num}! es: {f}")


if __name__ == "__main__":
    main()