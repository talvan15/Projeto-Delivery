class Restaurante:
    def _init_(self, nome, endereco, cnpj):
        self._nome = nome
        self._endereco = endereco
        self._cnpj = cnpj
        self._cardapio = []  # Lista de itens no cardápio

    def adicionar_item_ao_cardapio(self, item):
        self._cardapio.append(item)
        
    def mostrar_cardapio(self):
        if not self._cardapio:
            return "O cardápio está vazio."
        return "\n".join([item.exibir_detalhes() for item in self._cardapio])