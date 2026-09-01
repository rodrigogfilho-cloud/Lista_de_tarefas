import flet as ft
from classe_campo_incluir import Campo_incluir

def main(page:ft.Page):
    page.title = "Armazenamendo de Tarefas"
    page.bgcolor = "#ecdab3"
    page.horizontal_alignment = "center"
    page.window.width = 800
    page.window.height = 800

    title = ft.Text(value="Tarefas 📄",size=30,font_family="Arial",)
    lista_incluir = []
    def adicionar_campo():
        novo_campo = Campo_incluir()
        lista_incluir.append(novo_campo)

        page.controls.insert(-1, novo_campo)

    def excluir_campo():
        copia_incluir = lista_incluir.copy()
        for campo in copia_incluir:
            if campo.caixa_selecao.value == True:
                lista_incluir.remove(campo)



    button_excluir = ft.FloatingActionButton(icon=ft.Icon(ft.Icons.DELETE_FOREVER,
                                                          color="#000"),
                                                          bgcolor="#fff",
                                                          hover_color="#babaca",
                                                          on_click=excluir_campo)

    button_incluir = ft.Button(content="Incluir",
                               on_click=adicionar_campo,)
    

    campo_tarefas = ft.TextField(value="",
                                 label="Tarefas",
                                 text_align="center",
                                 on_submit=adicionar_campo)

    

    linha_começo = ft.Row(controls=[campo_tarefas, button_incluir],
                          alignment="center",
                          spacing=50)
    
    container = ft.Container(content=linha_começo,
                             bgcolor="#ebd29b",
                             padding=30,
                             border_radius=20,
                             width=550,
                             height=100)





    page.controls = [title,container,button_excluir]
    page.spacing = 45
    page.update()

ft.run(main)