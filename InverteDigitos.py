n = int(input())
nd = len(str(n))
aux = n
invertido = cont = 0

while(nd >= 1):

    nd -= 1
    pow = 10**nd
    v = int(n/pow)
    invertido += v*(10**cont)
    n = n % pow
    cont += 1

n = str(aux)
invertido = str(invertido)
dif = 0

if len(n) > len(invertido):

    dif = len(n) - len(invertido)

if dif == 0:

    print(invertido)

elif dif > 0:

    invertido = '0' * dif + invertido
    print(invertido)
