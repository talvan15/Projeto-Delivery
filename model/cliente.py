from model.pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, endereco, telefone):
        super().__init__(nome, endereco)
        self._telefone = telefone

    def mostrar_dados(self):
        return f"{super().mostrar_dados()}, Telefone: {self._telefone}"
