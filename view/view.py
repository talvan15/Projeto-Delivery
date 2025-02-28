import flet as ft

# Simulando um banco de dados de usuários (usuário -> senha)
USUARIOS = {
    "admin": "1234",
    "talvan": "1234"
}

def tela_cadastro(page):
    """ Tela de Cadastro de Usuário """

    def cadastrar_usuario(e):
        novo_usuario = campo_usuario.value
        nova_senha = campo_senha.value

        if novo_usuario in USUARIOS:
            resultado.value = "⚠️ Usuário já existe!"
            resultado.color = "red"
        elif novo_usuario and nova_senha:
            USUARIOS[novo_usuario] = nova_senha  # Adiciona ao dicionário
            resultado.value = "✅ Cadastro realizado com sucesso!"
            resultado.color = "green"
        else:
            resultado.value = "❌ Preencha todos os campos!"
            resultado.color = "red"

        page.update()

    def voltar_login(e):
        page.clean()
        tela_login(page)

    campo_usuario = ft.TextField(label="Novo Usuário")
    campo_senha = ft.TextField(label="Senha", password=True)
    botao_cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar_usuario)
    botao_voltar = ft.ElevatedButton(text="Voltar", on_click=voltar_login)
    resultado = ft.Text("")

    page.add(
        ft.Column([
            ft.Text("📌 Cadastro de Usuário", size=24, weight="bold"),
            campo_usuario,
            campo_senha,
            botao_cadastrar,
            botao_voltar,
            resultado
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )


def tela_login(page):
    """ Tela de Login """
    
    def verificar_login(e):
        usuario = campo_usuario.value
        senha = campo_senha.value

        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            resultado.value = "✅ Login bem-sucedido!"
            resultado.color = "green"
            page.update()
            page.clean()  # Limpa a tela de login
            tela_principal(page)  # Carrega a tela principal
        else:
            resultado.value = "❌ Usuário ou senha incorretos!"
            resultado.color = "red"
            page.update()
    
    def abrir_cadastro(e):
        e.page.clean()
        tela_cadastro(e.page)

    campo_usuario = ft.TextField(label="Usuário")
    campo_senha = ft.TextField(label="Senha", password=True)
    botao_login = ft.ElevatedButton(text="Entrar", on_click=verificar_login)
    botao_cadastro = ft.ElevatedButton(text="Cadastrar", on_click=abrir_cadastro)
    resultado = ft.Text("")

    page.add(
        ft.Column([
            ft.Text("Lo no Sistema de Delivery", size=24, weight="bold"),
            campo_usuario,
            campo_senha,
            botao_login,
            botao_cadastro,
            resultado
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

def voltar_tela(page):
        page.clean()
        tela_principal(page)
        page.update()

def tela_principal(page):
    """ Tela Principal do Sistema de Delivery """

    def abrir_cardapio(e):
        page.clean()
        tela_cardapio(page)

    def abrir_pedidos(e):
        page.clean()
        tela_pedidos(page)

    page.add(
        ft.Column([
            ft.Text("🏠 Tela Principal", size=24, weight="bold"),
            ft.ElevatedButton("Consultar Cardápio", on_click=abrir_cardapio),
            ft.ElevatedButton("Fazer Pedido", on_click=abrir_pedidos)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

def tela_cardapio(page):
    """ Tela de Cardápio """
    page.clean()
    page.add(ft.Text("📜 Cardápio do Restaurante", size=24, weight="bold"))
    page.add(ft.Text("🍕 Pizza - R$ 30.00 (Comida)"))
    page.add(ft.Text("🥤 Suco - R$ 5"))
    page.add(ft.Text("🍔 Hambúrguer - R$ 20"))
    page.add(ft.ElevatedButton("Adicionar ao Pedido", on_click=lambda e: tela_pedidos(page)))
    page.update()
    page.add(ft.ElevatedButton("Voltar", on_click=lambda e: voltar_tela(page)))
    page.update()

def tela_pedidos(page):
    """ Tela de Pedidos """
    page.clean()
    page.add(ft.Text("🛒 Fazer Pedido", size=24, weight="bold"))
    page.add(ft.ElevatedButton("Voltar", on_click=lambda e: voltar_tela(page)))
    page.update()

def main(page: ft.Page):
    page.clean()
    page.title = "Sistema de Delivery"
    page.window_widith = 800
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tela_login(page)  # Começa pela tela de login
    page.update()


ft.app(target=main)
