



#ai é loucura kkk

def inserir(lotes):


    codigo = int(input("Digite um código par: "))

    if codigo % 2 == 0:
        lotes.append(codigo)
    else:
        print("Erro! Apenas códigos pares.")

def listar(lotes):
    print(lotes)

def retirar(lotes):
    codigo = int(input("Código para retirar: "))

    if codigo in lotes:
        lotes.remove(codigo)
    else:
        print("Código não encontrado.")

def limpar(lotes):
    lotes.clear()

def contar_maior(lotes):
    x = int(input("Digite X: "))
    cont = 0

#acho que vou desistir e terminar em casa :(

    for valor in lotes:
        if valor > x:
            cont += 1

    print("Quantidade:", cont)

