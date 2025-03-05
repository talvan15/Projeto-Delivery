from model.cliente import Cliente
from model.entregador import Entregador
from model.pedido import Pedido
from model.produto import ItemCardapio

def cadastrar_produtos():
    produtos = []
    produtos.append(Produto("Pizza", 40.00, "Pizza de queijo e pepperoni"))
    produtos.append(Produto("Refrigerante", 5.00, "Refrigerante de cola 350ml"))
    produtos.append(Produto("Sobremesa", 10.00, "Torta de chocolate"))
    return produtos

def main():
    # Informações do cliente
    print("\nPor favor, insira os dados do cliente:")
    nome_cliente = input("Nome: ")
    endereco_cliente = input("Endereço: ")
    telefone_cliente = input("Telefone: ")
    cliente = Cliente(nome_cliente, endereco_cliente, telefone_cliente)
    
    # Cadastro de produtos
    produtos = cadastrar_produtos()
    print(f"Bem-vindo ao sistema de delivery, {nome_cliente}!\n")
    print("Produtos disponíveis para pedido:\n")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto.mostrar_dados()}")
    
    # Selecionando produtos
    itens_selecionados = []
    while True:
        escolha = input("\nDigite o número do produto que deseja adicionar ao pedido (ou '0' para finalizar): ")
        if escolha == '0':
            break
        try:
            indice = int(escolha) - 1
            if 0 <= indice < len(produtos):
                itens_selecionados.append(produtos[indice])
                print(f"'{produtos[indice]._nome}' adicionado ao pedido.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    if not itens_selecionados:
        print("\nNenhum item foi selecionado. Encerrando o sistema.")
        return


    # Selecionando entregador
    entregador = Entregador("Carlos Souza", "Rua B, 456", "Moto")  # Entregador fixo neste exemplo

    # Selecionando método de pagamento
    print("\nMétodos de pagamento disponíveis:")
    metodos_pagamento = ["Dinheiro", "Cartão de Crédito", "Pix"]
    for i, metodo in enumerate(metodos_pagamento, start=1):
        print(f"{i}. {metodo}")
    while True:
        escolha_pagamento = input("Escolha o método de pagamento (digite o número): ")
        try:
            indice_pagamento = int(escolha_pagamento) - 1
            if 0 <= indice_pagamento < len(metodos_pagamento):
                metodo_pagamento = metodos_pagamento[indice_pagamento]
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    # Criando o pedido
    pedido = Pedido(cliente, entregador, itens_selecionados, metodo_pagamento)
    print("\nDetalhes do Pedido:\n")
    print(pedido.mostrar_pedido())

    # Atualizando o status do pedido
    while True:
        atualizar = input("\nDeseja atualizar o status do pedido? (s/n): ")
        if atualizar.lower() == 's':
            pedido.atualizar_status("Entregue")
            print("\nDetalhes atualizados do Pedido:\n")
            print(pedido.mostrar_pedido())
            break
        elif atualizar.lower() == 'n':
            print("\nPedido finalizado sem alterações no status.")
            break
        else:
            print("Opção inválida. Por favor, digite 's' ou 'n'.")