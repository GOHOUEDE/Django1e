# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:38:24 2023

@author: HOME
"""

import flet as ft
import statistics
u="rrrFF"
toto=('c est egale a 10','ce n est pas egale à 10')[u=="rrr"]
zyae=[2,3,34,3,5,4]
moy=statistics.mean(zyae)
def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value=moy, text_align=ft.TextAlign.RIGHT, width=100)
    t = ft.Text(value=toto, color="green")
    page.controls.append(t)
    page.update()

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main )