from model.pessoa import Pessoa
class Entregador(Pessoa):
    def _init_(self, nome, endereco,cpf, veiculo):
        super()._init_(nome, endereco)
        self._cpf=cpf
        self._veiculo = veiculo

    def mostrar_dados(self):
        return f"{super().mostrar_dados()}, CPF: {self._cpf} Veículo: {self._veiculo}"