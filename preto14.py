def existe(vetor, valor):
    for item in vetor:
        if item == valor:
            return True
    return False

rfid = []

while len(rfid) < 15:
    codigo = int(input("Digite o código: "))

    if existe(rfid, codigo):
        print("Código repetido. Digite outro.")
    else:
        rfid.append(codigo)

print(rfid)
