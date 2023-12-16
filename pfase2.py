#Importações

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from random import randint

import ppassagem

def fase2(dificuldade):

    # Funções

    # Janela

    janela = Window(800, 600)
    janela.set_title("The Riddle of The King")

    # Teclado

    teclas = Window.get_keyboard()

    # Fundo

    fundo = GameImage("fundo-fase2.png")

    # Trilha sonora

    musica2 = Sound("musica-fase2.ogg")

    # Sprites

    espadaP = Sprite("item-EspadaPreta.png", 1)
    espadaBr = Sprite("item-EspadaBronze.png", 1)
    espadaO = Sprite("item-EspadaOuro.png", 1)
    espadaB = Sprite("item-EspadaBranca.png", 1)

    espadaP2 = Sprite("item-EspadaPreta.png", 1)
    espadaBr2 = Sprite("item-EspadaBronze.png", 1)
    espadaO2 = Sprite("item-EspadaOuro.png", 1)
    espadaB2 = Sprite("item-EspadaBranca.png", 1)

    espadaP3 = Sprite("item-EspadaPreta.png", 1)
    espadaBr3 = Sprite("item-EspadaBronze.png", 1)
    espadaO3 = Sprite("item-EspadaOuro.png", 1)
    espadaB3 = Sprite("item-EspadaBranca.png", 1)

    espadaP4 = Sprite("item-EspadaPreta.png", 1)
    espadaBr4 = Sprite("item-EspadaBronze.png", 1)
    espadaO4 = Sprite("item-EspadaOuro.png", 1)
    espadaB4 = Sprite("item-EspadaBranca.png", 1)

    espadaP5 = Sprite("item-EspadaPreta.png", 1)
    espadaBr5 = Sprite("item-EspadaBronze.png", 1)
    espadaO5 = Sprite("item-EspadaOuro.png", 1)
    espadaB5 = Sprite("item-EspadaBranca.png", 1)

    velocidade = Sprite("spell-velocidade.png", 1)
    lentidao = Sprite("spell-lentidao.png", 1)
    erro = Sprite("Erro.png")

    bonecoF = Sprite("BonecoFrente.png", 1)
    bonecoC = Sprite("BonecoCosta.png", 1)
    bonecoE = Sprite("BonecoLadoE.png", 1)
    bonecoD = Sprite("BonecoLadoD.png", 1)

    ordem1 = Sprite("ordem-espadas1.png", 1)
    ordem2 = Sprite("ordem-espadas2.png", 1)
    ordem3 = Sprite("ordem-espadas3.png", 1)
    ordem4 = Sprite("ordem-espadas4.png", 1)
    ordem5 = Sprite("ordem-espadas5.png", 1)
    ordem6 = Sprite("ordem-espadas6.png", 1)
    ordem7 = Sprite("ordem-espadas7.png", 1)

    # Velocidade e valores

    valorDoResete = 4

    resete = 0
    valor = 1
    falha = 0

    tempoVelocidade = 0
    tempoLentidao = 0

    tempoRecarga1 = 20
    tempoRecarga2 = 20

    qtdPegada = 0
    qtdQueda = 4

    velBoneco = 500
    velEspada = 250 * dificuldade
    velEspada2 = 250 * dificuldade

    concluido = True
    errado = False

    recarga1 = False
    recarga2 = False

    veloc = False
    lent = False

    item1 = False
    item2 = False
    item3 = False
    item4 = False
    item5 = False
    item6 = False
    item7 = False
    item8 = False
    item9 = False
    item10 = False
    item11 = False
    item12 = False
    item13 = False
    item14 = False
    item15 = False
    item16 = False

    # Posição inicial

    posE1 = janela.width - 200
    posE2 = janela.width - 150
    posE3 = janela.width - 100
    posE4 = janela.width - 50

    erro.x = janela.width / 2 - erro.width / 2
    erro.y = janela.height / 5

    ordem1.x = ordem2.x = ordem3.x = ordem4.x = ordem5.x = ordem6.x = ordem7.x = 30
    ordem1.y = ordem2.y = ordem3.y = ordem4.y = ordem5.y = ordem6.y = ordem7.y = -15

    velocidade.x = ordem1.x * 2
    velocidade.y = ordem1.height - 30

    lentidao.x = velocidade.x + 70
    lentidao.y = velocidade.y

    bonecoF.x = bonecoC.x = bonecoD.x = bonecoE.x = (janela.width / 2) - (bonecoF.width / 2)
    bonecoF.y = bonecoC.y = bonecoD.y = bonecoE.y = janela.height - bonecoF.height - 15

    # ListaDeEspadas

    listaEspadaAleatoria = []
    listaUsuario = []

    # Game looping
    while True:

        musica2.play()

        # Se o usario quiser sair
        if teclas.key_pressed("esc") == 1:
            musica2.stop()
            return None

        #Fundo
        fundo.draw()

        #Caso erre 2 vezes
        if falha == 2:

            velEspada -= 50
            valorDoResete += 1

            resete -= 1
            falha = 0

        # Muda de fase

        if resete == valorDoResete:
            musica2.stop()
            ppassagem.cuts(3, dificuldade)

        #Proxima lista
        if concluido:
            numeroAleatorio = randint(1, 7)

            if numeroAleatorio == 1:
                listaEspadaCerta = [1, 2, 3, 4]

            elif numeroAleatorio == 2:
                listaEspadaCerta = [3, 4, 2, 1]

            elif numeroAleatorio == 3:
                listaEspadaCerta = [4, 3, 2, 1]

            elif numeroAleatorio == 4:
                listaEspadaCerta = [3, 3, 3, 3]

            elif numeroAleatorio == 5:
                listaEspadaCerta = [4, 4, 4, 4]

            elif numeroAleatorio == 6:
                listaEspadaCerta = [2, 2, 2, 2]

            else:
                listaEspadaCerta = [1, 1, 1, 1]

            concluido = False

        #Velocidade

        velTotal = velBoneco * janela.delta_time()  # Velocidade total

        # Controles

        if teclas.key_pressed("W") and bonecoF.y >= 0:
            valor = 1

        if teclas.key_pressed("S"):
            valor = 2

        if teclas.key_pressed("D"):

            valor = 3

            bonecoF.x += velTotal
            bonecoC.x += velTotal
            bonecoD.x += velTotal
            bonecoE.x += velTotal

            if bonecoF.x + bonecoF.width > janela.width:
                bonecoF.x = 0
                bonecoC.x = 0
                bonecoD.x = 0
                bonecoE.x = 0

        if teclas.key_pressed("A"):

            valor = 4

            bonecoF.x -= velTotal
            bonecoC.x -= velTotal
            bonecoD.x -= velTotal
            bonecoE.x -= velTotal

            if bonecoF.x < 0:
                bonecoF.x = janela.width - bonecoF.width
                bonecoC.x = janela.width - bonecoF.width
                bonecoD.x = janela.width - bonecoF.width
                bonecoE.x = janela.width - bonecoF.width

        # Efeitos Especiais

        if teclas.key_pressed("Q"):
            if int(tempoRecarga1) == 20:
                    recarga1 = True
                    veloc = True

        if teclas.key_pressed("E"):
            if int(tempoRecarga2) == 20:
                recarga2 = True
                lent = True

        # Espadas caindo

        while qtdQueda == 4:

            qtdQueda = 0

            listaEspadaAleatoria.append(espadaP)
            listaEspadaAleatoria.append(espadaBr)
            listaEspadaAleatoria.append(espadaO)
            listaEspadaAleatoria.append(espadaB)

            listaEspadaAleatoria[len(listaEspadaAleatoria) - 4].x = randint(0, janela.width - 50)
            listaEspadaAleatoria[len(listaEspadaAleatoria) - 4].y = randint(-300, 0)

            listaEspadaAleatoria[len(listaEspadaAleatoria) - 3].x = randint(0, janela.width - 50)
            listaEspadaAleatoria[len(listaEspadaAleatoria) - 3].y = randint(-300, 0)

            listaEspadaAleatoria[len(listaEspadaAleatoria) - 2].x = randint(0, janela.width - 50)
            listaEspadaAleatoria[len(listaEspadaAleatoria) - 2].y = randint(-300, 0)

            listaEspadaAleatoria[len(listaEspadaAleatoria) - 1].x = randint(0, janela.width - 50)
            listaEspadaAleatoria[len(listaEspadaAleatoria) - 1].y = randint(-300, 0)

        # Queda

        for i in listaEspadaAleatoria:

            i.y += velEspada * janela.delta_time()

            i.draw()

            if errado:
                erro.draw()
                errado = False

                janela.update()
                janela.delay(2000)

            # Se colidir com o personagem

            if i.collided(bonecoF):

                # Qual espada ele pegar

                if i == espadaP:
                    listaUsuario.append(1)

                    qtdPegada += 1

                    if qtdPegada == 1:
                        item1 = True

                    if qtdPegada == 2:
                        item2 = True

                    if qtdPegada == 3:
                        item3 = True

                    if qtdPegada == 4:
                        item4 = True

                if i == espadaBr:
                    listaUsuario.append(2)

                    qtdPegada += 1

                    if qtdPegada == 1:
                        item5 = True

                    if qtdPegada == 2:
                        item6 = True

                    if qtdPegada == 3:
                        item7 = True

                    if qtdPegada == 4:
                        item8 = True

                if i == espadaO:
                    listaUsuario.append(3)

                    qtdPegada += 1

                    if qtdPegada == 1:
                        item9 = True

                    if qtdPegada == 2:
                        item10 = True

                    if qtdPegada == 3:
                        item11 = True

                    if qtdPegada == 4:
                        item12 = True

                if i == espadaB:
                    listaUsuario.append(4)

                    qtdPegada += 1

                    if qtdPegada == 1:
                        item13 = True

                    if qtdPegada == 2:
                        item14 = True

                    if qtdPegada == 3:
                        item15 = True

                    if qtdPegada == 4:
                        item16 = True

                # Se ele pegar a lista errada

                if len(listaUsuario) == 4 and listaUsuario != listaEspadaCerta:

                    qtdPegada = 0
                    falha += 1

                    listaUsuario.clear()

                    errado = True

                    item1 = False
                    item2 = False
                    item3 = False
                    item4 = False
                    item5 = False
                    item6 = False
                    item7 = False
                    item8 = False
                    item9 = False
                    item10 = False
                    item11 = False
                    item12 = False
                    item13 = False
                    item14 = False
                    item15 = False
                    item16 = False

                # Se pegar a lista certa

                if listaUsuario == listaEspadaCerta:

                    velEspada += 100
                    velEspada2 += 100

                    resete += 1
                    qtdPegada = 0

                    listaUsuario.clear()

                    concluido = True

                    item1 = False
                    item2 = False
                    item3 = False
                    item4 = False
                    item5 = False
                    item6 = False
                    item7 = False
                    item8 = False
                    item9 = False
                    item10 = False
                    item11 = False
                    item12 = False
                    item13 = False
                    item14 = False
                    item15 = False
                    item16 = False

                # Loop das proximas espadas
                if qtdQueda < 5:
                    qtdQueda += 1
                else:
                    qtdQueda = 0

                try:
                    listaEspadaAleatoria.remove(i)
                except:
                    continue

            # Se passar da tela


            if i.y + i.height >= janela.height:
                try:
                    listaEspadaAleatoria.remove(i)
                except:
                    continue


                # Loop das proximas espadas

                if qtdQueda < 5:

                    qtdQueda += 1
                else:
                    qtdQueda = 0
        # Desenho

        if item1:
            espadaP2.x = posE1
            espadaP2.draw()

        if item2:
            espadaP3.x = posE2
            espadaP3.draw()

        if item3:
            espadaP4.x = posE3
            espadaP4.draw()

        if item4:
            espadaP5.x = posE4
            espadaP5.draw()

        if item5:
            espadaBr2.x = posE1
            espadaBr2.draw()

        if item6:
            espadaBr3.x = posE2
            espadaBr3.draw()

        if item7:
            espadaBr4.x = posE3
            espadaBr4.draw()

        if item8:
            espadaBr5.x = posE4
            espadaBr5.draw()

        if item9:
            espadaO2.x = posE1
            espadaO2.draw()

        if item10:
            espadaO3.x = posE2
            espadaO3.draw()

        if item11:
            espadaO4.x = posE3
            espadaO4.draw()

        if item12:
            espadaO5.x = posE4
            espadaO5.draw()

        if item13:
            espadaB2.x = posE1
            espadaB2.draw()

        if item14:
            espadaB3.x = posE2
            espadaB3.draw()

        if item15:
            espadaB4.x = posE3
            espadaB4.draw()

        if item16:
            espadaB5.x = posE4
            espadaB5.draw()

        if valor == 1:
            bonecoC.draw()

        if valor == 2:
            bonecoF.draw()

        if valor == 3:
            bonecoD.draw()

        if valor == 4:
            bonecoE.draw()

        if numeroAleatorio == 1:
            ordem1.draw()

        elif numeroAleatorio == 2:
            ordem2.draw()

        elif numeroAleatorio == 3:
            ordem3.draw()

        elif numeroAleatorio == 4:
            ordem4.draw()

        elif numeroAleatorio == 5:
            ordem5.draw()

        elif numeroAleatorio == 6:
            ordem6.draw()

        else:
            ordem7.draw()

        janela.draw_text("Acertos:", ordem1.height * 2 - 100, 0, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(resete), ordem1.height * 2 - 25, 0, size=20, color=(250, 250, 250), font_name="Arial")

        janela.draw_text("Requisito:", ordem1.height * 2 - 100, 30, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(valorDoResete), ordem1.height * 2 - 15, 30, size=20, color=(250, 250, 250), font_name="Arial")

        #Especiais

        if veloc:
            tempoVelocidade += janela.delta_time()

            if int(tempoVelocidade) < 9:

                velBoneco = 1000

            else:
                velBoneco = 500
                tempoVelocidade = 0

                veloc = False

        if recarga1:

            tempoRecarga1 -= janela.delta_time()

            if int(tempoRecarga1) == 0:
                tempoRecarga1 = 20
                recarga1 = False
        else:
            velocidade.draw()

        if lent:
            tempoLentidao += janela.delta_time()

            if int(tempoLentidao) < 9:

                velEspada = 100

            else:
                velEspada = velEspada2
                tempoLentidao = 0
                lent = False

        if recarga2:

            tempoRecarga2 -= janela.delta_time()

            if int(tempoRecarga2) == 0:
                tempoRecarga2 = 20
                recarga2 = False
        else:
            lentidao.draw()

        janela.update()