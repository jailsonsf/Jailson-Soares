def eh_primo(x):

    aux = []
    for c in range(1, x + 1):

        if x % c == 0:

            aux.append(c)

    if len(aux) == 2 and aux[0] == 1 and aux[1] == x:

        return 1

def campeao(lista):

    aux = []
    for x in lista:

        if x not in aux:

            aux.append(x)

    total = 0
    camp = 0
    empate = False
    for x in aux:

        if lista.count(x) > total:

            total = lista.count(x)
            camp = x
            empate = False

        elif lista.count(x) == total:

            empate = True

    if empate == False and camp > 0:

        return camp

    elif  empate == True or camp <= 0:

        return -1

l, u = map(int, input().split(' '))

primos = []
saltos = []
for x in range(l, u + 1):

    if eh_primo(x) == 1:

        primos.append(x)

for x in range(len(primos) - 1):

    salto = primos[x + 1] - primos[x]
    saltos.append(salto)

resultado = campeao(saltos)

print(resultado)