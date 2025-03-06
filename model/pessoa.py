class Pessoa:
    def __init__(self, nome, endereco,telefone):
        self._nome = nome
        self._endereco = endereco
        self. telefone = telefone

    def get_endereco(self):
        return self._endereco
    
    def set_endereco(self, endereco):
        self._endereco = endereco

    def mostrar_dados(self):
        return f"Nome: {self._nome}, Endereço: {self._endereco}"
