import os
from model.cliente import Cliente
from model.entregador import Entregador
from model.pedido import Pedido
from model.produto import Produto
from model.restaurante import Restaurante

# Função para salvar informações dos restaurantes em um arquivo
def salvar_restaurantes_no_arquivo(restaurantes):
    with open("restaurantes.txt", "a") as file:
        for restaurante in restaurantes:
            file.write(f"{restaurante._nome}, {restaurante._endereco}, {restaurante._cnpj}\n")

# Função para carregar restaurantes de um arquivo
def carregar_restaurantes_do_arquivo():
    restaurantes = []
    try:
        with open("restaurantes.txt", "r") as file:
            for line in file:
                nome, endereco, cnpj = line.strip().split(", ")
                restaurantes.append(Restaurante(nome, endereco, cnpj))
    except FileNotFoundError:
        pass  # Caso o arquivo não exista, retorna uma lista vazia
    return restaurantes

# Função para cadastrar produtos no sistema
def cadastrar_produtos():
    produtos = [
        Produto("Pizza", 40.00, "Pizza de queijo e pepperoni"),
        Produto("Refrigerante", 5.00, "Refrigerante de cola 350ml"),
        Produto("Sobremesa", 10.00, "Torta de chocolate")
    ]
    return produtos

# Função para realizar o login do cliente
def login_cliente():
    os.system('cls')
    print("\n--------------Seja bem-vindo ao nosso app--------------")
    print("\nPor favor, insira seus dados:")
    nome_cliente = input("Nome: ")
    endereco_cliente = input("Endereço: ")
    telefone_cliente = input("Telefone: ")
    cliente = Cliente(nome_cliente, endereco_cliente, telefone_cliente)
    return cliente

# Função para realizar o login do entregador
def login_entregador():
    os.system('cls')
    print("\n--------------Seja bem-vindo ao nosso app--------------")
    print("\nPor favor, insira os dados do entregador:")
    nome_entregador = input("Nome: ")
    endereco_entregador = input("Endereço: ")
    cpf_entregador = input("CPF: ")
    veiculo_entregador = input("Veículo: ")
    entregador = Entregador(nome_entregador, endereco_entregador, cpf_entregador, veiculo_entregador)
    return entregador


def restaurante_cardapio():
    os.system('cls')
    
    # Carregar restaurantes cadastrados
    restaurantes = carregar_restaurantes_do_arquivo()
    
    # Função para realizar o login do restaurante e salvar no arquivo
    def login_restaurante():
        while True:
            print("\n--------------Seja bem-vindo ao nosso app--------------")
            print("\nPor favor, insira os dados do restaurante:")
            nome_restaurante = input("Nome: ")
            endereco_restaurante = input("Endereço: ")
            cnpj_restaurante = input("CNPJ: ")
            print("\nSeu restaurante foi cadastrado com sucesso!")

            restaurante = Restaurante(nome_restaurante, endereco_restaurante, cnpj_restaurante)
            
            # Salvar restaurante no arquivo
            salvar_restaurantes_no_arquivo([restaurante])  # Passamos a lista com o restaurante para a função de salvar
            restaurantes.append(restaurante)  # Adiciona o restaurante na lista local
            
            cadastrar_outro = input("\nDeseja cadastrar outro restaurante? (s/n): ")
            if cadastrar_outro.lower() == 'n':
                break  # Sai do loop e retorna ao menu de login
            elif cadastrar_outro.lower() != 's':
                print("Opção inválida. Por favor, insira 's' ou 'n'.")

    # Função para cadastrar um produto ao cardápio do restaurante
    def cadastrar_produto_restaurante():
        if len(restaurantes) == 0:
            print("Nenhum restaurante cadastrado. Vamos cadastrar um novo restaurante.")
            login_restaurante()
        
        while True:
            print("\n------ Restaurantes Cadastrados ------")
            for i, r in enumerate(restaurantes, start=1):
                print(f"{i}. {r._nome} - {r._endereco}")

            escolha_restaurante = input("\nQual restaurante você deseja adicionar o item? (Digite o número): ")
            try:
                escolha_restaurante = int(escolha_restaurante) - 1
                if 0 <= escolha_restaurante < len(restaurantes):
                    restaurante_escolhido = restaurantes[escolha_restaurante]
                    print(f"Você escolheu o restaurante: {restaurante_escolhido._nome}")
                    
                    # Mostrar cardápio do restaurante escolhido
                    if len(restaurante_escolhido._cardapio) > 0:  # Alterado de cardapio para _cardapio
                        print(f"\nCardápio do {restaurante_escolhido._nome}:")
                        for item in restaurante_escolhido._cardapio:
                            print(f"- {item._nome}: {item._preco} - {item._categoria}")
                    else:
                        print("\nAdicione item ao seu cardápio")

                    nome_item = input("Nome do item: ")
                    preco_item = float(input("Preço do item: "))
                    categoria_item = input("Categoria do item (ex: Pizza, Bebida, Sobremesa): ")

                    item = ItemCardapio(nome_item, preco_item, categoria_item)
                    restaurante_escolhido.adicionar_item_ao_cardapio(item)
                    print(f"Item '{nome_item}' adicionado ao cardápio do restaurante.")
                    
                    cadastrar_mais = input("Deseja adicionar outro item? (s/n): ")
                    if cadastrar_mais.lower() != 's':
                        break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    # Verificar se o restaurante foi cadastrado ou precisa cadastrar um
    cadastrar_produto_restaurante()

# Função para mostrar o cardápio de um restaurante
def mostrar_cardapio_restaurante(restaurante):
    print(f"\nCardápio do restaurante {restaurante._nome}:")
    if len(restaurante._cardapio) == 0:  # Alterado de cardapio para _cardapio
        print("Adicione item ao seu cardápio.")
    else:
        for item in restaurante._cardapio:
            print(f"{item._nome} - {item._preco} - {item._categoria}")

# Função principal que controla o fluxo do sistema
def main():
    while True:
        print("\nEscolha o tipo de login:")
        print("1. Cliente")
        print("2. Entregador")
        print("3. Restaurante")
        tipo_usuario = input("Digite o número da opção: ")

        # Login de acordo com a opção do usuário
        match tipo_usuario:
            case '1':
                cliente = login_cliente()
                break
            case '2':
                entregador = login_entregador()
                break
            case '3':
                restaurante_cardapio()
                break
            case _:
                print("Opção inválida. Tente novamente.")
            
    # Cadastro de produtos
    produtos = cadastrar_produtos()
    print("\nBem-vindo ao sistema de delivery!\n")

    # Exibir lista de produtos disponíveis
    print("Produtos disponíveis para pedido:\n")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto.mostrar_dados()}")

    # Seleção de produtos
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

    # Seleção de entregador fixo (exemplo)
    entregador = Entregador("Carlos Souza", "Rua B, 456", "Moto")

    # Seleção do método de pagamento
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
        match atualizar.lower():
            case 's':
                pedido.atualizar_status("Entregue")
                print("\nDetalhes atualizados do Pedido:\n")
                print(pedido.mostrar_pedido())
                break
            case 'n':
                print("\nPedido finalizado sem alterações no status.")
                break
            case _:
                print("Opção inválida. Por favor, digite 's' ou 'n'.")