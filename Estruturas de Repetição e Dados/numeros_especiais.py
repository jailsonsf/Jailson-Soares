def especial_num(lista, l, r):

    aux = []
    for x in range(l - 1, r):

        aux.append(lista[x])

    cont = 0
    for x in aux:

        if x < 10 and x >= 0:

            cont += 1

        elif x >= 10:

            aux = str(x)

            if aux[0] == aux[-1]:

                cont += 1

    return cont

def troca_item(lista, i, k):

    for x in range(len(lista)):

        if lista[x] == i:

            lista[x] = k

    return lista

n, q = map(int, input().split(' '))
numeros = [int(x) for x in input().split(' ')]

operacao = 0
item1 = 0
item2 = 0
for x in range(q):

    operacao, item1, item2 = map(int, input().split(' '))

    if operacao == 1:

        print(especial_num(numeros, item1, item2))

    elif operacao == 2:

        numeros = troca_item(numeros, item1, item2)
