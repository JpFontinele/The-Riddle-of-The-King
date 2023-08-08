#Importações

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from random import randint

import ppassagem

def fase1(dificuldade):

    # Funções

    #Janela

    janela = Window(800, 600)
    janela.set_title("The Riddle of The King")

    #Teclado

    teclas = Window.get_keyboard()

    #Fundo

    fundo = GameImage("fundo-fase1.png")

    # Trilha sonora

    musica1 = Sound("musica-fase1.ogg")

    #Sprites

    bonecoF = Sprite("BonecoFrente.png", 1)
    bonecoC = Sprite("BonecoCosta.png", 1)
    bonecoE = Sprite("BonecoLadoE.png", 1)
    bonecoD = Sprite("BonecoLadoD.png", 1)

    velocidade = Sprite("spell-velocidade.png", 1)
    lentidao = Sprite("spell-lentidao.png", 1)
    erro = Sprite("Erro.png")

    ordem1 = Sprite("ordem-livros1.png", 1)
    ordem2 = Sprite("ordem-livros2.png", 1)
    ordem3 = Sprite("ordem-livros3.png", 1)
    ordem4 = Sprite("ordem-livros4.png", 1)
    ordem5 = Sprite("ordem-livros5.png", 1)
    ordem6 = Sprite("ordem-livros6.png", 1)
    ordem7 = Sprite("ordem-livros7.png", 1)

    livroR = Sprite("item-livro1.png", 1)
    livroA = Sprite("item-livro2.png", 1)
    livroV = Sprite("item-livro3.png", 1)
    livroM = Sprite("item-livro4.png", 1)

    livroR2 = Sprite("item-livro1.png", 1)
    livroA2 = Sprite("item-livro2.png", 1)
    livroV2 = Sprite("item-livro3.png", 1)
    livroM2 = Sprite("item-livro4.png", 1)

    livroR3 = Sprite("item-livro1.png", 1)
    livroA3 = Sprite("item-livro2.png", 1)
    livroV3 = Sprite("item-livro3.png", 1)
    livroM3 = Sprite("item-livro4.png", 1)

    livroR4 = Sprite("item-livro1.png", 1)
    livroA4 = Sprite("item-livro2.png", 1)
    livroV4 = Sprite("item-livro3.png", 1)
    livroM4 = Sprite("item-livro4.png", 1)

    livroR5 = Sprite("item-livro1.png", 1)
    livroA5 = Sprite("item-livro2.png", 1)
    livroV5 = Sprite("item-livro3.png", 1)
    livroM5 = Sprite("item-livro4.png", 1)

    #Velocidade e valores

    valorDoResete = 3

    valor = 1
    resete = 0

    tempoVelocidade = 0
    tempoLentidao = 0

    tempoRecarga1 = 20
    tempoRecarga2 = 20

    qtdPegada = 0
    qtdQueda = 4

    velLivro = 300 * dificuldade
    velLivro2 = 300 * dificuldade
    velBoneco = 500


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

    #Posição inicial

    posE1 = janela.width - 200
    posE2 = janela.width - 150
    posE3 = janela.width - 100
    posE4 = janela.width - 50

    ordem1.x = ordem2.x = ordem3.x = ordem4.x = ordem5.x = ordem6.x = ordem7.x = 30

    velocidade.x = ordem1.x * 2
    velocidade.y = ordem1.height

    lentidao.x = velocidade.x + 70
    lentidao.y = velocidade.y

    erro.x = janela.width / 2 - erro.width / 2
    erro.y = janela.height / 5

    bonecoF.x = bonecoC.x = bonecoD.x = bonecoE.x = (janela.width / 2) - (bonecoF.width / 2)
    bonecoF.y = bonecoC.y = bonecoD.y = bonecoE.y = janela.height - bonecoF.height - 20

    #Listas
    listaLivrosAleatorios = []
    listaUsuario = []

    #Game looping
    while True:

        musica1.play()

        if teclas.key_pressed("esc") == 1:  # Se o usario quiser sair
            musica1.stop()
            return None

        #Fundo

        fundo.draw()

        # ListaDeLivros

        if concluido:
            numeroAleatorio = randint(1, 7)

            if numeroAleatorio == 1:
                listaLivrosCerta = [4, 1, 2, 3]

            elif numeroAleatorio == 2:
                listaLivrosCerta = [1, 2, 4, 3]

            elif numeroAleatorio == 3:
                listaLivrosCerta = [3, 2, 4, 1]

            elif numeroAleatorio == 4:
                listaLivrosCerta = [3, 3, 3, 3]

            elif numeroAleatorio == 5:
                listaLivrosCerta = [2, 2, 2, 2]

            elif numeroAleatorio == 6:
                listaLivrosCerta = [1, 1, 1, 1]

            else:
                listaLivrosCerta = [4, 4, 4, 4]

            concluido = False

        #Muda de fase

        if resete == valorDoResete:
            musica1.stop()
            ppassagem.cuts(2, dificuldade)

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

        #Efeitos Especiais

        if teclas.key_pressed("Q"):
            if int(tempoRecarga1) == 20:
                recarga1 = True
                veloc = True

        if teclas.key_pressed("E"):
            if int(tempoRecarga2) == 20:
                recarga2 = True
                lent = True

        #Livros caindo
        while qtdQueda == 4:

            qtdQueda = 0

            listaLivrosAleatorios.append(livroR)
            listaLivrosAleatorios.append(livroA)
            listaLivrosAleatorios.append(livroV)
            listaLivrosAleatorios.append(livroM)

            listaLivrosAleatorios[len(listaLivrosAleatorios) - 4].x = randint(0, janela.width - 50) #Livro Rosa
            listaLivrosAleatorios[len(listaLivrosAleatorios) - 4].y = randint(-300, 0)

            listaLivrosAleatorios[len(listaLivrosAleatorios) - 3].x = randint(0, janela.width - 50) #Livro Azul
            listaLivrosAleatorios[len(listaLivrosAleatorios) - 3].y = randint(-300, 0)

            listaLivrosAleatorios[len(listaLivrosAleatorios) - 2].x = randint(0, janela.width - 50) #Livro Vermelho
            listaLivrosAleatorios[len(listaLivrosAleatorios) - 2].y = randint(-300, 0)

            listaLivrosAleatorios[len(listaLivrosAleatorios) - 1].x = randint(0, janela.width - 50) #Livro marrom
            listaLivrosAleatorios[len(listaLivrosAleatorios) - 1].y = randint(-300, 0)

        #Queda

        for i in listaLivrosAleatorios:

            i.y += velLivro * janela.delta_time()

            i.draw()

            if errado:
                erro.draw()
                errado = False

                janela.update()
                janela.delay(2000)

            #Se colidir com o personagem

            if i.collided(bonecoF):

                #Qual livro ele pegar

                if i == livroR:
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

                if i == livroA:
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

                if i == livroV:
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

                if i == livroM:
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

                if len(listaUsuario) == 4 and listaUsuario != listaLivrosCerta:

                    listaUsuario.clear()
                    qtdPegada = 0

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

                if listaUsuario == listaLivrosCerta:

                    velLivro += 100
                    velLivro2 += 100

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

                #Loop dos proximos livros

                if qtdQueda < 5:
                    qtdQueda += 1
                else:
                    qtdQueda = 0

                try:
                    listaLivrosAleatorios.remove(i)
                except:
                    continue

            #Se passar da tela

            if i.y + i.height >= janela.height:
                try:
                    listaLivrosAleatorios.remove(i)
                except:
                    continue

                # Loop dos proximos livros
                if qtdQueda < 5:

                    qtdQueda += 1
                else:
                    qtdQueda = 0

        # Desenho

        if item1:
            livroR2.x = posE1
            livroR2.draw()

        if item2:
            livroR3.x = posE2
            livroR3.draw()

        if item3:
            livroR4.x = posE3
            livroR4.draw()

        if item4:
            livroR5.x = posE4
            livroR5.draw()

        if item5:
            livroA2.x = posE1
            livroA2.draw()

        if item6:
            livroA3.x = posE2
            livroA3.draw()

        if item7:
            livroA4.x = posE3
            livroA4.draw()

        if item8:
            livroA5.x = posE4
            livroA5.draw()

        if item9:
            livroV2.x = posE1
            livroV2.draw()

        if item10:
            livroV3.x = posE2
            livroV3.draw()

        if item11:
            livroV4.x = posE3
            livroV4.draw()

        if item12:
            livroV5.x = posE4
            livroV5.draw()

        if item13:
            livroM2.x = posE1
            livroM2.draw()

        if item14:
            livroM3.x = posE2
            livroM3.draw()

        if item15:
            livroM4.x = posE3
            livroM4.draw()

        if item16:
            livroM5.x = posE4
            livroM5.draw()

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

        janela.draw_text("Acertos:", ordem1.height * 2 - 40, 70, size=20,color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(resete), ordem1.height * 2 + 30, 70, size=20, color=(250, 250, 250), font_name="Arial")

        janela.draw_text("Requisito:",  ordem1.height * 2 - 40, 90, size=20, color=(250, 250, 250), font_name="Arial")
        janela.draw_text(str(valorDoResete), ordem1.height * 2 + 40, 90, size=20, color=(250, 250, 250), font_name="Arial")


        #Poderes

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

                velLivro = 100

            else:

                velLivro = velLivro2
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