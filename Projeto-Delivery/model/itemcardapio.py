class ItemCardapio:
    """
    Classe que representa um item do cardápio.

    Um item do cardápio possui um nome, um preço e uma categoria.
    """

    def __init__(self, nome, preco, categoria):
        """
        Inicializa um objeto ItemCardapio.

        Args:
            nome (str): Nome do item do cardápio.
            preco (float): Preço do item.
            categoria (str): Categoria do item (ex: bebida, prato principal, sobremesa).
        """
        self._nome = nome
        self._preco = preco
        self._categoria = categoria
