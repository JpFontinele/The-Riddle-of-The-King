#Importações

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
import ppassagem

#Funções

janela = Window(800, 600)
janela.set_title("The Riddle of The King")

#Fundo

fundo = GameImage("fundo-menu.png")

#Mouse e teclado

teclas = Window.get_keyboard()
mouse = Window.get_mouse()

#Trilha sonora

musica = Sound("musica-menu.ogg")

#Opções

novoJogo = Sprite("botao-novojogo.png", 1)
dificuldade = Sprite("botao-nivel.png", 1)
sair = Sprite("botao-sair.png", 1)
controle = Sprite("botao-controle.png", 1)
credito = Sprite("botao-estrela.png", 1)
movimento = Sprite("botao-movimento.png", 1)

fase1 = Sprite("botao-fase1.png", 1)
fase2 = Sprite("botao-fase2.png", 1)
fase3 = Sprite("botao-fase3.png", 1)
fase4 = Sprite("botao-fase4.png", 1)

facil = Sprite("botao-facil.png", 1)
medio = Sprite("botao-medio.png", 1)
dificil = Sprite("botao-dificil.png", 1)

#posição das opções

controle.x = janela.width - controle.width - 5
controle.y = 5

credito.x = 5
credito.y = janela.height - credito.height - 10

movimento.x = 5
movimento.y = credito.y = janela.height - credito.height - 20

novoJogo.x = (janela.width / 2) - novoJogo.width / 2
novoJogo.y = janela.height - novoJogo.height * 5

dificuldade.x = (janela.width / 2) - (dificuldade.width / 2)
dificuldade.y = janela.height - dificuldade.height * 3.5

sair.x = (janela.width / 2) - (sair.width / 2)
sair.y = janela.height - sair.height * 2

fase1.x = (janela.width / 2) - fase1.width / 2
fase1.y = janela.height - fase1.height * 5.7

fase2.x = (janela.width / 2) - (fase2.width / 2)
fase2.y = janela.height - fase2.height * 4.2

fase3.x = (janela.width / 2) - (fase3.width / 2)
fase3.y = janela.height - fase3.height * 2.8

fase4.x = (janela.width / 2) - (fase4.width / 2)
fase4.y = janela.height - fase4.height * 1.4

facil.x = (janela.width / 2) - fase1.width / 2
facil.y = janela.height - fase1.height * 5.0

medio.x = (janela.width / 2) - (fase2.width / 2)
medio.y = janela.height - fase2.height * 3.5

dificil.x = (janela.width / 2) - (fase3.width / 2)
dificil.y = janela.height - fase3.height * 2.0

#Fase

fase = 1
click = True

#Game Looping menu

while True:

    musica.play()

    #Se o usario apertar em novo jogo

    if mouse.is_over_object(novoJogo) and mouse.is_button_pressed(1):
        musica.stop()
        ppassagem.cuts(1, 1)

    #Se o usario apertar em dificuldades

    if mouse.is_over_object(dificuldade) and mouse.is_button_pressed(1):
        click = False

        while teclas.key_pressed("esc") == 0: #Se o usario quiser sair

            if mouse.is_button_pressed(1) == False:

                click = True

            if mouse.is_over_object(facil) and mouse.is_button_pressed(1) and click:
                musica.stop()
                ppassagem.cuts(11, 1)

            if mouse.is_over_object(medio) and mouse.is_button_pressed(1) and click:
                 musica.stop()
                 ppassagem.cuts(12, 2)

            if mouse.is_over_object(dificil) and mouse.is_button_pressed(1) and click:
                musica.stop()
                ppassagem.cuts(13, 3)

            fundo.draw()
            facil.draw()
            medio.draw()
            dificil.draw()
            janela.update()

    #Se o usario apertar em controles

    if mouse.is_over_object(controle) and mouse.is_button_pressed(1):
        click = False

        while teclas.key_pressed("esc") == 0: #Se o usario quiser sair
            if mouse.is_button_pressed(1) == False:

                click = True

            if mouse.is_over_object(fase1) and mouse.is_button_pressed(1) and click:
                ppassagem.cuts(5)

            if mouse.is_over_object(fase2) and mouse.is_button_pressed(1) and click:
                 ppassagem.cuts(6)

            if mouse.is_over_object(fase3) and mouse.is_button_pressed(1) and click:
                ppassagem.cuts(7)

            if mouse.is_over_object(fase4) and mouse.is_button_pressed(1) and click:
                ppassagem.cuts(8)

            if mouse.is_over_object(movimento) and mouse.is_button_pressed(1) and click:
                ppassagem.cuts(9)

            fundo.draw()
            fase1.draw()
            fase2.draw()
            fase3.draw()
            fase4.draw()
            movimento.draw()
            janela.update()

    #Se o usario apertar nos creditos

    if mouse.is_over_object(credito) and mouse.is_button_pressed(1):
        musica.stop()
        ppassagem.cuts(10)


    #Se o usario apertar em sair

    if mouse.is_over_object(sair) and mouse.is_button_pressed(1):
        janela.close()

    #Desenho

    fundo.draw()
    controle.draw()
    credito.draw()
    novoJogo.draw()
    dificuldade.draw()
    sair.draw()
    janela.update()