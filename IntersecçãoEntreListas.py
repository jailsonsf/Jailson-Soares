a = []
b = []
inters = []

for i in range(0,20):

    n = int(input())
    a.append(n)

for i in range(0,20):

    n = int(input())
    b.append(n)

for i in range(0,20):

    for x in b:
    
        if (a[i] == x) and x not in inters:
        
            inters.append(x)

inters = sorted(inters)

if len(inters) == 0:

    print('VAZIO')
    
else:

    for x in inters:

        print(x)
