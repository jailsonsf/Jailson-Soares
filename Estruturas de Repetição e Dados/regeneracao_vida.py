def enemy_dead(dic, atk, reg):

    hp_init = 100
    tempo = 0
    dano = 0
    aux = 0
    for x in range(atk + 1):

        dano = dic[x][0]
        tempo = dic[x][1] - aux
        aux = tempo

        hp_init -= dano

        if hp_init <= 0:

            return True

        hp_init += tempo * reg

    return False

x = int(input())
resultados = {}
hp = 100
d = t = 0
aux = []
for x in range(x):

    d, t = map(int, input().split(' '))
    aux.append(d)
    aux.append(t)
    resultados[x] = aux
    aux = []

y = int(input())

hp_final = enemy_dead(resultados, x, y)

if hp_final == False:

    print('Inimigo Vivo')

else:

    print('Inimigo Morto')
