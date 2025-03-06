class Restaurante:
    def __init__(self, nome, endereco, cnpj):
        self._nome = nome
        self._endereco = endereco
        self._cnpj = cnpj
        self._cardapio = []  # Lista para armazenar os itens do cardápio
    
    def adicionar_item_ao_cardapio(self, item):
        self._cardapio.append(item)
    
    def mostrar_dados(self):
        return f"{self._nome} - {self._endereco} - {self._cnpj}"
