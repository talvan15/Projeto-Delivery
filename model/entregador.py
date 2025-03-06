from model.pessoa import Pessoa# Classe Entregador (herda de Pessoa)
class Entregador(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf, veiculo):
        # Chama o construtor da classe base Pessoa (somente com nome, endereco e telefone)
        super().__init__(nome, endereco, telefone)
        # Adiciona os atributos específicos do Entregador
        self.cpf = cpf
        self.veiculo = veiculo

    def mostrar_dados(self):
        # Retorna todos os dados, incluindo os específicos do Entregador
        return f"{super().mostrar_dados()}, CPF: {self.cpf}, Veículo: {self.veiculo}"
