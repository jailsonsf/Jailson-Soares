def quant_caminhoes(l_pesos, l_tipo):

    caminhoes_N = 0
    caminhoes_E =  0
    caminhoes1 = 0
    caminhoes2 = 0
    tipo = -1
    for x in range(len(l_pesos)):

        tipo = l_tipo[x]

        if tipo == 0:

            caminhoes_N += l_pesos[x]

        elif tipo == 1:

            caminhoes_E += l_pesos[x]

    caminhoes1 += caminhoes_N // 10

    if caminhoes_N % 10 > 0:

        caminhoes1 += 1

    caminhoes2 += caminhoes_E // 5

    if caminhoes_E % 5 > 0:

        caminhoes2 += 1

    caminhoes = [caminhoes1 + caminhoes2, caminhoes1, caminhoes2]

    return caminhoes

def preco(ca_E, ca_N):

    preco = (ca_E * 1200) + (ca_N * 500)
    return preco

def dias_gastos(dist, tip):

    aux = dist[0]
    pos = 0
    for x in range(1, len(dist)):

        if dist[x] > aux:

            aux = dist[x]
            pos = x

    opcao_entrega = tip[pos]

    dias = 0
    if opcao_entrega == 0:

        dias = aux // 100

        if aux % 100 > 0:

            dias += 1

    elif opcao_entrega == 1:

        dias = aux // 250

        if aux % 250 > 0:

            dias += 1

    return dias

n = int(input())
pesos = []
tipo_entrega = []
distancias = []
peso = tipo = distancia = 0

for x in range(n):

    peso = int(input())
    tipo = int(input())
    distancia = int(input())

    pesos.append(peso)
    tipo_entrega.append(tipo)
    distancias.append(distancia)

t_caminhoes = quant_caminhoes(pesos, tipo_entrega)
caminhoes_e = t_caminhoes[2]
caminhoes_n = t_caminhoes[1]
caminhoes = t_caminhoes[0]
total_preco = preco(caminhoes_e, caminhoes_n)
total_dias = dias_gastos(distancias, tipo_entrega)

print('{} {} {}'.format(caminhoes, total_preco, total_dias))
