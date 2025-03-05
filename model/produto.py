class Produto:
    def __init__(self, nome, preco, descricao):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def mostrar_dados(self):
        return f"Produto: {self._nome}, Preço: R${self._preco:.2f}, Descrição: {self._descricao}"
