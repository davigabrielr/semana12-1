def maior_menor(vetor):
    maior = vetor[0]
    menor = vetor[0]
    pos_maior = 0
    pos_menor = 0

    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            pos_maior = i

        if vetor[i] < menor:
            menor = vetor[i]
            pos_menor = i

    print("Maior:", maior, "posição:", pos_maior)
    print("Menor:", menor, "posição:", pos_menor)

producoes = []

for i in range(5):
    producoes.append(int(input("Digite a produção: ")))

maior_menor(producoes)
