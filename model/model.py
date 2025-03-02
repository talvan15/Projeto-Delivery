class Pessoa:
    """"Classe base para representar uma pessoa."""
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    def get_nome(self):
        """Get para o atributo nome."""
        return self._nome

    def get_telefone(self):
        """Get para o atributo telefone."""
        return self._telefone


class Usuario(Pessoa):
    """Classe para representar um usuário."""
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone)
        self._endereco = endereco
        self._pedidos = []

    def realizar_pedido(self, pedido):
        """Método para realizar um pedido"""
        self._pedidos.append(pedido)

    def visualizar_pedidos(self):
        """Método para visualizar os pedidos realizados."""
        return self._pedidos


class Restaurante:
    """Classe para representar um restaurante."""
    def __init__(self, nome):
        self._nome = nome
        self._cardapio = {}
        self._pedidos = []
        

    def adicionar_item(self, item):
        """Método para adicionar um item ao cardápio."""
        self._cardapio[item._nome] = item._preco

    def listar_cardapio(self):
        """Método para listar o cardápio do restaurante."""
        cardapio_formatado = "Cardápio do Restaurante:\n"
        for nome, preco in self._cardapio.items():
            cardapio_formatado += f"{nome}: R${preco:.2f}\n"
        return cardapio_formatado


class ItemCardapio:
    """Classe para representar um item do cardápio."""
    def __init__(self, nome, preco, categoria):
        self._nome = nome
        self._preco = preco
        self._categoria = categoria

    def exibir_detalhes(self):
        """Método para exibir os detalhes do item do cardápio."""
        return f"{self._nome} - R${self._preco:.2f} ({self._categoria})"


class Pedido:
    """Classe para representar um pedido."""
    def __init__(self, cliente, restaurante, itens):
        self._cliente = cliente
        self._restaurante = restaurante
        self._itens = itens
        self._status = "Pendente"

    def calcular_total(self):
        """Método para calcular o total do pedido."""
        return sum(item._preco for item in self._itens)

    def atualizar_status(self, status):
        """Método para atualizar o status do pedido."""
        self._status = status
