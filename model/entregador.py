from model.pessoa import Pessoa
class Entregador(Pessoa):
    def __init__(self, nome, endereco, veiculo):
        super().__init__(nome, endereco)
        self._veiculo = veiculo

    def mostrar_dados(self):
        return f"{super().mostrar_dados()}, Veículo: {self._veiculo}"