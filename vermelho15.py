



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

#acho que vou desistir

    for valor in lotes:
        if valor > x:
            cont += 1

    print("Quantidade:", cont)
 def verificar(lotes):
    codigo = int(input("Código para procurar: "))

    if codigo in lotes:
        print("Presente")
    else:
        print("Não presente")

def maior_menor(lotes):
    if len(lotes) == 0:
        print("Lista vazia")
    else:
        print("Maior:", max(lotes))
        print("Menor:", min(lotes))

lotes = []

while True:
    print("\n1-Inserir")
    print("2-Listar")
    print("3-Retirar")
    print("4-Limpar")
    print("5-Contar maiores que X")
    print("6-Verificar código")
    print("7-Maior e menor")
    print("8-Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        inserir(lotes)
    elif opcao == 2:
        listar(lotes)
    elif opcao == 3:
        retirar(lotes)
    elif opcao == 4:
        limpar(lotes)
    elif opcao == 5:
        contar_maior(lotes)
    elif opcao == 6:
        verificar(lotes)
    elif opcao == 7:
        maior_menor(lotes)
    elif opcao == 8:
        break
    else:
        print("Opção inválida")
