from random import randint

def cara_koroa(n, d, matriz, diferenca):

    aux = []
    for x in range(n):
        aux1 = randint(0,1)
        aux1 = str(aux1).replace('0', 'C')
        aux1 = aux1.replace('1', 'K')
        aux.append(aux1)

        C = 0
        K = 0
        for x in aux:
            if x == 'C':
                C += 1

            elif x == 'K':
                K += 1

    if aux not in matriz:
        matriz.append(aux)

        dif = abs(C - K)

        if dif == d:
            diferenca += 1

    if len(matriz) == 2 ** n:
        return diferenca

    return cara_koroa(n, d, matriz, diferenca)

n, d = map(int, input().split())
comb = []
diff = 0

print(cara_koroa(n, d, comb, diff))
