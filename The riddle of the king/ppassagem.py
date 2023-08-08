#Importações

from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sound import *

import pfase1
import pfase2
import pfase3
import pfase4

def cuts(valor, dificuldade=1):

    # Funções

    janela = Window(800, 600)
    janela.set_title("The Riddle of The King")

    #Teclas

    teclas = Window.get_keyboard()

    #musica
    creditoMusica = Sound("musica-creditos.ogg")

    #Imagens

    creditoImagem = GameImage("creditosImagem.png")
    movimento = GameImage("regra-movimentacao.png")

    regra1 = GameImage("regra-fase1.png")
    regra2 = GameImage("regra-fase2.png")
    regra3 = GameImage("regra-fase3.png")
    regra4 = GameImage("regra-fase4.png")

    if valor == 1:
        pfase1.fase1(1)

    elif valor == 2:
        pfase2.fase2(dificuldade)

    elif valor == 3:
        pfase3.fase3(dificuldade)

    elif valor == 4:
        pfase4.fase4(dificuldade)

    elif valor == 5:

        while teclas.key_pressed("esc") == 0: #Se o usario quiser sair
            regra1.draw()
            janela.update()

    elif valor == 6:

        while teclas.key_pressed("esc") == 0:  # Se o usario quiser sair
            regra2.draw()
            janela.update()

    elif valor == 7:

        while teclas.key_pressed("esc") == 0:  # Se o usario quiser sair
            regra3.draw()
            janela.update()

    elif valor == 8:

        while teclas.key_pressed("esc") == 0:  # Se o usario quiser sair
            regra4.draw()
            janela.update()

    elif valor == 9:

        while teclas.key_pressed("esc") == 0:  # Se o usario quiser sair
            movimento.draw()
            janela.update()

    elif valor == 10:

        while teclas.key_pressed("esc") == 0:  # Se o usario quiser sair
            creditoMusica.play()
            creditoImagem.draw()
            janela.update()

        creditoMusica.stop()

    elif valor == 11:
        pfase1.fase1(1)

    elif valor == 12:
        pfase1.fase1(2)

    elif valor == 13:
        pfase1.fase1(3)
