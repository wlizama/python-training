
# def protectegida(paramFunc):

#     def wrapFuncion(password):

#         if password == 'superpassword':
#             return paramFunc()
#         else:
#             print('La contraseña es incorrecta')

#     return wrapFuncion


# @protectegida
# def protected_func():
#     print('Tu contraseña es correcta.')


# if __name__ == '__main__':
#     pwd = str(input('Ingresa tu contraseña: '))

#     protected_func(pwd)


def funcionProtegida(func):

    def action(a, b, veces):
        for i in range(veces):
            a = a * b
            func(i, a)

    return action


@funcionProtegida
def multiply(itera, param):
    print("Iteración {}: {}".format(itera + 1, param))


if __name__ == '__main__':
    print("Multiplicación de n veces de 2 números")
    times = int(input("Veces que debe repetirse la operación: "))
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))

    multiply(num1, num2, times)