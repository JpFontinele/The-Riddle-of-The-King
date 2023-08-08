#Importações

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from random import randint

import ppassagem

def fase3(dificuldade):

    # Funções

    #Janela

    janela = Window(800, 600)
    janela.set_title("The Riddle of The King")

    #Teclado

    teclas = Window.get_keyboard()

    #Fundo

    fundo = GameImage("fundo-fase3.png")

    # Trilha sonora

    musica3 = Sound("musica-fase3.ogg")

    #Sprites

    bonecoF = Sprite("BonecoFrente.png", 1)
    bonecoC = Sprite("BonecoCosta.png", 1)
    bonecoE = Sprite("BonecoLadoE.png", 1)
    bonecoD = Sprite("BonecoLadoD.png", 1)

    velocidade = Sprite("spell-velocidade.png", 1)
    lentidao = Sprite("spell-lentidao.png", 1)
    erro = Sprite("Erro.png")

    ordem1 = Sprite("ordem-pocao1.png", 1)
    ordem2 = Sprite("ordem-pocao2.png", 1)
    ordem3 = Sprite("ordem-pocao3.png", 1)
    ordem4 = Sprite("ordem-pocao4.png", 1)
    ordem5 = Sprite("ordem-pocao5.png", 1)
    ordem6 = Sprite("ordem-pocao6.png", 1)
    ordem7 = Sprite("ordem-pocao7.png", 1)

    pocaoV = Sprite("item-pt1.png", 1)
    pocaoA = Sprite("item-pt2.png", 1)
    pocaoVe = Sprite("item-pt3.png", 1)
    pocaoAm = Sprite("item-pt4.png", 1)

    pocaoV2 = Sprite("item-pt1.png", 1)
    pocaoA2 = Sprite("item-pt2.png", 1)
    pocaoVe2 = Sprite("item-pt3.png", 1)
    pocaoAm2 = Sprite("item-pt4.png", 1)

    pocaoV3 = Sprite("item-pt1.png", 1)
    pocaoA3 = Sprite("item-pt2.png", 1)
    pocaoVe3 = Sprite("item-pt3.png", 1)
    pocaoAm3 = Sprite("item-pt4.png", 1)

    pocaoV4 = Sprite("item-pt1.png", 1)
    pocaoA4 = Sprite("item-pt2.png", 1)
    pocaoVe4 = Sprite("item-pt3.png", 1)
    pocaoAm4 = Sprite("item-pt4.png", 1)

    pocaoV5 = Sprite("item-pt1.png", 1)
    pocaoA5 = Sprite("item-pt2.png", 1)
    pocaoVe5 = Sprite("item-pt3.png", 1)
    pocaoAm5 = Sprite("item-pt4.png", 1)

    #Velocidade e valores

    valorDoResete = 5

    resete = 0
    falha = 0
    valor = 1

    tempoVelocidade = 0
    tempoLentidao = 0

    tempoRecarga1 = 20
    tempoRecarga2 = 20

    velPocao = 250* dificuldade
    velPocao2 = 250 * dificuldade
    velBoneco = 600


    qtdQueda = 4
    qtdPegada = 0

    errado = False
    concluido = True

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

    #Posição inicial

    posE1 = janela.width - 200
    posE2 = janela.width - 150
    posE3 = janela.width - 100
    posE4 = janela.width - 50

    ordem1.x = ordem2.x = ordem3.x = ordem4.x = ordem5.x = ordem6.x = ordem7.x = 30
    ordem1.y = ordem2.y = ordem3.y = ordem4.y = ordem5.y = ordem6.y = ordem7.y = - 35

    velocidade.x = ordem1.x * 2
    velocidade.y = ordem1.height - 30

    lentidao.x = velocidade.x + 70
    lentidao.y = velocidade.y

    erro.x = janela.width / 2  - erro.width / 2
    erro.y = janela.height / 5

    bonecoF.x = bonecoC.x = bonecoD.x = bonecoE.x = (janela.width / 2) - (bonecoF.width / 2)
    bonecoF.y = bonecoC.y = bonecoD.y = bonecoE.y = janela.height - bonecoF.height - 20

    #Lista

    listaPocoesAleatorios = []
    listaUsuario = []

    #Game looping

    while True:

        musica3.play()

        if teclas.key_pressed("esc") == 1:  # Se o usario quiser sair
            musica3.stop()
            return None

        #Fundo

        fundo.draw()

        # Caso erre 1 vezes

        if falha == 1:
            velPocao -= 50
            valorDoResete += 1

            resete -= 1
            falha = 0

        # Muda de fase
        if resete == valorDoResete:
            musica3.stop()
            ppassagem.cuts(4, dificuldade)

        #nova lista

        if concluido:
            numeroAleatorio = randint(1, 7)

            if numeroAleatorio == 1:
               listaPocaoCerta = [1, 1, 1, 1]

            elif numeroAleatorio == 2:
                listaPocaoCerta = [2, 2, 2, 2]

            elif numeroAleatorio == 3:
                listaPocaoCerta = [3, 3, 3, 3]

            elif numeroAleatorio == 4:
                listaPocaoCerta = [4, 4, 4, 4]

            elif numeroAleatorio == 5:
                listaPocaoCerta = [1, 2, 3, 4]

            elif numeroAleatorio == 6:
                listaPocaoCerta = [1, 3, 2, 4]

            else:
                listaPocaoCerta = [4, 3, 2, 1]

            concluido = False

        # Velocidade total

        velTotal = velBoneco * janela.delta_time()

        #Controles

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

        #Poções caindo

        while qtdQueda == 4:

            qtdQueda = 0

            listaPocoesAleatorios.append(pocaoV)
            listaPocoesAleatorios.append(pocaoA)
            listaPocoesAleatorios.append(pocaoVe)
            listaPocoesAleatorios.append(pocaoAm)

            listaPocoesAleatorios[len(listaPocoesAleatorios) - 4].x = randint(0, janela.width - 50)
            listaPocoesAleatorios[len(listaPocoesAleatorios) - 4].y = randint(-300, 0)

            listaPocoesAleatorios[len( listaPocoesAleatorios) - 3].x = randint(0, janela.width - 50)
            listaPocoesAleatorios[len( listaPocoesAleatorios) - 3].y = randint(-300, 0)

            listaPocoesAleatorios[len( listaPocoesAleatorios) - 2].x = randint(0, janela.width - 50)
            listaPocoesAleatorios[len( listaPocoesAleatorios) - 2].y = randint(-300, 0)

            listaPocoesAleatorios[len( listaPocoesAleatorios) - 1].x = randint(0, janela.width - 50)
            listaPocoesAleatorios[len( listaPocoesAleatorios) - 1].y = randint(-300, 0)

            #Queda

        for i in  listaPocoesAleatorios:

            i.y += velPocao * janela.delta_time()

            i.draw()

            if errado:
                erro.draw()
                errado = False

                janela.update()
                janela.delay(2000)

            #Se colidir com o personagem

            if i.collided(bonecoF):

                #Qual poção ele pegar

                if i == pocaoV:
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

                if i == pocaoA:
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

                if i == pocaoVe:
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

                if i == pocaoAm:
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

               #Se ele pegar a lista errada

                if len(listaUsuario) == 4 and listaUsuario != listaPocaoCerta:

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

                #Se pegar a lista certa

                if listaUsuario == listaPocaoCerta:
                    velPocao += 50
                    velPocao2 += 50
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

                #Loop das proximas poçoes

                if qtdQueda < 5:
                    qtdQueda += 1
                else:
                    qtdQueda = 0

                try:
                    listaPocoesAleatorios.remove(i)
                except:
                    continue

            #Se passar da tela


            if i.y + i.height >= janela.height:
                try:
                    listaPocoesAleatorios.remove(i)
                except:
                    continue

                # Loop das proximas poções

                if qtdQueda < 5:
                    qtdQueda += 1
                else:
                    qtdQueda = 0

        # Desenho

        if item1:
            pocaoV2.x = posE1
            pocaoV2.draw()

        if item2:
            pocaoV3.x = posE2
            pocaoV3.draw()

        if item3:
            pocaoV4.x = posE3
            pocaoV4.draw()

        if item4:
            pocaoV5.x = posE4
            pocaoV5.draw()

        if item5:
            pocaoA2.x = posE1
            pocaoA2.draw()

        if item6:
            pocaoA3.x = posE2
            pocaoA3.draw()

        if item7:
            pocaoA4.x = posE3
            pocaoA4.draw()

        if item8:
            pocaoA5.x = posE4
            pocaoA5.draw()

        if item9:
            pocaoVe2.x = posE1
            pocaoVe2.draw()

        if item10:
            pocaoVe3.x = posE2
            pocaoVe3.draw()

        if item11:
            pocaoVe4.x = posE3
            pocaoVe4.draw()

        if item12:
            pocaoVe5.x = posE4
            pocaoVe5.draw()

        if item13:
            pocaoAm2.x = posE1
            pocaoAm2.draw()

        if item14:
            pocaoAm3.x = posE2
            pocaoAm3.draw()

        if item15:
            pocaoAm4.x = posE3
            pocaoAm4.draw()

        if item16:
            pocaoAm5.x = posE4
            pocaoAm5.draw()

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

        janela.draw_text("Acertos:", ordem1.height * 2 - 80 , 0, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(resete), ordem1.height * 2 + 10 , 0, size=20, color=(250, 250, 250), font_name="Arial")

        janela.draw_text("Requisito:", ordem1.height * 2 - 80 , 30, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(valorDoResete), ordem1.height * 2 + 10 , 30, size=20, color=(250, 250, 250),font_name="Arial")

        #Efeitos

        if veloc:

            tempoVelocidade += janela.delta_time()

            if int(tempoVelocidade) < 9:

                velBoneco = 1400

            else:
                velBoneco = 700
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

                velPocao = 100

            else:
                velPocao = velPocao2
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