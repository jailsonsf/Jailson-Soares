def pares(n, aux):
    
    if aux == n - 1:
        return aux

    if aux % 2 == 0:
        print(aux)

        if aux < n - 2:
            return pares(n, aux + 2)

        

        elif aux == n - 2:
            return n
            

n = int(input())
print(pares(n, 0))
