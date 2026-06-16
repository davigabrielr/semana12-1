import random

def mostrar_pares(vetor):
    for valor in vetor:
        if valor % 2 == 0:
            print(valor)

ids = []

for i in range(10):
    ids.append(random.randint(1, 100))

print("Todos os IDs:", ids)
print("IDs pares:")
mostrar_pares(ids)
