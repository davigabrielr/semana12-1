def acima_media (vetor):
    media = sum(vetor) / len(vetor)
    print("media: ", media)
    print("produções acima da media")

    for valor in vetor:
        if valor > media:
            print(valor)
producao = []

for i in range(8):
    producao.append(float(input("digite a produção:")))
acima_media(producao)
