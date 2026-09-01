import flet as ft

class Campo_incluir(ft.Row):
    def __init__(self):
        super().__init__()

        self.caixa_texto = ft.TextField(label="Pendente",
                                        filled=True)
        self.caixa_selecao = ft.Checkbox(on_change=self.alterar_cor)
        self.armazem = ft.Container(content=ft.Row(controls=[self.caixa_selecao,
                                                             self.caixa_texto]),
                                                             border_radius=10,
                                                             padding=6,
                                                             bgcolor="#123456",
                                                             animate=ft.Animation(duration=500))

        self.button_delete=ft.Button(content="Delete",
                                     width=100)
        self.nutton_edit=ft.Button(content="Edit",
                                   width=100)
        self.linha_buttons = ft.Column(controls=[self.button_delete, self.nutton_edit])

        self.controls = [self.armazem,self.linha_buttons]

    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.armazem.bgcolor = "#654321"
        else:
            self.armazem.bgcolor = "#123456"

    @property
    def value(self):
        return self.caixa_texto.value