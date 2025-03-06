from model.pessoa import Pessoa

class Entregador(Pessoa):
    """
    Classe Entregador que herda da classe Pessoa.

    Representa um entregador com nome, endereço, telefone, CPF e veículo utilizado para entrega.
    """

    def __init__(self, nome, endereco, telefone, cpf, veiculo):
        """
        Inicializa um objeto Entregador.

        Args:
            nome (str): Nome do entregador.
            endereco (str): Endereço do entregador.
            telefone (str): Número de telefone do entregador.
            cpf (str): CPF do entregador.
            veiculo (str): Tipo de veículo utilizado pelo entregador.
        """
        super().__init__(nome, endereco, telefone)
        self.cpf = cpf
        self.veiculo = veiculo

    def mostrar_dados(self):
        """
        Retorna uma string formatada com os dados do entregador.

        Returns:
            str: Nome, endereço, telefone, CPF e veículo do entregador.
        """
        return f"{super().mostrar_dados()}, CPF: {self.cpf}, Veículo: {self.veiculo}"
