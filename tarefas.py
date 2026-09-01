import flet as ft
from classe_campo_incluir import Campo_incluir

def main(page:ft.Page):
    page.title = "Armazenamendo de Tarefas"
    page.bgcolor = "#white"
    page.horizontal_alignment = "center"
    page.window.width = 700
    page.window.height = 800

    title = ft.Text(value="Tarefas",
                    size=30,
                    font_family="Arial")
    lista_incluir = []
    def adicionar_campo():
        lista_incluir.append()

    def excluir_campo():
        copia_incluir = lista_incluir.copy()
        for campo in copia_incluir:
            if campo.caixa_selecao.value == True:
                lista_incluir.remove(campo)
    def incluir():
        adicionar =0

        for campo in lista_incluir:
            incluir = int(campo.value)
            adicionar = adicionar + incluir


    button_excluir = ft.FloatingActionButton(icon=ft.Icon(ft.Icons.DELETE_FOREVER,
                                                          color="#000"),
                                                          bgcolor="#fff",
                                                          hover_color="#babaca",
                                                          on_click=excluir_campo)

    button_incluir = ft.Button(content="Incluir",
                               on_click=incluir)

    campo_tarefas = ft.TextField(value=0,
                                 label="Tarefas",
                                 read_only=True,
                                 text_align="center",
                                 on_click=adicionar_campo)

    linha_começo = ft.Row(controls=[campo_tarefas, button_incluir],
                          alignment="center",
                          spacing=50)





    page.controls = [title,linha_começo,button_excluir]
    page.spacing = 45
    page.update()

ft.run(main)