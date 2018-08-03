lista_num = [int(x) for x in input().split(' ')]

soma = cont = 0

for x in lista_num:

    if x > 0 and x % 2 == 0:

        soma += x
        cont += 1

if soma == 0:

    print('-1')

else:

    print('{:.2f}'.format(soma / cont))