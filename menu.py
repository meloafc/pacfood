# -*- coding: cp1252 -*-
import pygame, sys
from pygame.locals import *

#Cabecalho
icone = pygame.image.load('menu/icone.png')
pygame.display.set_icon(icone)
pygame.display.set_caption('PacFood')

pygame.mouse.set_visible(False)

pygame.init()

#musica
musica = pygame.mixer.music.load("menu/abertura1.mp3")
pygame.mixer.music.play(-1)

rect = Rect(450,105,32,32)
opcao_rect = 1
opcao1 = False
opcao2 = False
opcao3 = False
opcao4 = False
opcao5 = False
opcao6 = False

def menu():
    tela = pygame.display.set_mode((800,600))
    menu = pygame.image.load("menu/menu.png")
    personagem = icone
    fonte =  pygame.font.SysFont('Comics Sans', 50)

    #Cores
    branco = (255,255,255)
    amarelo = (242,239,0)

    #opcoes
    global rect
    global opcao_rect
    
    global opcao1
    global opcao2
    global opcao3
    global opcao4
    global opcao5
    global opcao6

    #Menu Opções 
    if opcao_rect == 1: jogar = fonte.render("Jogar", True, amarelo)
    else: jogar = fonte.render("Jogar", True, branco)

    if opcao_rect == 2: recordes = fonte.render("Recordes", True, amarelo)
    else: recordes = fonte.render("Recordes", True, branco)

    if opcao_rect == 3: como_jogar = fonte.render("Como Jogar", True, amarelo)
    else: como_jogar = fonte.render("Como Jogar", True, branco)

    if opcao_rect == 4: creditos = fonte.render("Créditos", True, amarelo)
    else: creditos = fonte.render("Créditos", True, branco)

    if opcao_rect == 5: sobre = fonte.render("Sobre", True, amarelo)
    else: sobre = fonte.render("Sobre", True, branco)

    if opcao_rect == 6: sair = fonte.render("Sair", True, amarelo)
    else: sair = fonte.render("Sair", True, branco)

    #controla para nao sair da tela
    if rect.y > 460:
        rect.y = 105
    elif rect.y < 100:
        rect.y = 455

    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                exit()
                      

            if evento.key == K_UP:
                rect.y -= 70
                opcao_rect -= 1
            elif evento.key == K_DOWN:
                rect.y += 70
                opcao_rect += 1
            elif evento.key == K_RETURN:
                if opcao_rect == 1:
                    opcao1 = True
                if opcao_rect == 2:
                    opcao2 = True
                if opcao_rect == 3:
                    opcao3 = True
                if opcao_rect == 4:
                    opcao4 = True
                if opcao_rect == 5:
                    opcao5 = True
                if opcao_rect == 6:
                    opcao6 = True
                    
    #controla para nao sair da tela
    if opcao_rect == 0:
        opcao_rect = 6
    elif opcao_rect == 7:
        opcao_rect = 1

    tela.blit(menu, (0,0))
    tela.blit(jogar, (500,106))    
    tela.blit(recordes, (500, 176))
    tela.blit(como_jogar, (500,246))
    tela.blit(creditos, (500,316))
    tela.blit(sobre, (500,386))
    tela.blit(sair, (500,456))
    tela.blit(personagem, (rect.x, rect.y))


    pygame.display.flip()

#Menu Opcoes

def menu1():
    import mapa
    
def menu2():
    global opcao2
    menu_recorde = pygame.image.load("menu/recorde.png")
    tela = pygame.display.set_mode((800,600))    
    tela.blit(menu_recorde, (0,0))

    #Abri o arquivo e faz a leitura

    arquivo = open("recorde.txt","r")
    ponto = str(arquivo.readline())
    arquivo.close()

    fonte =  pygame.font.SysFont('Comics Sans', 50)
    branco = (255,255,255)

    pontuacao = fonte.render(ponto, True, branco)

    tela.blit(pontuacao, (350,250))
    
    pygame.display.flip()
    
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_RETURN:
                opcao2 = False
                
def menu3():
    global opcao3
    menu_como_jogar = pygame.image.load("menu/como_jogar.png")
    tela = pygame.display.set_mode((800,600))    
    tela.blit(menu_como_jogar, (0,0))
    pygame.display.flip()
    
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_RETURN:
                opcao3 = False

def menu4():
    global opcao4
    menu_creditos = pygame.image.load("menu/creditos.png")
    tela = pygame.display.set_mode((800,600))    
    tela.blit(menu_creditos, (0,0))
    pygame.display.flip()
    
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_RETURN:
                opcao4 = False                
                
def menu5():
    global opcao5
    menu_sobre = pygame.image.load("menu/sobre.png")
    tela = pygame.display.set_mode((800,600))    
    tela.blit(menu_sobre, (0,0))
    pygame.display.flip()
    
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_RETURN:
                opcao5 = False                
                
def menu6():
    exit()
    pygame.quit()

while True:
    if opcao1 == True:
        musica = pygame.mixer.music.load("menu/abertura1.mp3")
        pygame.mixer.music.play(-1)
        #jogo iniciado
        menu1()

    elif opcao2 == True:
        menu2()        
    elif opcao3 == True:
        menu3()
    elif opcao4 == True:
        menu4()
    elif opcao5 == True:
        menu5()
    elif opcao6 == True:
        menu6()
    else:
        menu()
