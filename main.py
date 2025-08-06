produtos = {}
total = 0
cod = 0
def cadastrar():
    while True:
        global cod
        cod = int(input("Codigo:"))
        nome= input("Nome:")
        quant = int(input("Quantidade:"))
        valor = float(input("Valor:"))
        prod = []
        prod.append(nome)
        prod.append(quant)
        prod.append(valor)
        produtos[cod] = prod
        resposta_2 =input("Voce gostaria de sair?[S][N]")
        if resposta_2.upper() == "S":
            print("Saindo...")
            break

def verificar_produtos():
    print("Itens cadastrados:")
    print(60*"-")
    for chave, valor in produtos.items():
        print(f"Código: {chave}, Nome: {valor[0]}, Quantidade: {valor[1]}, Valor: {valor[2]}")
    print(60*"-")

def remover_estoque():
    if cod in produtos[cod]:
        produtos.popitem(cod)
while True:
    print(" 1.Cadastrar Produtos\n",
            "2.Verificar produtos\n",
            "3.Remover produto\n",
            "4.Sair")
    resposta = int(input(""))

    if resposta ==1:
        cadastrar()
    if resposta == 2:
        if cod in produtos:
            verificar_produtos()
        elif cod not in produtos:
            print("Não possui produtos registrados!")
    if resposta == 3:
        cod_remover = int(input("Qual item voce deseja remover? [Codigo]"))
        if cod_remover in produtos:
            produtos.pop(cod_remover)
    if resposta == 4:
        print("Saindo...")
        break
