n1 = int(input())
n2 = int(input())

quant = 0
i = 1

while(i < 50):

    if i % n1 == 0 and i % n2 == 0:

        quant += 1

    i += 1

print(quant)