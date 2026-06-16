import random

def gerar_pragas():
    pragas = []

    while len(pragas) < 5:
        num = random.randint(1, 100)

        if num not in pragas:
            pragas.append(num)

    return pragas

def confronto(equipe, pragas):
    protegidos = 0
    perdidos = 0

    print("Equipe:", equipe)
    print("Pragas:", pragas)

    for i in range(5):
        if equipe[i] > pragas[i]:
            print("Lote", i + 1, "- Protegido")
            protegidos += 1
        else:
            print("Lote", i + 1, "- Perdido")
            perdidos += 1

    print("Placar final:", protegidos, "x", perdidos)

equipe = []

for i in range(5):
    equipe.append(int(input("Força da equipe: ")))

pragas = gerar_pragas()

confronto(equipe, pragas)
