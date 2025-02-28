# controllers/controller.py
from model.model import Usuario, Restaurante, Pedido, ItemCardapio

class Controller:
    """Classe que controla a interação entre a view e o modelo."""
    def __init__(self, view):
        self.view = view
        self.usuario = Usuario("João", "123456789", "Rua A, 123")
        self.restaurante = Restaurante("Pizza Place")

        # Adiciona itens ao restaurante
        self.restaurante.adicionar_item(ItemCardapio("Pizza", 30.0, "Comida"))
        self.restaurante.adicionar_item(ItemCardapio("Suco", 5.0, "Bebida"))

    def realizar_pedido(self):
        pedido = Pedido(self.usuario, self.restaurante, self.restaurante.listar_cardapio())
        self.usuario.realizar_pedido(pedido)
        self.view.show_message(f"Pedido realizado! Total: R$ {pedido.calcular_total():.2f}")

    def ver_cardapio(self):
        cardapio = "\n".join(item.exibir_detalhes() for item in self.restaurante.listar_cardapio())
        self.view.show_message(cardapio)