parar = False

lista_velocidade = []
lista_ano = []
cont = 0

while(parar != True):

    continua = input().lower()

    if continua == 's':

        ano = int(input())
        velocidade = float(input())
        
        lista_ano.append(ano)
        lista_velocidade.append(velocidade)
        
        cont = 1

    elif continua == 'n':

        parar = True

if cont == 1:

    print('{:.2f}\n{}'.format(max(lista_velocidade),max(lista_ano)))
    print('{:.2f}'.format(sum(lista_velocidade)/len(lista_velocidade)))

elif cont == 0:

    print('zero')
