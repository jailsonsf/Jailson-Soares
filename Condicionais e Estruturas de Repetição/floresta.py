n_total = int(input())
quant = 0
limite = int((2 + (8 * n_total - 4)**0.5) / 4)

for x in range(2, limite + 1):

    if ((n_total - 1 + x) % (2 * x - 1)) == 0:
        
        quant += 1

print(quant)