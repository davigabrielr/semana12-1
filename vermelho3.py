



def inverter(vetor):
    for i in range (len(vetor)-1,-1,-1):
        print(vetor[i])


producao = []



for i in range(5):
    producao.append(float(input("digite a produçao")))




inverter(producao)
