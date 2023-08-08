#Importações

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from random import randint

import ppassagem

def fase4(dificuldade):
    # Funções

    # Janela

    janela = Window(800, 600)
    janela.set_title("The Riddle of The King")

    # Teclado

    teclas = Window.get_keyboard()

    # Fundo

    fundo = GameImage("fundo-fase4.png")

    # Trilha sonora

    musica4 = Sound("musica-fase4.ogg")

    # Sprites

    livro = Sprite("item-livroSagrado.png", 1)
    espada = Sprite("item-espadaSagrada.png", 1)
    pocao = Sprite("item-pocaoSagrada.png", 1)
    coroa = Sprite("item-coroaSagrada.png", 1)

    livro2 = Sprite("item-livroSagrado.png", 1)
    espada2 = Sprite("item-espadaSagrada.png", 1)
    pocao2 = Sprite("item-pocaoSagrada.png", 1)
    coroa2 = Sprite("item-coroaSagrada.png", 1)

    livro3 = Sprite("item-livroSagrado.png", 1)
    espada3 = Sprite("item-espadaSagrada.png", 1)
    pocao3 = Sprite("item-pocaoSagrada.png", 1)
    coroa3 = Sprite("item-coroaSagrada.png", 1)

    livro4 = Sprite("item-livroSagrado.png", 1)
    espada4 = Sprite("item-espadaSagrada.png", 1)
    pocao4 = Sprite("item-pocaoSagrada.png", 1)
    coroa4 = Sprite("item-coroaSagrada.png", 1)

    livro5 = Sprite("item-livroSagrado.png", 1)
    espada5 = Sprite("item-espadaSagrada.png", 1)
    pocao5 = Sprite("item-pocaoSagrada.png", 1)
    coroa5 = Sprite("item-coroaSagrada.png", 1)

    bonecoF = Sprite("BonecoFrente.png", 1)
    bonecoC = Sprite("BonecoCosta.png", 1)
    bonecoE = Sprite("BonecoLadoE.png", 1)
    bonecoD = Sprite("BonecoLadoD.png", 1)

    velocidade = Sprite("spell-velocidade.png", 1)
    lentidao = Sprite("spell-lentidao.png", 1)
    erro = Sprite("Erro.png")

    ordem1 = Sprite("ordem-lendaria1.png", 1)
    ordem2 = Sprite("ordem-lendaria2.png", 1)
    ordem3 = Sprite("ordem-lendaria3.png", 1)
    ordem4 = Sprite("ordem-lendaria4.png", 1)
    ordem5 = Sprite("ordem-lendaria5.png", 1)
    ordem6 = Sprite("ordem-lendaria6.png", 1)
    ordem7 = Sprite("ordem-lendaria7.png", 1)

    # Velocidade e valores

    valorDoResete = 5

    resete = 0
    valor = 1
    falha = 0

    tempoVelocidade = 0
    tempoLentidao = 0

    tempoRecarga1 = 20
    tempoRecarga2 = 20

    qtdPegada = 0
    qtdQueda = 4

    velBoneco = 600
    velLendaria = 350 * dificuldade
    velLendaria2 = 350 * dificuldade

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

    # ListaDeItens

    listaItensAleatoria = []
    listaUsuario = []

    # Game looping
    while True:

        musica4.play()

        # Se o usario quiser sair

        if teclas.key_pressed("esc") == 1:
            musica4.stop()
            return None

        #Fundo

        fundo.draw()

        #Caso erre 2 vezes

        if falha == 1:
            velLendaria -= 50
            valorDoResete += 2

            resete -= 1
            falha = 0

        # Muda de fase

        if resete == valorDoResete:
            musica4.stop()
            ppassagem.cuts(10, dificuldade)

        if concluido:

            numeroAleatorio = randint(1, 7)

            if numeroAleatorio == 1:
                listaItensCerta = [1, 4, 2, 3]

            elif numeroAleatorio == 2:
                listaItensCerta = [1, 1, 1, 1]

            elif numeroAleatorio == 3:
                listaItensCerta = [4, 4, 4, 4]

            elif numeroAleatorio == 4:
                listaItensCerta = [2, 2, 2, 2]

            elif numeroAleatorio == 5:
                listaItensCerta = [3, 3, 3, 3]

            elif numeroAleatorio == 6:
                listaItensCerta = [3, 4, 2, 1]

            else:
                listaItensCerta = [3, 2, 4, 1]

            concluido = False

        #Velocidade total
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

        # Itens caindo

        while qtdQueda == 4:

            qtdQueda = 0

            listaItensAleatoria.append(livro)
            listaItensAleatoria.append(espada)
            listaItensAleatoria.append(pocao)
            listaItensAleatoria.append(coroa)

            listaItensAleatoria[len(listaItensAleatoria) - 4].x = randint(0, janela.width - 50)
            listaItensAleatoria[len(listaItensAleatoria) - 4].y = randint(-300, 0)

            listaItensAleatoria[len(listaItensAleatoria) - 3].x = randint(0, janela.width - 50)
            listaItensAleatoria[len(listaItensAleatoria) - 3].y = randint(-300, 0)

            listaItensAleatoria[len(listaItensAleatoria) - 2].x = randint(0, janela.width - 50)
            listaItensAleatoria[len(listaItensAleatoria) - 2].y = randint(-300, 0)

            listaItensAleatoria[len(listaItensAleatoria) - 1].x = randint(0, janela.width - 50)
            listaItensAleatoria[len(listaItensAleatoria) - 1].y = randint(-300, 0)

        # Queda

        for i in listaItensAleatoria:

            i.y += velLendaria * janela.delta_time()

            i.draw()

            if errado:
                erro.draw()
                errado = False

                janela.update()
                janela.delay(2000)

            # Se colidir com o personagem

            if i.collided(bonecoF):

                # Qual item ele pegar

                if i == livro:
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

                if i == espada:
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

                if i == pocao:
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

                if i == coroa:
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

                if len(listaUsuario) == 4 and listaUsuario != listaItensCerta:

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

                if listaUsuario == listaItensCerta:
                    velLendaria += 60
                    velLendaria2 += 60

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

                # Loop dos proximos itens

                if qtdQueda < 5:
                    qtdQueda += 1
                else:
                    qtdQueda = 0
                try:
                    listaItensAleatoria.remove(i)
                except:
                    continue

            # Se passar da tela

            if i.y + i.height >= janela.height:
                try:
                    listaItensAleatoria.remove(i)
                except:
                    continue

                # Loop dos proximos itens
                if qtdQueda < 5:

                    qtdQueda += 1
                else:
                    qtdQueda = 0
        # Desenho

        if item1:
            livro2.x = posE1
            livro2.draw()

        if item2:
            livro3.x = posE2
            livro3.draw()

        if item3:
            livro4.x = posE3
            livro4.draw()

        if item4:
            livro5.x = posE4
            livro5.draw()

        if item5:
            espada2.x = posE1
            espada2.draw()

        if item6:
            espada3.x = posE2
            espada3.draw()

        if item7:
            espada4.x = posE3
            espada4.draw()

        if item8:
            espada5.x = posE4
            espada5.draw()

        if item9:
            pocao2.x = posE1
            pocao2.draw()

        if item10:
            pocao3.x = posE2
            pocao3.draw()

        if item11:
            pocao4.x = posE3
            pocao4.draw()

        if item12:
            pocao5.x = posE4
            pocao5.draw()

        if item13:
            coroa2.x = posE1
            coroa2.draw()

        if item14:
            coroa3.x = posE2
            coroa3.draw()

        if item15:
            coroa4.x = posE3
            coroa4.draw()

        if item16:
            coroa5.x = posE4
            coroa5.draw()

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

        janela.draw_text("Acertos:", ordem1.height * 2 - 90, 0, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(resete), ordem1.height * 2 - 20, 0, size=20, color=(250, 250, 250), font_name="Arial")

        janela.draw_text("Requisito:", ordem1.height * 2 - 90, 30, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(valorDoResete), ordem1.height * 2 - 10, 30, size=20, color=(250, 250, 250),font_name="Arial")

        #Especiais

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

                velLendaria = 100

            else:
                velLendaria = velLendaria2
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