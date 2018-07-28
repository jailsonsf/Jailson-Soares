ano_i, ano_f = map(int, input().split(' '))
cont = 0

for i in range(ano_i,ano_f + 1):

    ano = i
    
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

        print(ano)
        cont += 1


if cont == 0:
    
    print('-1')