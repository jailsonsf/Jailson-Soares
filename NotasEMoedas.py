valor = float(input())

valores = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]

quantia = []

divisao = 0

for x in valores:

    divisao = int(valor / x)
    valor = round(valor % x, 2)
    quantia.append(divisao)

print('NOTAS:')

for i in range(0, int(len(valores)/2)):

    print('{} nota(s) de R$ {:.2f}'.format(quantia[i],valores[i]))

print('MOEDAS:')

for i in range(int(len(valores)/2), len(valores)):

    print('{} moeda(s) de R$ {:.2f}'.format(quantia[i],valores[i]))
print()