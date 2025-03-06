class Restaurante:
    """
    Classe Restaurante que representa um restaurante.

    Contém informações sobre o restaurante, como nome, endereço, telefone,
    além de um cardápio com os itens disponíveis.
    """

    def __init__(self, nome, endereco, telefone):
        """
        Inicializa um objeto Restaurante.

        Args:
            nome (str): Nome do restaurante.
            endereco (str): Endereço do restaurante.
            telefone (str): Número de telefone do restaurante.
        """
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cardapio = []

    def adicionar_item_ao_cardapio(self, item):
        """
        Adiciona um item ao cardápio do restaurante.

        Args:
            item (ItemCardapio): O item a ser adicionado ao cardápio.
        """
        self._cardapio.append(item)

    def mostrar_cardapio(self):
        """
        Retorna a lista de itens do cardápio.

        Returns:
            list[ItemCardapio]: A lista de objetos ItemCardapio que representam os itens do cardápio.
        """
        return self._cardapio  # Retorna a lista de objetos ItemCardapio
