import os
from model.cliente import Cliente
from model.entregador import Entregador
from model.pedido import Pedido
from model.restaurante import Restaurante
from model.itemcardapio import ItemCardapio  # Importando a classe ItemCardapio

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
        ItemCardapio("Pizza", 40.00, "Pizza de queijo e pepperoni"),
        ItemCardapio("Refrigerante", 5.00, "Refrigerante de cola 350ml"),
        ItemCardapio("Sobremesa", 10.00, "Torta de chocolate")
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
    telefone_entregador = input("Telefone: ")
    cpf_entregador = input("CPF: ")
    veiculo_entregador = input("Veículo: ")
    entregador = Entregador(nome_entregador, endereco_entregador, telefone_entregador, cpf_entregador, veiculo_entregador)
    return entregador


def restaurante_cardapio(restaurantes):
    os.system('cls')
    
    if not restaurantes:  # Verifique se a lista de restaurantes está vazia
        print("Não há restaurantes cadastrados. Por favor, cadastre um restaurante.")
        return

    def cadastrar_produto_restaurante():
        
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
                    
                    if len(restaurante_escolhido.cardapio) > 0:
                        print(f"\nCardápio do {restaurante_escolhido._nome}:")
                        for item in restaurante_escolhido.cardapio:
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

    cadastrar_produto_restaurante()

def login_restaurante():
    os.system('cls')
    restaurantes = carregar_restaurantes_do_arquivo()
    while True:
        print("\n--------------Seja bem-vindo ao nosso app--------------")
        print("\nPor favor, insira os dados do restaurante:")
        nome_restaurante = input("Nome: ")
        endereco_restaurante = input("Endereço: ")
        cnpj_restaurante = input("CNPJ: ")
        print("\nSeu restaurante foi cadastrado com sucesso!")

        restaurante = Restaurante(nome_restaurante, endereco_restaurante, cnpj_restaurante)
        
        salvar_restaurantes_no_arquivo([restaurante])
        restaurantes.append(restaurante)
        
        cadastrar_outro = input("\nDeseja cadastrar outro restaurante? (s/n): ")
        if cadastrar_outro.lower() == 'n':
            break
        elif cadastrar_outro.lower() != 's':
            print("Opção inválida. Por favor, insira 's' ou 'n'.")

# Função para mostrar o cardápio de um restaurante
def mostrar_cardapio_restaurante(restaurante):
    print(f"\nCardápio do restaurante {restaurante._nome}:")
    if len(restaurante.cardapio) == 0:
        print("Adicione item ao seu cardápio.")
    else:
        for item in restaurante.cardapio:
            print(f"{item._nome} - {item._preco} - {item._categoria}")

def main():
    restaurantes = carregar_restaurantes_do_arquivo()
    while True:
        print("\nEscolha o tipo de login:")
        print("1. Cliente")
        print("2. Entregador")
        print("3. Restaurante")
        print("4. Adicionar item no cardapio")
        tipo_usuario = input("Digite o número da opção: ")

        match tipo_usuario:
            case '1':
                cliente = login_cliente()
                break
            case '2':
                entregador = login_entregador()
                break
            case '3':
                restaurante = login_restaurante()
                break
            case '4':
                restaurante_cardapio(restaurantes)
                break
            case _:
                print("Opção inválida. Tente novamente.")
            
    produtos = cadastrar_produtos()
    print("\nBem-vindo ao sistema de delivery!\n")

    print("Produtos disponíveis para pedido:\n")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto.mostrar_dados()}")

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

    entregador = Entregador("Carlos Souza", "Rua B, 456", "999999999", "12345678901", "Moto")

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

    pedido = Pedido(cliente, entregador, itens_selecionados, metodo_pagamento)
    print("\nDetalhes do Pedido:\n")
    print(pedido.mostrar_pedido())

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
