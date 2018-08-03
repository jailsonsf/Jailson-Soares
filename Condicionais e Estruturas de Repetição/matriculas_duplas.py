turma_p2 = [i for i in input().split(' ')]
turma_p3 = [i for i in input().split(' ')]
alunos_ambas_disc = []

for x in turma_p2:

    if x in turma_p3:

        alunos_ambas_disc.append(x)

for x in alunos_ambas_disc:

    print('{}'.format(x), end=' ')
