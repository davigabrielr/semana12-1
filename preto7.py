def calcular_azeite(lotes, rendimento):
    for i in range(len(lotes)):
        litros = lotes[i] * rendimento
        print("Lote", i + 1, "=", litros, "litros")

lotes = []

for i in range(6):
    lotes.append(float(input("Kg do lote: ")))

calcular_azeite(lotes, 0.18)
