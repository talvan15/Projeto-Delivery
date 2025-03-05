class Pedido:
    def __init__(self, cliente, entregador, itens, metodo_pagamento):
        self._cliente = cliente
        self._entregador = entregador
        self._itens = itens
        self._status = "Pendente"
        self._metodo_pagamento = metodo_pagamento

    def atualizar_status(self, novo_status):
        self._status = novo_status

    def calcular_total(self):
        total = sum(item._preco for item in self._itens)
        return total

    def mostrar_pedido(self):
        itens_str = "\n".join([item.mostrar_dados() for item in self._itens])
        return (f"Cliente: {self._cliente.mostrar_dados()}\n"
                f"Entregador: {self._entregador.mostrar_dados()}\n"
                f"Itens:\n{itens_str}\n"
                f"Método de Pagamento: {self._metodo_pagamento}\n"
                f"Total: R${self.calcular_total():.2f}\n"
                f"Status: {self._status}")