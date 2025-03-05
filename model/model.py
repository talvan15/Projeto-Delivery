# Classe base para Produto
class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def mostrar_dados(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Descrição: {self.descricao}"

# Classe base para Pessoa
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mostrar_dados(self):
        return f"Nome: {self.nome}, Endereço: {self.endereco}"

# Cliente herda da classe Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, endereco, telefone):
        super().__init__(nome, endereco)
        self.telefone = telefone

    def mostrar_dados(self):
        return f"{super().mostrar_dados()}, Telefone: {self.telefone}"

# Entregador herda da classe Pessoa
class Entregador(Pessoa):
    def __init__(self, nome, endereco, veiculo):
        super().__init__(nome, endereco)
        self.veiculo = veiculo

    def mostrar_dados(self):
        return f"{super().mostrar_dados()}, Veículo: {self.veiculo}"

# Pedido que armazena informações dos pedidos
class Pedido:
    def __init__(self, cliente, entregador, itens, metodo_pagamento):
        self.cliente = cliente
        self.entregador = entregador
        self.itens = itens
        self.status = "Pendente"
        self.metodo_pagamento = metodo_pagamento

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total

    def mostrar_pedido(self):
        itens_str = "\n".join([item.mostrar_dados() for item in self.itens])
        return (f"Cliente: {self.cliente.mostrar_dados()}\n"
                f"Entregador: {self.entregador.mostrar_dados()}\n"
                f"Itens:\n{itens_str}\n"
                f"Método de Pagamento: {self.metodo_pagamento}\n"
                f"Total: R${self.calcular_total():.2f}\n"
                f"Status: {self.status}")

# Função para cadastrar produtos
def cadastrar_produtos():
    produtos = []
    produtos.append(Produto("Pizza", 40.00, "Pizza de queijo e pepperoni"))
    produtos.append(Produto("Refrigerante", 5.00, "Refrigerante de cola 350ml"))
    produtos.append(Produto("Sobremesa", 10.00, "Torta de chocolate"))
    return produtos

# Função principal
def main():
    # Informações do cliente
    print("\nPor favor, insira os dados do cliente:")
    nome_cliente = input("Nome: ")
    endereco_cliente = input("Endereço: ")
    telefone_cliente = input("Telefone: ")
    cliente = Cliente(nome_cliente, endereco_cliente, telefone_cliente)
    
    # Cadastro de produtos
    produtos = cadastrar_produtos()
    print("Bem-vindo ao sistema de delivery!\n")
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
                print(f"'{produtos[indice].nome}' adicionado ao pedido.")
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

if __name__ == "__main__":
    main()
