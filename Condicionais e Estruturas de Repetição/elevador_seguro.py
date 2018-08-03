peso = -1
quant_pessoas = peso_total = 0

while peso != 0 and quant_pessoas < 7 and peso_total < 560:

    peso = int(input())
    quant_pessoas += 1
    peso_total += peso

if quant_pessoas < 7 and peso == 0:

    quant_pessoas -= 1

if peso_total > 560:

    peso_total -= peso
    quant_pessoas -= 1

print(quant_pessoas)
print('{:.1f}'.format(peso_total))
