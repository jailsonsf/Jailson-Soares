def soma_r(n):

    raiz_n = int(n ** 0.5)
    cont = 0

    for cont in range(2, raiz_n):

        if n % cont == 0:

            return cont + soma_r(int(n / cont))

    return n

n = int(input())

while n > 0:

    soma = soma_r(n)

    print(soma)

    n = int(input())
