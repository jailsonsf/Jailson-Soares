romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

n = list(str(input().upper()))
tam = len(n)
valor = 0

for x in range(tam - 1):

    if n[x] != '0':

        if romanos[n[x]] < romanos[n[x + 1]]:

            valor += romanos[n[x + 1]] - romanos[n[x]]

        else:

            valor += romanos[n[x]] + romanos[n[x + 1]]
        
        n[x + 1] = '0'

    elif x + 2 == tam:

        valor += romanos[n[x + 1]]

if tam == 1:

    valor = romanos[n[0]]

if valor % 5 == 0:

    print('O numero e multiplo de 5!')

else:
    
    print('O resto pela divisao por 5 do numero dado e igual a {}!'.format(valor % 5))