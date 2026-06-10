

def calcular_valor(kg, preco):
    valor = []

  
    for i in range(len(kg))::
        valor.append(kg[i] * preco[i])

    return valor

kg_colhidos = []
preco_por_kg = []

for i in range(5):
    kg_colhidos.append(float(input(f"Kg da árvore: ")))


for i in range(5):
    preco_por_kg.append(float(input(f"Preço por kg da árvore: ")))

resultado = calcular_valor(kg_colhidos, preco_por_kg)

print("Valor obtido por árvore:")
print(resultado)
