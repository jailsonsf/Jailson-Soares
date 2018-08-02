while True:

    n = int(input())

    if n == 0:

        break

    palavra = input()
    tamanho = len(palavra)

    for i in range(tamanho - 1, -1, -1):

        print(palavra[i], end='')
    
    print()