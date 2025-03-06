class ItemCardapio:
    def __init__(self, nome, preco, categoria):
        self._nome = nome
        self._preco = preco
        self._categoria = categoria

    def mostrar_dados(self):
        return f"{self._nome} - {self._preco} - {self._categoria}"
