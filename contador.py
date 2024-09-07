import flet as ft
from time import sleep
import random
import pygame
import json

with open('./json/frases.json', encoding='utf-8') as dados:
    jdados = json.load(dados)

def main(page: ft.Page):
    page.window_height= 280
    page.window_max_height= 280
    page.window_width= 420
    page.window_max_width= 420
    page.theme_mode= ft.ThemeMode.LIGHT
    page.title= 'Contador'
    page.bgcolor= '#999ea0'
    page.padding= 0
    page.vertical_alignment= 'center'
    page.horizontal_alignment= 'center'
    page.update()

    page.fonts = {
        "Hour_font": "./fonts/DOMINICA.TTF"
    }

    ################# TOCAR ALARME #################
    def alarme(e):
        path_alarme = './audio/alarm.mp3'
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(path_alarme)
            pygame.mixer_music.play()
        except Exception as er:
            return er
    
    ################# 30 min #################
    def meia_hora(e):
        m = 29
        while True:
            for s in range(59, -1, -1):
                text_c.value = f"{m}:{s}"
                if s == 0:
                    m = m -1
                page.update()
                sleep(1)
            if m == 0:
                text_c.value = 'Fim!'
                frase = random.choice(jdados['frase'])
                h2.value= f'{frase}'
                page.update()
                alarme(e)
                break
        block.visible = True
        page.update()    

    ################# CONTADOR #################
    def contador(e):
        block.visible = False
        text_c.size = 60

        if block.value == "30 min":
            meia_hora(e)
        
    btn = ft.ElevatedButton(
        text= 'Start',
        bgcolor= '#f4f1ed',
        on_click= contador,
        color= '#10110d'
    )

    block = ft.Dropdown(
        hint_text= 'Chose!',
        width= 95,
        height= 60,
        border= 'transparent',
        border_radius= 16,
        bgcolor= ft.colors.GREY_300,
        focused_border_color= 'transparent',
        options=[
            ft.dropdown.Option("30 min"),
            ft.dropdown.Option("1 hora"),
            ft.dropdown.Option("2 horas"),
            ft.dropdown.Option("3 horas"),
        ]
    )

    h2 = ft.Text(
        value= f'{random.choice(jdados['frase'])}',
        size=16,
        text_align= 'center',
        color= '#10110d',
        font_family= 'Hour_font'
    ) 

    text_c = ft.Text(
        value= '',
        size=24,
        text_align= 'center',
        color= '#10110d',
        font_family= 'Hour_font',
        italic= True
    )

    acima = fundo = ft.Container(
        width=page.window_width,
        height=40,
        bgcolor= 'transparent',
        alignment=ft.alignment.center,
        content=ft.Row([h2], alignment=ft.MainAxisAlignment.CENTER),
    )
 
    fundo =   ft.Container(
                content=ft.Row([
                    block,
                    text_c, 
                    btn,
                    ],alignment=ft.MainAxisAlignment.SPACE_AROUND),
                image_src="./img/bg2.gif",  # Substitua pelo caminho da sua imagem
                image_fit=ft.ImageFit.COVER,  # Ajusta a imagem para cobrir o container
                width=420,
                height=243,
                alignment=ft.alignment.center,
            )
                
    stack = ft.Stack(
        [
            fundo,
            acima
        ]
    )

    page.add(stack)

ft.app(target=main)