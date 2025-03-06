class Pedido:
    """
    Classe Pedido que representa um pedido feito por um cliente.

    Contém informações sobre o cliente, restaurante, itens do pedido e método de pagamento.
    """

    def __init__(self, cliente, restaurante, itens, metodo_pagamento="Cartão"):
        """
        Inicializa um objeto Pedido.

        Args:
            cliente (Cliente): O cliente que fez o pedido.
            restaurante (Restaurante): O restaurante onde o pedido foi realizado.
            itens (list[ItemCardapio]): Lista de itens do pedido.
            metodo_pagamento (str, opcional): Método de pagamento escolhido (default é "Cartão").
        """
        self.cliente = cliente
        self.restaurante = restaurante
        self.itens = itens
        self.metodo_pagamento = metodo_pagamento

    def resumo(self):
        """
        Gera um resumo do pedido, incluindo os itens, total e método de pagamento.

        Returns:
            str: Resumo completo do pedido, incluindo informações sobre o cliente, restaurante,
            itens, total e método de pagamento.
        """
        itens_str = "\n".join([f"{item.nome} - R${item.preco:.2f}" for item in self.itens])
        total = sum(item.preco for item in self.itens)
        return (f"Pedido de {self.cliente._nome}:\n"
                f"Restaurante: {self.restaurante._nome}\n"
                f"Itens:\n{itens_str}\n"
                f"Total: R${total:.2f}\n"
                f"Método de pagamento: {self.metodo_pagamento}")
