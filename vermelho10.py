def procurar(vetor, codigo):
    for valor in vetor:
        if valor == codigo:
            return True
    return False

lotes = []

for i in range(5):
    lotes.append(int(input(f"Código do lote: ")))

codigo = int(input("Digite o código a procurar: "))

if procurar(lotes, codigo):
    print("Encontrado")
else:
    print("Não encontrado")
