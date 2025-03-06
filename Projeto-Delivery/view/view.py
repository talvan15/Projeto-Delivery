import os
from model.cliente import Cliente
from model.entregador import Entregador  
from model.pedido import Pedido
from model.restaurante import Restaurante
from model.itemcardapio import ItemCardapio  

# Função para cadastrar cliente
def cadastrar_cliente():
    os.system('cls')  # Limpa a tela
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    return Cliente(nome, endereco, telefone)

# Função para escolher um restaurante
def escolher_restaurante(restaurantes):
    os.system('cls') 
    print("\nEscolha um restaurante:")
    for i, restaurante in enumerate(restaurantes, start=1):
        print(f"{i}. {restaurante._nome}")  

    # Garantir que a escolha seja válida
    escolha = 0
    while escolha < 1 or escolha > len(restaurantes):
        escolha = int(input(f"Digite o número do restaurante desejado (1 a {len(restaurantes)}): "))
        if escolha < 1 or escolha > len(restaurantes):
            print("Escolha inválida. Tente novamente.")
    
    return restaurantes[escolha - 1]  # Retorna o restaurante escolhido

# Função para o cliente fazer a compra (fazer um pedido)
def fazer_compra(cliente, restaurante):
    os.system('cls')  # Limpa a tela
    print(f"\n{cliente._nome}, agora você pode escolher os itens do cardápio do restaurante {restaurante._nome}")
    
    # Exibindo o cardápio do restaurante
    cardapio = restaurante.mostrar_cardapio()
    print("\nCardápio:")
    for i, item in enumerate(cardapio, start=1):
        print(f"{i}. {item.nome} - R${item.preco:.2f}") 

    # Permitindo que o cliente escolha os itens
    itens_escolhidos = []
    while True:
        escolha = int(input(f"\nDigite o número do item que deseja adicionar ao pedido (1 a {len(cardapio)}), ou 0 para finalizar: "))
        if escolha == 0:
            if itens_escolhidos:  
                print("\nPedido finalizado!")
                break
            else:
                print("\nVocê não adicionou nenhum item ao pedido. Tente novamente.")
        elif 1 <= escolha <= len(cardapio):
            item = cardapio[escolha - 1]
            itens_escolhidos.append(item)
            print(f"Você adicionou {item.nome} ao seu pedido.")
        else:
            print("Escolha inválida. Tente novamente.")
    
    # Solicitar o método de pagamento
    metodo_pagamento = input("Escolha o método de pagamento (Cartão/Dinheiro/Outro): ")
    
    # Criação do pedido com o método de pagamento
    if itens_escolhidos:
        pedido = Pedido(cliente, restaurante, itens_escolhidos, metodo_pagamento)
        print(f"\nSeu pedido foi feito com sucesso!\n{pedido.resumo()}")
        
        # Escolher um entregador
        entregador = escolher_entregador()
        print(f"Entregador atribuído: {entregador.mostrar_dados()}")
        pedido.entregador = entregador  # Associando o entregador ao pedido
        print(f"Pedido atribuído para {entregador._nome}. A entrega será realizada.")
    else:
        print("\nVocê não fez nenhum pedido.")

# Função para escolher um entregador
def escolher_entregador():
    
    # Lista de entregadores
    entregador1 = Entregador("Carlos Silva", "Rua das Laranjeiras, 100", "999876543", "12345678901", "Moto")
    entregador2 = Entregador("Ana Costa", "Av. Brasil, 200", "988765432", "98765432101", "Carro")
    entregador3 = Entregador("Roberto Souza", "Rua Nova, 300", "977654321", "11223344556", "Bicicleta")

    entregadores = [entregador1, entregador2, entregador3]

    # Exibindo entregadores disponíveis
    print("\nEscolha um entregador:")
    for i, entregador in enumerate(entregadores, start=1):
        print(f"{i}. {entregador._nome} - {entregador.veiculo}")
    
    # Garantir que a escolha seja válida
    escolha = 0
    while escolha < 1 or escolha > len(entregadores):
        escolha = int(input(f"Digite o número do entregador desejado (1 a {len(entregadores)}): "))
        if escolha < 1 or escolha > len(entregadores):
            print("Escolha inválida. Tente novamente.")
    
    return entregadores[escolha - 1]

def main():
    os.system('cls') 
    # Criar restaurantes
    restaurante1 = Restaurante("Pizzaria Bella", "Rua das Flores, 123", "123456789")
    restaurante2 = Restaurante("Churrascaria do Gaúcho", "Av. Central, 456", "987654321")
    restaurante3 = Restaurante("Sushi House", "Rua da Praia, 789", "555123456")
    restaurante4 = Restaurante("Sabor divino", "R. Francisco Alves, 443", "467364382")
    restaurante5 = Restaurante("Pizzarely", "Centro, 537", "632738232")

    # Adicionando itens aos cardápios dos restaurantes

    # Restaurante 1
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza Margherita", 35.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza Calabresa", 40.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza Portuguesa", 45.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Frango com Catupiry", 42.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Pepperoni", 50.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza Veggie", 48.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Calabresa com Queijo", 45.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza 4 Queijos", 55.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Nutella", 60.0, "Pizza"))
    restaurante1.adicionar_item_ao_cardapio(ItemCardapio("Pizza Margherita Grande", 70.0, "Pizza"))

    # Restaurante 2
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Churrasco", 50.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Espetinho", 20.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Costela no Bafo", 80.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Picanha", 120.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Maminha", 55.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Linguiça Calabresa", 25.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Espetinho de Frango", 18.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Coração de Frango", 30.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Alcatra", 70.0, "Carnes"))
    restaurante2.adicionar_item_ao_cardapio(ItemCardapio("Fraldinha", 85.0, "Carnes"))

    # Restaurante 3
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Sushi de Salmão", 30.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Temaki", 25.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Sashimi de Atum", 40.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Uramaki", 35.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Hossomaki", 32.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Maki de Pepino", 28.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Sushi de Camarão", 38.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Ceviche", 45.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Nigiri", 25.0, "Sushi"))
    restaurante3.adicionar_item_ao_cardapio(ItemCardapio("Sushi Vegetariano", 22.0, "Sushi"))

    # Restaurante 4
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Feijoada", 45.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Arroz com Pequi", 40.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Frango Assado", 50.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Baião de Dois", 35.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Carne de Sol com Mandioca", 60.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Feijão Tropeiro", 55.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Galinhada", 40.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Peixada", 75.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Mocofava", 50.0, "Prato Principal"))
    restaurante4.adicionar_item_ao_cardapio(ItemCardapio("Tapioca", 20.0, "Sobremesa"))

    # Restaurante 5
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Atum", 30.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza Marguerita Especial", 40.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Calabresa", 35.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Frango", 42.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Pepperoni", 45.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza Veggie", 50.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza 4 Queijos", 55.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Chocolate", 60.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza de Alho", 30.0, "Pizza"))
    restaurante5.adicionar_item_ao_cardapio(ItemCardapio("Pizza Margherita Especial", 50.0, "Pizza"))

    # Lista de restaurantes
    restaurantes = [restaurante1, restaurante2, restaurante3, restaurante4, restaurante5]

    # Cadastra o cliente
    cliente = cadastrar_cliente()
    print(f"\nCliente cadastrado: {cliente.mostrar_dados()}")

    # Escolher restaurante
    restaurante_escolhido = escolher_restaurante(restaurantes)
    print(f"\nVocê escolheu o restaurante: {restaurante_escolhido._nome}")
    
    # Cliente faz a compra
    fazer_compra(cliente, restaurante_escolhido)


