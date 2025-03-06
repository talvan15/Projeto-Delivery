class Pessoa:
    """
    Classe Pessoa que representa uma pessoa genérica.

    Contém informações básicas de uma pessoa, como nome, endereço e telefone,
    além de métodos para manipular essas informações.
    """

    def __init__(self, nome, endereco, telefone):
        """
        Inicializa um objeto Pessoa.

        Args:
            nome (str): Nome da pessoa.
            endereco (str): Endereço da pessoa.
            telefone (str): Número de telefone da pessoa.
        """
        self._nome = nome
        self._endereco = endereco
        self.telefone = telefone

    def get_endereco(self):
        """
        Retorna o endereço da pessoa.

        Returns:
            str: O endereço da pessoa.
        """
        return self._endereco
    
    def set_endereco(self, endereco):
        """
        Atualiza o endereço da pessoa.

        Args:
            endereco (str): O novo endereço da pessoa.
        """
        self._endereco = endereco

    def mostrar_dados(self):
        """
        Retorna uma string formatada com os dados da pessoa.

        Returns:
            str: Nome e endereço da pessoa.
        """
        return f"Nome: {self._nome}, Endereço: {self._endereco}"
