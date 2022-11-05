# 1. Crie uma interface gráfica que tenha essas características:

#  Um título da tela
#  Uma cor de fundo (background) de sua preferência.
#  Link para a paleta de cores:
# https://color.adobe.com/pt/explore
#  A janela será dimensionada com 300 de largura, 200 de
# altura, 550 de posicionamento da esquerda/direita e 100 de
# posicionamento do topo para o rodapé.
#  A janela ela não irá ser modificada, então desative com o
# comando resizable.


from tkinter import *
import tkinter as tk


class atvd1:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'

janela = tk.Tk()
objeto = atvd1(janela)
janela.mainloop()