def verificar_distintos(vetor):
    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            if vetor[i] == vetor[j]:
                print("Há duplicatas")
                return

    print("Distintos")

codigos = []

for i in range(5):
    codigos.append(int(input("Código: ")))

verificar_distintos(codigos)
