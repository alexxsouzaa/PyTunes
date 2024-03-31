from typing import Tuple
from customtkinter import *
from PIL import Image, ImageTk


class App(CTk):
    def __init__(self):
        super().__init__()
        # ============= Janela =============
        self.title('teste')
        self.geometry('450x668')
        self.resizable(False, False)
        self.config(bg='#141414')
        
        # ============= Capa da musica =============
        capa = CTkImage(Image.open('assets\\img\\capa.png'), size=(418, 386))
        self.capa_musica = CTkLabel(
            self,
            image=capa,
            text='',
            corner_radius=8,
            fg_color='#000',
            bg_color='#000'
        )
        self.capa_musica.place(x=8, y=16)

        # ============= Titulo da Musica =============
        self.titulo_musica = CTkLabel(
            self,
            text='The Weeknd - Starboy',
            text_color='#fff',
            font=('Source Sans Pro', 16, 'bold'),
            fg_color='#000'
        )
        self.titulo_musica.place(x=40, y=438)
        
        # ============= Botão de favorito =============
        icon_favorito = CTkImage(Image.open('assets\\icons\\icon_pack\\heart.png'))
        self.botao_favorito = CTkButton(
            self,
            image=icon_favorito,
            text='',
            width=0,
            height=0,
            fg_color='#000'
        )
        self.botao_favorito.place(x=386, y=438)

        # ============= Linha do Tempo =============
        self.container_linha_tempo = CTkFrame(
            self,
            width=369,
            height=32,
            fg_color='#000',
            bg_color='#000'
        )
        self.container_linha_tempo.place(x=40, y=496)
        
        # Linha do tempo
        self.linha_tempo = CTkProgressBar(
            self.container_linha_tempo,
            width=369,
            height=4,
            progress_color='#fff',
            corner_radius=8,
        )
        self.linha_tempo.place(x=0, y=0)
        
        # Minuto atual da musica
        self.minuto_atual = CTkLabel(
            self.container_linha_tempo,
            text='1:38',
            text_color='#fff'
        )
        self.minuto_atual.place(x=0, y=12)
        
        # Minuto total da musica
        self.minuto_total = CTkLabel(
            self.container_linha_tempo,
            text='3:99',
            text_color='#fff'
        )
        self.minuto_total.place(x=342, y=12)

        # ============= Botões =============
        # Botão Repeat
        self.icon_repeat = CTkImage(Image.open('assets\\icons\\icon_pack\\repeat.png'))
        self.butao_repeat = CTkButton(
            self,
            image=self.icon_repeat,
            text='',
            width=0,
            height=0,
            fg_color='#000',
            hover_color='#000'
        )
        self.butao_repeat.place(x=89, y=586)

        # Botão Previous
        self.icon_previous = CTkImage(
            Image.open('assets\\icons\\icon_pack\\previous.png'))
        self.butao_previous = CTkButton(
            self,
            image=self.icon_previous,
            text='',
            width=0,
            height=0,
            fg_color='#000'
        )
        self.butao_previous.place(x=138, y=586)

        # Botão Play
        self.icon_play = CTkImage(Image.open(
            'assets\\icons\\icon_pack\\play.png'), size=(64, 64))
        self.butao_play = CTkButton(
            self,
            image=self.icon_play,
            text='',
            width=0,
            height=0,
            fg_color='#000'
        )
        self.butao_play.place(x=188, y=564)

        # Botão Next
        self.icon_next = CTkImage(Image.open('assets\\icons\\icon_pack\\next.png'))
        self.butao_next = CTkButton(
            self,
            image=self.icon_next,
            text='',
            width=0,
            height=0,
            fg_color='#000'
        )
        self.butao_next.place(x=284, y=586)

        # Botão random
        self.icon_random = CTkImage(Image.open('assets\\icons\\icon_pack\\random.png'))
        self.butao_random = CTkButton(
            self,
            image=self.icon_random,
            text='',
            width=0,
            height=0,
            fg_color='#000'
        )
        self.butao_random.place(x=332, y=586)


if __name__ == '__main__':
    window = App()
    window.mainloop()
