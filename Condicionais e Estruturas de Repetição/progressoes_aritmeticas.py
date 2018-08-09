tam = int(input())
lista_n = [int(x) for x in input().split(' ')]
PAs = {}
aux = aux_2 = []
r = lista_n[1] - lista_n[0]

x = 0
for i in range(tam - 1):

    if lista_n[i + 1] - lista_n[i] != r:

        r = lista_n[i + 1] - lista_n[i]
        aux_2 = aux
        aux = []
        x += 1

    if lista_n[i + 1] - lista_n[i] == r:

        if lista_n[i] not in aux_2:

            aux.append(lista_n[i])
        
            if i == tam - 2 or lista_n[i + 1] - lista_n[i] == r and lista_n[i + 2] - lista_n[i + 1] != r:

                aux.append(lista_n[i + 1])

    PAs[x] = aux

    if PAs[x] == []:

        del PAs[x]
        
print(len(PAs))