def soma_media(vetor):
    soma = 0

    for valor in vetor:
        soma += valor

    media = soma / len(vetor)

    print("Soma:", soma)
    print("Média:", media)

colheitas = []

for i in range(5):
    colheitas.append(int(input("Digite uma quantidade: ")))

soma_media(colheitas)
