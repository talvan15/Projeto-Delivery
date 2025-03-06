from model.pessoa import Pessoa
class Cliente(Pessoa):
    def _init_(self, nome, endereco, telefone):
        super()._init_(nome, endereco)
        self._telefone = telefone


    def mostrar_dados(self):
        return f"{super().mostrar_dados()}, Telefone: {self._telefone}"