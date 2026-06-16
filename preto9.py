
import random

def contar_pares_impares(vetor):
    pares = 0
    impares = 0

    for valor in vetor:
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Pares:", pares)
    print("Ímpares:", impares)

ids = []

for i in range(10):
    ids.append(random.randint(1, 50))

print(ids)
contar_pares_impares(ids)
