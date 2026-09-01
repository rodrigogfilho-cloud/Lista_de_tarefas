import flet as ft

class Campo_incluir(ft.Row):
    def __init__(self):
        super().__init__()

        self.caixa_texto = ft.TextField(label="Incluir texto",
                                        filled=True)
        self.caixa_selecao = ft.Checkbox(on_change=self.alterar_cor)
        self.armazem = ft.Container(content=ft.Row(controls=[self.caixa_texto,
                                                             self.caixa_selecao]),
                                                             border_radius=10,
                                                             padding=6,
                                                             bgcolor="123456",
                                                             animate=ft.Animation(duration=500))
        self.controls = [self.armazem]

    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.armazem.bgcolor = "654321"
        else:
            self.armazem.bgcolor = "123456"

    @property
    def value(self):
        return self.caixa_texto.value