n = int(input())
lista = [int(x) for x in input().split(' ')]

for x in range(n - 1, -1, -1):

    print(lista[x], end=' ')

print()

cont = 0
deslocamento = 1
while x < n:

    i = deslocamento % n
    print(lista[i],end=' ')

    x += 1
    deslocamento += 1

print()

d_lista = sorted(lista, reverse = True)

for x in d_lista:

    print(x, end=' ')

print()