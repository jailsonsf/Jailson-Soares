n = int(input())

a = 1
b = 2
c = 3

while True:

    if a * b * c == n:

        print('{} * {} * {} = {}'.format(a,b,c,n))
        print('Verdadeiro')
        break

    elif a * b * c > n:

        print('Falso')
        break

    else:

        a += 1
        b += 1
        c += 1