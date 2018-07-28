tam_A, tam_B = map(int, input().split(' '))
k, m = map(int, input().split(' '))
A = [int(x) for x in input().split(' ')]
B = [int(x) for x in input().split(' ')]

A = sorted(A)
B = sorted(B, reverse = True)

sub_A = []
sub_B = []

menores = 0

for i in range(0,k):

    sub_A.append(A[i])
    
for i in range(0,m):

    sub_B.append(B[i])


for i in sub_A:

    for x in sub_B:
    
        if i < x:
            
            menores += 1


if(menores == (k * m)):

    print('YES')

else:

    print('NO')
