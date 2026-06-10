def soma_fazendas(a, b):
    c = []

  
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

fazendaA = []
fazendaB = []

for i in range(5):
    fazendaA.append(int(input("Fazenda A posição: ")))
for i in range(5):
    fazendaB.append(int(input("Fazenda B posição: ")))
    
resultado = soma_fazendas(fazendaA, fazendaB)



print("Array soma:", resultado)
