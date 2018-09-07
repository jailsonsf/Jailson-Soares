def euclides(a, d):

    if a > d:

        a, d = d, a
        
    if a % d == 0:
        return d

    return euclides(a, d % a)

n = int(input())

for x in range(n):

    a, d = map(int, input().split())
    print('MDC({},{}) = {}'.format(a, d, euclides(a, d)))
