def binario(n, bin):

    if n == 0:
        return bin

    bin.append(n % 2)

    if n != 0:
        return binario(n // 2, bin)

lista = []

n = int(input())

if n == 0:

    print(n)

else:
    
    num_binario = binario(n, lista)

    for x in range(len(num_binario) - 1, -1, -1):

        print(num_binario[x])