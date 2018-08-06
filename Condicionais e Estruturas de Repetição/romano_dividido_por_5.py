num_romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

n_r = []

n = input().upper()

for x in n:

    n_r.append(num_romanos[x])

tam = len(n)
i = 0
valor = aux = n_r[i]
cont = 1

for x in range(1,tam):

    if n_r[x] == aux and x - i < 3 and cont < 3:

        valor += int(n_r[x])
        cont += 1

    elif n_r[x] > aux:

        valor += int(n_r[x]) - int(aux)

    elif n_r[x] < aux:

        valor += int(aux) + int(n_r[x])

    i += 1
    aux = n_r[i]

if tam == 1:

    valor = int(n_r[0])

resto = valor % 5

if resto == 0:

    print('O numero e multiplo de 5!')

else:
    
    print('O resto pela divisao por 5 do numero dado e igual a {}!'.format(resto))