# -*- coding: cp1252 -*-
"""
Imagens de propriedade de David Reilly
retiradas do seguinte site:
http://pinproject.com/pacman/pacman.htm
"""

import pygame, sys
from pygame.locals import *
import random

pygame.init()

#  ________________
#_/ Resolucao Tela \_________________________________

largura = 600
altura = 600

tela = pygame.display.set_mode((largura,altura),0, 32)
fonte =  pygame.font.SysFont('Comics Sans', 20)
placar = 0

#   _____________________
#__/ Controle geral jogo \_________________________________________

#Fase inicial
fase = 1

#Controle da Vida Extra
extra = 10000 #aumenta a cada vida que o pac ganha

#Controla a morte do Pac
morrendo = False 
morrendo_laco = 1

#Controle da pontuacao ao comer o fantasma
quantidade_fantasma_comido = 0

#Controla a pausa do começo do jogo, ou passagem de fase
intro = True

#Controle do Print da Super Pastilha
super_p = 0

#Controla o Fim do Jogo
fase_final = False
fim_jogo = False

#Contador de vulnerabilidade dos fantasmas
fraco = False
tempo_fantasma_vulneravel = 0

#Sons
som_super_pastilha = pygame.mixer.Sound('sons/fantasma_fraco.wav') #Som da super pastilha
vida_extra = pygame.mixer.Sound('sons/vida_extra.wav') #Som da Vida extra

#Variaveis da Fruta
tempo = random.choice(range(500,1000,10))
fruta_escolhida = None
frutas = []
rect_fruta = None
coordenada_fruta = (216,288)
ponto = None
contador_delay = 0

#listas contendo Rects do labirinto
move_direita = []
move_esquerda = []
move_baixo = []
move_cima = []

parede = []
pastilha = []
super_pastilha = []
pastilha_comida = []

bloco = None

#Variavel que conta quantos lacos ja foram executados
laco = 0


#   _________
#__/ Imagens \_______________________________________

pacman_ = pygame.image.load('sprite/pacman.gif')
p0 = pygame.image.load('blocos/0.gif')

def cor_mapa(cor):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16
    
    p1 = pygame.image.load('blocos/'+cor+'/1.gif')
    p2 = pygame.image.load('blocos/'+cor+'/2.gif')
    p3 = pygame.image.load('blocos/'+cor+'/3.gif')
    p4 = pygame.image.load('blocos/'+cor+'/4.gif')
    p5 = pygame.image.load('blocos/'+cor+'/5.gif')
    p6 = pygame.image.load('blocos/'+cor+'/6.gif')
    p7 = pygame.image.load('blocos/'+cor+'/7.gif')
    p8 = pygame.image.load('blocos/'+cor+'/8.gif')
    p9 = pygame.image.load('blocos/'+cor+'/9.gif')
    p10 = pygame.image.load('blocos/'+cor+'/10.gif')
    p11 = pygame.image.load('blocos/'+cor+'/11.gif')
    p12 = pygame.image.load('blocos/'+cor+'/12.gif')
    p13 = pygame.image.load('blocos/'+cor+'/13.gif')
    p14 = pygame.image.load('blocos/'+cor+'/14.gif')
    p15 = pygame.image.load('blocos/'+cor+'/15.gif')
    p16 = pygame.image.load('blocos/'+cor+'/16.gif')

cor_mapa("verde")

p17 = pygame.image.load('blocos/17.gif')
p18 = pygame.image.load('blocos/18.gif')
p19 = pygame.image.load('blocos/19.gif')
p20 = pygame.image.load('blocos/20.gif')
p21 = pygame.image.load('blocos/21.gif')

#Frutas
banana = pygame.image.load('frutas/banana.gif')
cereja = pygame.image.load('frutas/cereja.gif')
laranja = pygame.image.load('frutas/laranja.gif')
morango = pygame.image.load('frutas/morango.gif')
uva = pygame.image.load('frutas/uva.gif')

#   ________
#__/ Pacman \_______________________________________________

#Lado Direito
pac_d = pygame.image.load('sprite/pacman-r 1.gif')
pac2_d = pygame.image.load('sprite/pacman-r 2.gif')
pac3_d = pygame.image.load('sprite/pacman-r 3.gif')
pac4_d = pygame.image.load('sprite/pacman-r 4.gif')
pac5_d = pygame.image.load('sprite/pacman-r 5.gif')
pac6_d = pygame.image.load('sprite/pacman-r 6.gif')
pac7_d = pygame.image.load('sprite/pacman-r 7.gif')
pac8_d = pygame.image.load('sprite/pacman-r 8.gif')

#Lado Esquerdo
pac_e = pygame.image.load('sprite/pacman-l 1.gif')
pac2_e = pygame.image.load('sprite/pacman-l 2.gif')
pac3_e = pygame.image.load('sprite/pacman-l 3.gif')
pac4_e = pygame.image.load('sprite/pacman-l 4.gif')
pac5_e = pygame.image.load('sprite/pacman-l 5.gif')
pac6_e = pygame.image.load('sprite/pacman-l 6.gif')
pac7_e = pygame.image.load('sprite/pacman-l 7.gif')
pac8_e = pygame.image.load('sprite/pacman-l 8.gif')

#Cima
pac_c = pygame.image.load('sprite/pacman-u 1.gif')
pac2_c = pygame.image.load('sprite/pacman-u 2.gif')
pac3_c = pygame.image.load('sprite/pacman-u 3.gif')
pac4_c = pygame.image.load('sprite/pacman-u 4.gif')
pac5_c = pygame.image.load('sprite/pacman-u 5.gif')
pac6_c = pygame.image.load('sprite/pacman-u 6.gif')
pac7_c = pygame.image.load('sprite/pacman-u 7.gif')
pac8_c = pygame.image.load('sprite/pacman-u 8.gif')

#Baixo
pac_b = pygame.image.load('sprite/pacman-d 1.gif')
pac2_b = pygame.image.load('sprite/pacman-d 2.gif')
pac3_b = pygame.image.load('sprite/pacman-d 3.gif')
pac4_b = pygame.image.load('sprite/pacman-d 4.gif')
pac5_b = pygame.image.load('sprite/pacman-d 5.gif')
pac6_b = pygame.image.load('sprite/pacman-d 6.gif')
pac7_b = pygame.image.load('sprite/pacman-d 7.gif')
pac8_b = pygame.image.load('sprite/pacman-d 8.gif')

#Morrendo
morte1 = pygame.image.load('sprite/pac_morte/morte1.gif')
morte2 = pygame.image.load('sprite/pac_morte/morte2.gif')
morte3 = pygame.image.load('sprite/pac_morte/morte3.gif')
morte4 = pygame.image.load('sprite/pac_morte/morte4.gif')
morte5 = pygame.image.load('sprite/pac_morte/morte5.gif')
morte6 = pygame.image.load('sprite/pac_morte/morte6.gif')
morte7 = pygame.image.load('sprite/pac_morte/morte7.gif')
morte8 = pygame.image.load('sprite/pac_morte/morte8.gif')
morte9 = pygame.image.load('sprite/pac_morte/morte9.gif')

#Icone de Vida
vida = pygame.image.load('sprite/vida.gif')

#Fantasma Vermelho

#Lado Direito
vermelho_direita = pygame.image.load('fantasma/vermelho_d.gif')
vermelho_direita2 = pygame.image.load('fantasma/vermelho_d2.gif')

#Lado Esquerdo
vermelho_esquerda = pygame.image.load('fantasma/vermelho_e.gif')
vermelho_esquerda2 = pygame.image.load('fantasma/vermelho_e2.gif')

#Cima
vermelho_cima = pygame.image.load('fantasma/vermelho_c.gif')
vermelho_cima2 = pygame.image.load('fantasma/vermelho_c2.gif')

#Baixo
vermelho_baixo = pygame.image.load('fantasma/vermelho_b.gif')
vermelho_baixo2 = pygame.image.load('fantasma/vermelho_b2.gif')

#Fantasma Azul

#Lado Direito
azul_direita = pygame.image.load('fantasma/azul_d.gif')
azul_direita2 = pygame.image.load('fantasma/azul_d2.gif')

#Lado Esquerdo
azul_esquerda = pygame.image.load('fantasma/azul_e.gif')
azul_esquerda2 = pygame.image.load('fantasma/azul_e2.gif')

#Cima
azul_cima = pygame.image.load('fantasma/azul_c.gif')
azul_cima2 = pygame.image.load('fantasma/azul_c2.gif')

#Baixo
azul_baixo = pygame.image.load('fantasma/azul_b.gif')
azul_baixo2 = pygame.image.load('fantasma/azul_b2.gif')

#Fantasma Laranja

#Lado Direito
laranja_direita = pygame.image.load('fantasma/laranja_d.gif')
laranja_direita2 = pygame.image.load('fantasma/laranja_d2.gif')

#Lado Esquerdo
laranja_esquerda = pygame.image.load('fantasma/laranja_e.gif')
laranja_esquerda2 = pygame.image.load('fantasma/laranja_e2.gif')

#Cima
laranja_cima = pygame.image.load('fantasma/laranja_c.gif')
laranja_cima2 = pygame.image.load('fantasma/laranja_c2.gif')

#Baixo
laranja_baixo = pygame.image.load('fantasma/laranja_b.gif')
laranja_baixo2 = pygame.image.load('fantasma/laranja_b2.gif')

#Fantasma Rosa

#Lado Direito
rosa_direita = pygame.image.load('fantasma/rosa_d.gif')
rosa_direita2 = pygame.image.load('fantasma/rosa_d2.gif')

#Lado Esquerdo
rosa_esquerda = pygame.image.load('fantasma/rosa_e.gif')
rosa_esquerda2 = pygame.image.load('fantasma/rosa_e2.gif')

#Cima
rosa_cima = pygame.image.load('fantasma/rosa_c.gif')
rosa_cima2 = pygame.image.load('fantasma/rosa_c2.gif')

#Baixo
rosa_baixo = pygame.image.load('fantasma/rosa_b.gif')
rosa_baixo2 = pygame.image.load('fantasma/rosa_b2.gif')

#Fantasma Fraco

#Lado Direito
fraco_direita = pygame.image.load('fantasma/fraco_d.gif')
fraco_direita2 = pygame.image.load('fantasma/fraco_d2.gif')

#Lado Esquerdo
fraco_esquerda = pygame.image.load('fantasma/fraco_e.gif')
fraco_esquerda2 = pygame.image.load('fantasma/fraco_e2.gif')

#Cima
fraco_cima = pygame.image.load('fantasma/fraco_c.gif')
fraco_cima2 = pygame.image.load('fantasma/fraco_c2.gif')

#Baixo
fraco_baixo = pygame.image.load('fantasma/fraco_b.gif')
fraco_baixo2 = pygame.image.load('fantasma/fraco_b2.gif')

#Fantasma Olho

#Lado Direito
olho_direita = pygame.image.load('fantasma/olho_d.gif')

#Lado Esquerdo
olho_esquerda = pygame.image.load('fantasma/olho_e.gif')

#Cima
olho_cima = pygame.image.load('fantasma/olho_c.gif')

#Baixo
olho_baixo = pygame.image.load('fantasma/olho_b.gif')

#Fim Jogo Imagem
fim = pygame.image.load('menu/fim.png')


#Rects e contadores
pacman = {"rect":Rect(216,288,24,24),"tecla":"direita","vida":2,"morte":False,"velo":2,
        "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,
        "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}

fantasma = {"rect":Rect(216,192,24,24),"tecla":"esquerda","velo":1,"fraco":False,"morto":False,
        "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
        "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
fantasma2 = {"rect":Rect(216,240,24,24),"tecla":"cima","velo":1,"fraco":False,"morto":False,
        "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
        "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
fantasma3 = {"rect":Rect(240,240,24,24),"tecla":"esquerda","velo":1,"fraco":False,"morto":False,
        "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
        "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
fantasma4 = {"rect":Rect(192,240,24,24),"tecla":"direita","velo":1,"fraco":False,"morto":False,
        "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
        "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}

#Lista contendo o dicionario de todos os fantasmas
fantasmas = [fantasma,fantasma2,fantasma3,fantasma4]

#Relogio
relogio = pygame.time.Clock()

def tecla_random(rect):
    #Escolhe um lado para o fantasma se mover
    
    global fantasma
    teclas = []
    for indice in move_esquerda:
        if rect["rect"].contains(indice):
            teclas.append("esquerda")
    for indice in move_direita:
        if rect["rect"].contains(indice):
            teclas.append("direita")
    for indice in move_cima:
        if rect["rect"].contains(indice):
            teclas.append("cima")
    for indice in move_baixo:
        if rect["rect"].contains(indice):
            teclas.append("baixo")

    if len(teclas) != 0:
        rect["tecla"] = random.choice(teclas)

#   ___________________________
#__/ Movimentacao "Automatica" \___________________________________
""" Alguns trechos de codigo de movimentacao copiados do seguinte link:
    http://stthiaggo.blogspot.com.br/2012/05/criando-um-movimento-automatico.html
"""

def direcao(tecla,objeto):
    if tecla == "direita":        
        moveDireita(objeto)
    elif tecla == "esquerda":
        moveEsquerda(objeto)
    elif tecla == "cima":
        moveCima(objeto)
    elif tecla == "baixo":
        moveBaixo(objeto)
        
def moveDireita(objeto):    
    if objeto["lado_direito"] == True:
            if colisao(objeto["rect"]) == True:
                objeto["rect"].x += objeto["velo"]
                if objeto == pacman:
                    comendo_pastilha()
                    comendo_super_pastilha()
                    
            else:
                objeto["rect"].x -= objeto["velo"]
                objeto["lado_direito"] = False
                

    objeto["lado_esquerdo"] = True        
    objeto["para_cima"] = True
    objeto["para_baixo"] = True
    
    objeto["cont"] += 1
    objeto["esquerda"] = 0
    objeto["direita"] += 1
    objeto["cima"] = 0
    objeto["baixo"] = 0
    
def moveEsquerda(objeto):
    global velo
    
    if objeto["lado_esquerdo"] == True:
            if colisao(objeto["rect"]) == True:
                objeto["rect"].x -= objeto["velo"]
                if objeto == pacman:
                    comendo_pastilha()
                    comendo_super_pastilha()
                    
            else:
                objeto["rect"].x += objeto["velo"]
                objeto["lado_esquerdo"] = False
                

    objeto["lado_direito"] = True        
    objeto["para_cima"] = True
    objeto["para_baixo"] = True
    
    objeto["cont"] += 1
    objeto["esquerda"] += 1
    objeto["direita"] = 0
    objeto["cima"] = 0
    objeto["baixo"] = 0

def moveCima(objeto):
    global velo
    
    if objeto["para_cima"] == True:
            if colisao(objeto["rect"]) == True:
                objeto["rect"].y -= objeto["velo"]
                if objeto == pacman:
                    comendo_pastilha()
                    comendo_super_pastilha()
                    
            else:
                objeto["rect"].y += objeto["velo"]
                objeto["para_cima"] = False
                

    objeto["lado_direito"] = True        
    objeto["lado_esquerdo"] = True
    objeto["para_baixo"] = True
    
    objeto["cont"] += 1
    objeto["esquerda"] = 0
    objeto["direita"] = 0
    objeto["cima"] += 1
    objeto["baixo"] = 0

def moveBaixo(objeto):
    global velo
    
    if objeto["para_baixo"] == True:
            if colisao(objeto["rect"]) == True:
                objeto["rect"].y += objeto["velo"]
                if objeto == pacman:
                    comendo_pastilha()
                    comendo_super_pastilha()
                    
            else:
                objeto["rect"].y -= objeto["velo"]
                objeto["para_baixo"] = False
                

    objeto["lado_direito"] = True        
    objeto["lado_esquerdo"] = True
    objeto["para_cima"] = True
    
    objeto["cont"] += 1
    objeto["esquerda"] = 0
    objeto["direita"] = 0
    objeto["cima"] = 0
    objeto["baixo"] += 1

def colisao(objeto):
    #se o objeto nao colidir em nada, retorna-se -1.
    if objeto.collidelist(parede) == -1:   
        return True
    else:
        return False

def comendo_pastilha():    
    global placar
    for rect in pastilha:
        if pacman["rect"].colliderect(rect):
            pastilha_comida.append(rect)
            
            #som
            comendo_pastilha = pygame.mixer.music.load('sons/pastilha.wav')
            pygame.mixer.music.play()
            
            placar += 10

def comendo_super_pastilha():
    global som_super_pastilha
    global fraco
    global tempo_fantasma_vulneravel
    global fantasma,fantasma2,fantasma3,fantasma4    
    
    for rect in super_pastilha:
        if pacman["rect"].colliderect(rect):
            pastilha_comida.append(rect)
            fraco = True
            if fraco == True:
                tempo_fantasma_vulneravel = 0
                for i in fantasmas:
                    i["morto"] = False
                    
            #som
            som_super_pastilha.play()
            

def fantasma_fraco():
    global fraco
    global tempo_fantasma_vulneravel
    global quantidade_fantasma_comido
    global fantasma,fantasma2,fantasma3,fantasma4
    
    if (fraco == True) and (tempo_fantasma_vulneravel <= 420):        
        for i in fantasmas:
            if (i["morto"] == False):
                i["fraco"] = True
        tempo_fantasma_vulneravel += 1
        pac_comendo_fantasma()

    else:
        fraco = False
        for i in fantasmas:
            i["fraco"] = False
        tempo_fantasma_vulneravel = 0
        quantidade_fantasma_comido = 0

def pac_comendo_fantasma():
    global placar
    global fantasmas
    global fantasma,fantasma2,fantasma3,fantasma4
    global quantidade_fantasma_comido
    
    for i in fantasmas:
        if pacman["rect"].colliderect(i["rect"]):
            if i["fraco"] == True:
                
                if i == fantasma:                    
                    quantidade_fantasma_comido += 1
                    
                    fantasma = {"rect":Rect(216,240,24,24),"tecla":"cima","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}

                elif i == fantasma2:
                    quantidade_fantasma_comido += 1
                    
                    fantasma2 = {"rect":Rect(216,240,24,24),"tecla":"cima","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}

                elif i == fantasma3:
                    quantidade_fantasma_comido += 1
                    
                    fantasma3 = {"rect":Rect(216,240,24,24),"tecla":"cima","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}

                elif i == fantasma4:                    
                    quantidade_fantasma_comido += 1
                    
                    fantasma4 = {"rect":Rect(216,240,24,24),"tecla":"cima","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True} 

                if quantidade_fantasma_comido == 1:
                    placar += 200
                if quantidade_fantasma_comido == 2:
                    placar += 400
                if quantidade_fantasma_comido == 3:
                    placar += 800
                if quantidade_fantasma_comido == 4:
                    placar += 1600
                    
                #atualiza a lista fantasma
                fantasmas = [fantasma,fantasma2,fantasma3,fantasma4]
                #som
                comendo_fantasma = pygame.mixer.Sound('sons/comendo_fantasma.wav')
                comendo_fantasma.play()


            
    

#    _______            
#___/ Fruta \_______________________________________________
            
def fruta_random():
    #Escolhe aleatoriamente uma fruta
    
    global fruta_escolhida
    fruta = ["banana","cereja","laranja","morango","uva"]
    fruta_escolhida = random.choice(fruta)
    
def fruta_rect():
    #Cria um rect pra fruta escolhida
    
    global rect_fruta
    rect_fruta = Rect(coordenada_fruta,(24,24))

def fruta_blit():   
    if pacman["rect"].colliderect(rect_fruta) == True:  #Fica blitando a fruta escolhida enquanto ela nao colide com o pac     
        comendo_fruta()

    elif (laco > 1500) or (morrendo == True):   #Se o tempo expirar ou o pacman morrer a fruta some
        fruta_sumindo()

    else:            
        if fruta_escolhida == "banana":
            tela.blit(banana,coordenada_fruta)        
            
        elif fruta_escolhida == "cereja":
            tela.blit(cereja,coordenada_fruta)
            
        elif fruta_escolhida == "laranja":
            tela.blit(laranja,coordenada_fruta)
            
        elif fruta_escolhida == "morango":
            tela.blit(morango,coordenada_fruta)
            
        elif fruta_escolhida == "uva":
            tela.blit(uva,coordenada_fruta)    


def comendo_fruta():
    #Quanto o pac colide com a fruta, a nota é computada e blitada
    
    global ponto    
    global placar
    global rect_fruta
    global contador_delay
    global laco
    global tempo
    fonte =  pygame.font.SysFont('Comics Sans', 25)

    #musica
    comendo_fruta = pygame.mixer.Sound('sons/comendo_fruta.wav')
    comendo_fruta.play()
    
    if (fruta_escolhida == "banana") and (contador_delay == 0):           
        ponto = fonte.render("200", True, (255,255,255))
        placar += 200
        
    
    elif (fruta_escolhida == "cereja") and (contador_delay == 0):            
        ponto = fonte.render("400", True, (255,255,255))
        placar += 400
        
        
    elif (fruta_escolhida == "laranja") and (contador_delay == 0):            
        ponto = fonte.render("600", True, (255,255,255))
        placar += 600
        
        
    elif (fruta_escolhida == "morango") and (contador_delay == 0):            
        ponto = fonte.render("800", True, (255,255,255))
        placar += 800
        
        
    elif (fruta_escolhida == "uva") and (contador_delay == 0):            
        ponto = fonte.render("1000", True, (255,255,255))
        placar += 1000       

    tela.blit(ponto,coordenada_fruta)
    
    if contador_delay == 1:
        pygame.time.delay(500)
        
    contador_delay += 1
    
    if contador_delay == 2:
        #Zera os contadores para a proxima fruta a ser comida
        contador_delay = 0 
        rect_fruta = None
        laco = 0
        tempo = random.choice(range(500,1000,10))

def fruta_sumindo():
    #Se o pacman nao comer(colidir) com a fruta durante um determinado tempo ela some
    global rect_fruta
    global contador_delay
    global laco
    global tempo
    contador_delay = 0 
    rect_fruta = None
    laco = 0
    tempo = random.choice(range(500,1000,10))
    
#   ___________
#__/ Zeradores \__________________________________________

def zerador():
    global move_direita
    global move_esquerda
    global move_baixo
    global move_cima

    global parede
    global pastilha
    global super_pastilha
    global pastilha_comida

    global bloco

    global laco

    global tempo_fantasma_vulneravel
    
    move_direita = []
    move_esquerda = []
    move_baixo = []
    move_cima = []

    parede = []
    pastilha = []
    super_pastilha = []
    pastilha_comida = []

    bloco = None

    laco = 0

    tempo_fantasma_vulneravel = 0
    
def pac_morrendo():
    global morrendo        
    
    for i in fantasmas:
        if pacman["rect"].colliderect(i["rect"]):
            if i["fraco"] == False:
                morrendo = True
                

def zerador_objeto():
    #unico item que nao reseta é a vida do pacman
    
    global pacman
    global fantasma,fantasma2,fantasma3,fantasma4
    global fantasmas
    
    pacman = {"rect":Rect(216,288,24,24),"tecla":"direita","vida":pacman["vida"],"morte":False,"velo":2,
        "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,
        "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}

    fantasma = {"rect":Rect(216,192,24,24),"tecla":"esquerda","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
    fantasma2 = {"rect":Rect(216,240,24,24),"tecla":"cima","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
    fantasma3 = {"rect":Rect(240,240,24,24),"tecla":"esquerda","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
    fantasma4 = {"rect":Rect(192,240,24,24),"tecla":"direita","velo":1,"fraco":False,"morto":True,
            "cont":0,"direita":0,"esquerda":0,"cima":0,"baixo":0,"laco":0,
            "lado_esquerdo":True,"lado_direito":True,"para_cima":True,"para_baixo":True}
    fantasmas = [fantasma,fantasma2,fantasma3,fantasma4]


#   ________
#__/ 1 Fase \____________________________________________________________


#21 ou 41 -direita,baixo
#22 ou 42 -cima,direita,baixo
#23 ou 43 -cima,direita 
#24 ou 44 -esquerda,direita,baixo
#25 ou 45 -todas as direcoes
#26 ou 46 -esquerda,cima,direita
#27 ou 47 -esquerda,baixo
#28 ou 48 -cima,esquerda,baixo
#29 ou 49 -esquerda,cima
#30 ou 50 -esquerda,direita
#31 ou 51 -cima,baixo
#Numeros negativos: possuem apenas os movimentos
#entre 20 a 40 blitam pastilha
#entre 40 a 60 blitam super pastilha

def escolhe_mapa(fase):
    if fase == 1:
        cor_mapa("azul") #Carrega a cor do mapa
        mapa = [[5,15,15,15,15,15,15,15,15,11,15,15,15,15,15,15,15,15,6],#linha1
                [14,41,30,30,24,30,30,30,27,14,21,30,30,30,24,30,30,47,14],#linha2
                [14,31,5,6,31,5,15,6,31,14,31,5,15,6,31,5,6,31,14],#linha3
                [14,31,3,4,31,3,15,4,31,1,31,3,15,4,31,3,4,31,14],#linha4
                [14,22,30,30,25,30,24,30,26,30,26,30,24,30,25,30,30,28,14],#linha5
                [14,31,12,7,31,2,31,12,15,11,15,7,31,2,31,12,7,31,14],#linha6
                [14,23,30,30,28,14,23,30,27,14,21,30,29,14,22,30,30,29,14],#linha7
                [3,15,15,6,31,8,15,7,31,1,31,12,15,10,31,5,15,15,4],#linha8
                [19,19,19,14,31,14,21,30,26,-30,26,30,27,14,31,14,19,19,19],#linha9 observacao: na coluna 10 apos o fantasma sair da casinha ele nao pode mais retornar, exceto quando o fantasma é comido pelo pac 
                [12,15,15,4,31,1,31,5,7,17,12,6,31,1,31,3,15,15,7],#linha10
                [-30,-30,-30,-30,25,30,28,14,-30,-31,-30,14,22,30,25,-30,-30,-30,-30],#linha11
                [12,15,15,6,31,2,31,3,15,15,15,4,31,2,31,5,15,15,7],#linha12
                [19,19,19,14,31,14,22,30,30,30,30,30,28,14,31,14,19,19,19],#linha13
                [5,15,15,4,31,1,31,12,15,11,15,7,31,1,31,3,15,15,6],#linha14
                [14,21,30,30,25,30,26,30,27,14,21,30,26,30,25,30,30,27,14],#linha15
                [14,31,12,6,31,12,15,7,31,1,31,12,15,7,31,5,7,31,14],#linha16
                [14,23,27,14,22,30,24,30,26,30,26,30,24,30,28,14,21,29,14],#linha17
                [8,7,31,1,31,2,31,12,15,11,15,7,31,2,31,1,31,12,10],#linha18
                [14,21,26,30,29,14,23,30,27,14,21,30,29,14,23,30,26,27,14],#linha19
                [14,31,12,15,15,9,15,7,31,1,31,12,15,9,15,15,7,31,14],#linha20
                [14,43,30,30,30,30,30,30,26,30,26,30,30,30,30,30,30,49,14],#linha21
                [3,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,4],#linha22
                ]        

    elif fase == 2:
        cor_mapa("verde") #Carrega a cor do mapa
        mapa = [[5,15,15,15,15,15,15,15,6,-31,5,15,15,15,15,15,15,15,6],#linha1
                [14,21,30,30,30,30,30,27,14,-31,14,21,30,30,30,30,30,27,14],#linha2
                [14,31,5,15,15,15,7,31,1,-31,1,31,12,15,15,15,6,31,14],#linha3
                [14,31,1,41,30,30,30,25,30,26,30,25,30,30,30,47,1,31,14],#linha4
                [14,22,30,28,12,11,7,31,5,15,6,31,12,11,7,22,30,28,14],#linha5
                [14,31,2,23,27,14,21,28,3,15,4,22,27,14,21,29,2,31,14],#linha6
                [14,31,3,7,31,1,22,26,30,30,30,26,28,1,31,12,4,31,14],#linha7
                [14,23,24,30,25,30,28,12,15,15,15,7,22,30,25,30,24,28,14],#linha8
                [8,7,31,2,31,2,22,30,30,-30,30,30,28,2,31,2,22,29,14],#linha9
                [14,21,29,14,31,14,31,5,7,17,12,6,31,14,31,14,31,12,10],#linha10
                [14,31,12,10,31,14,31,14,-30,-31,-30,14,31,14,31,14,23,27,14],#linha11
                [14,23,27,14,31,14,31,3,15,15,15,4,31,14,31,8,7,31,14],#linha12
                [8,7,31,14,31,14,22,30,30,30,30,30,28,14,31,14,21,29,14],#linha13
                [14,21,28,1,31,1,31,12,15,15,15,7,31,1,31,1,31,12,10],#linha14
                [14,22,26,30,25,30,25,30,30,24,30,30,25,30,25,30,26,27,14],#linha15
                [14,31,5,7,31,2,31,12,7,31,12,7,31,2,31,12,6,31,14],#linha16
                [14,31,1,21,29,14,23,24,30,25,30,24,29,14,23,27,1,31,14],#linha17
                [14,22,30,28,12,9,7,31,13,31,13,31,12,9,7,22,30,28,14],#linha18
                [14,31,2,43,30,30,30,25,30,25,30,25,30,30,30,49,2,31,14],#linha19
                [14,31,3,15,15,15,7,31,2,-31,2,31,12,15,15,15,4,31,14],#linha20
                [14,23,30,30,30,30,30,29,14,-31,14,23,30,30,30,30,30,29,14],#linha21
                [3,15,15,15,15,15,15,15,4,-31,3,15,15,15,15,15,15,15,4],#linha22
                ]

    elif fase == 3:
        cor_mapa("roxo") #Carrega a cor do mapa
        mapa = [[5,15,15,15,11,15,15,15,6,-31,5,15,15,15,11,15,15,15,6],#linha1
                [14,21,30,27,14,41,30,27,14,-31,14,21,30,47,14,21,30,27,14],#linha2
                [14,31,13,31,1,31,13,31,1,-31,1,31,13,31,1,31,13,31,14],#linha3
                [14,23,30,25,30,25,30,26,30,26,30,26,30,25,30,25,30,29,14],#linha4
                [8,15,7,31,2,31,12,11,15,15,15,11,7,31,2,31,12,15,10],#linha5
                [14,21,30,28,14,23,27,1,21,30,27,1,21,29,14,22,30,27,14],#linha6
                [14,31,2,31,8,6,22,30,29,2,23,30,28,5,10,31,2,31,14],#linha7
                [14,31,14,31,8,4,31,12,15,9,15,7,31,3,10,31,14,31,14],#linha8
                [14,31,14,31,14,21,25,30,30,-30,30,30,25,27,14,31,14,31,14],#linha9
                [14,31,14,31,1,22,29,5,7,17,12,6,23,28,1,31,14,31,14],#linha10
                [14,31,14,22,30,28,12,10,-30,-31,-30,8,7,22,30,28,14,31,14],#linha11
                [14,31,14,31,2,22,27,3,15,15,15,4,21,28,2,31,14,31,14],#linha12
                [14,31,14,31,14,22,26,30,30,30,30,30,26,28,14,31,14,31,14],#linha13
                [14,31,14,31,14,31,5,15,15,15,15,15,6,31,14,31,14,31,14],#linha14
                [14,31,14,31,14,31,1,21,30,24,30,27,1,31,14,31,14,31,14],#linha15
                [14,31,1,31,14,22,30,28,13,31,13,22,30,28,14,31,1,31,14],#linha16
                [14,23,30,28,14,31,2,23,30,26,30,29,2,31,14,22,30,29,14],#linha17
                [8,15,7,31,1,31,3,15,15,15,15,15,4,31,1,31,12,15,10],#linha18
                [14,21,30,25,30,25,30,24,30,24,30,24,30,25,30,25,30,27,14],#linha19
                [14,31,13,31,2,31,13,31,2,-31,2,31,13,31,2,31,13,31,14],#linha20
                [14,23,30,29,14,43,30,29,14,-31,14,23,30,49,14,23,30,29,14],#linha21
                [3,15,15,15,9,15,15,15,4,-31,3,15,15,15,9,15,15,15,4],#linha22
                ]

    elif fase == 4:
        cor_mapa("vermelho") #Carrega a cor do mapa
        mapa = [[5,15,15,15,15,15,15,15,7,-31,12,15,15,15,15,15,15,15,6],#linha1
                [14,21,30,30,24,30,30,24,30,25,30,24,30,30,24,30,30,27,14],#linha2
                [14,31,5,7,31,12,6,31,2,31,2,31,5,7,31,12,6,31,14],#linha3
                [14,31,1,41,26,27,1,31,14,31,14,31,1,21,26,47,1,31,14],#linha4
                [14,22,30,28,13,22,30,28,14,31,14,22,30,28,13,22,30,28,14],#linha5
                [14,31,2,23,24,29,2,31,1,31,1,31,2,23,24,29,2,31,14],#linha6
                [14,31,8,7,31,12,10,22,30,25,30,28,8,7,31,12,10,31,14],#linha7
                [14,31,1,21,26,27,1,31,12,15,7,31,1,21,26,27,1,31,14],#linha8
                [14,22,30,29,2,23,24,26,30,30,30,26,24,29,2,23,30,28,14],#linha9
                [1,31,12,15,9,7,31,5,7,17,12,6,31,12,9,15,7,31,1],#linha10
                [-30,25,30,30,30,30,28,14,-30,-31,-30,14,22,30,30,30,30,25,-30],#linha11
                [2,31,12,15,15,7,31,3,15,15,15,4,31,12,15,15,7,31,2],#linha12
                [14,22,30,30,24,30,26,30,30,24,30,30,26,30,24,30,30,28,14],#linha13
                [14,31,12,7,31,12,15,15,6,31,5,15,15,7,31,12,7,31,14],#linha14
                [14,22,30,30,25,30,30,27,14,31,14,21,30,30,25,30,30,28,14],#linha15
                [14,31,5,7,31,12,6,31,14,31,14,31,5,7,31,12,6,31,14],#linha16
                [14,31,1,21,26,27,1,31,1,31,1,31,1,21,26,27,1,31,14],#linha17
                [14,22,30,28,13,22,30,25,30,25,30,25,30,28,13,22,30,28,14],#linha18
                [14,31,2,43,24,29,2,31,2,31,2,31,2,23,24,49,2,31,14],#linha19
                [14,31,3,7,31,12,4,31,1,31,1,31,3,7,31,12,4,31,14],#linha20
                [14,23,30,30,26,30,30,26,30,25,30,26,30,30,26,30,30,29,14],#linha21
                [3,15,15,15,15,15,15,15,7,-31,12,15,15,15,15,15,15,15,4],#linha22
                ]
    elif fase == 5:
        cor_mapa("marron") #Carrega a cor do mapa
        mapa = [[5,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,6],#linha1
                [14,21,30,30,30,24,24,30,24,24,30,30,30,24,30,30,30,27,14],#linha2
                [14,31,5,15,7,22,28,13,22,28,5,15,6,31,5,15,6,31,14],#linha3
                [14,31,14,41,24,25,26,30,26,28,14,31,14,31,14,51,14,31,14],#linha4
                [14,31,14,23,26,28,12,11,7,31,14,31,3,15,4,31,14,31,14],#linha5
                [14,31,8,15,7,22,27,14,21,28,14,22,30,24,30,28,14,31,14],#linha6
                [14,31,14,21,30,25,29,14,23,28,14,31,2,31,2,31,14,31,14],#linha7
                [14,31,1,31,13,31,12,9,15,15,4,31,1,31,1,31,1,31,14],#linha8
                [14,23,30,25,30,26,24,30,30,26,30,26,24,26,30,25,30,29,14],#linha9
                [3,15,7,31,12,7,31,5,7,17,12,6,31,12,7,31,12,15,4],#linha10
                [-30,-30,-30,25,30,30,28,14,-30,-31,-30,14,22,30,30,25,-30,-30,-30],#linha11
                [5,15,7,31,12,7,31,3,15,15,15,4,31,12,7,31,12,15,6],#linha12
                [14,21,30,25,30,24,26,30,30,30,30,30,26,24,30,25,30,27,14],#linha13
                [14,31,2,31,2,31,12,15,15,15,15,15,7,31,2,31,2,31,14],#linha14
                [14,31,14,31,14,23,24,30,30,30,30,30,24,29,14,31,14,31,14],#linha15
                [14,31,14,31,3,7,31,12,15,15,15,7,31,12,4,31,14,31,14],#linha16
                [14,31,14,43,30,30,25,30,30,30,30,30,25,30,30,49,14,31,14],#linha17
                [14,31,3,15,15,7,31,5,15,15,15,6,31,12,15,15,4,31,14],#linha18
                [14,22,30,30,30,30,28,14,21,30,27,14,22,30,30,30,30,28,14],#linha19
                [14,31,12,15,15,7,31,1,31,13,31,1,31,12,15,15,7,31,14],#linha20
                [14,23,30,30,30,30,26,30,26,30,26,30,26,30,30,30,30,29,14],#linha21
                [3,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,4],#linha22
                ]
    return mapa

#     ___________________
#____/ Criacao dos Rects \__________________________________________

def mapa_rect(mapa):

    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):

            if mapa[linha][coluna] == 1:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 2:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                
            if mapa[linha][coluna] == 3:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 4:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 5:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 6:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 7:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 8:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 9:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 10:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 11:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 12:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 13:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 14:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 15:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)
                    
            if mapa[linha][coluna] == 16:
                bloco = Rect(coluna*24,linha*24,24,24)
                parede.append(bloco)                
                
            #if mapa[linha][coluna] == 17:
            #if mapa[linha][coluna] == 18:
            #if mapa[linha][coluna] == 19:
            #if mapa[linha][coluna] == 20:
                    
            if (mapa[linha][coluna] == 21) or (mapa[linha][coluna] == 41) or (mapa[linha][coluna] == -21):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_baixo.append(bloco)
                    
            if (mapa[linha][coluna] == 22) or (mapa[linha][coluna] == 42) or (mapa[linha][coluna] == -22):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_baixo.append(bloco)
                move_cima.append(bloco)
                    
            if (mapa[linha][coluna] == 23) or (mapa[linha][coluna] == 43) or (mapa[linha][coluna] == -23):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_cima.append(bloco)
                
            if (mapa[linha][coluna] == 24) or (mapa[linha][coluna] == 44) or (mapa[linha][coluna] == -24):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_esquerda.append(bloco)
                move_baixo.append(bloco)
                    
            if (mapa[linha][coluna] == 25) or (mapa[linha][coluna] == 45) or (mapa[linha][coluna] == -25):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_esquerda.append(bloco)
                move_baixo.append(bloco)
                move_cima.append(bloco)
                    
            if (mapa[linha][coluna] == 26) or (mapa[linha][coluna] == 46) or (mapa[linha][coluna] == -26):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_esquerda.append(bloco)
                move_cima.append(bloco)
                    
            if (mapa[linha][coluna] == 27) or (mapa[linha][coluna] == 47) or (mapa[linha][coluna] == -27):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_esquerda.append(bloco)
                move_baixo.append(bloco)
                    
            if (mapa[linha][coluna] == 28) or (mapa[linha][coluna] == 48) or (mapa[linha][coluna] == -28):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_esquerda.append(bloco)
                move_baixo.append(bloco)
                move_cima.append(bloco)
                    
            if (mapa[linha][coluna] == 29) or (mapa[linha][coluna] == 49) or (mapa[linha][coluna] == -29):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_esquerda.append(bloco)
                move_cima.append(bloco)
                
            if (mapa[linha][coluna] == 30) or (mapa[linha][coluna] == 50) or (mapa[linha][coluna] == -30):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_direita.append(bloco)
                move_esquerda.append(bloco)
                    
            if (mapa[linha][coluna] == 31) or (mapa[linha][coluna] == 51) or (mapa[linha][coluna] == -31):
                bloco = Rect(coluna*24,linha*24,24,24)
                move_baixo.append(bloco)
                move_cima.append(bloco)


#escolhe o mapa
mapa = escolhe_mapa(fase)
#cria os rect do mapa
mapa_rect(mapa)


while fim_jogo == False:    
    tela.fill((0,0,0))

#    ______
#___/ Mapa \______________________________________________    
       
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):           
            
            if (mapa[linha][coluna] > 20) and (mapa[linha][coluna] < 40):                
                tela.blit(p18, (coluna*24,linha*24))                               
                bloco = Rect((coluna*24)+12,(linha*24)+12,1,1)
                
                #Enquanto pac nao colidir com a pastilha, ela e blitada.
                if bloco not in pastilha_comida:
                    tela.blit(p0, (coluna*24,linha*24)) 
                    pastilha.append(bloco)

            #super pastilha
            if (mapa[linha][coluna] > 40) and (mapa[linha][coluna] < 60):
                tela.blit(p18, (coluna*24,linha*24))
                bloco = Rect((coluna*24)+12,(linha*24)+12,1,1)
               
                #Enquanto pac nao colidir com a super_pastilha, ela e blitada.
                if bloco not in pastilha_comida:
                    
                    #Printa as 3 Fases da Super pastilha:
                    if super_p < 60:
                        tela.blit(p19, (coluna*24,linha*24))
                    if (super_p >= 60) and (super_p <= 120):
                        tela.blit(p20, (coluna*24,linha*24))
                    if (super_p >= 120) and (super_p <= 180):
                        tela.blit(p21, (coluna*24,linha*24))
                    if (super_p >= 180) and (super_p <= 240):
                        tela.blit(p20, (coluna*24,linha*24))

                    #reseta o contador da super pastilha
                    super_p += 1
                    if super_p > 240:
                        super_p = 0

                    #cria o rect da super pastilha
                    super_pastilha.append(bloco)
                
            if mapa[linha][coluna] == 1:
                tela.blit(p1, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 2:
                tela.blit(p2, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 3:                
                tela.blit(p3, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 4:
                tela.blit(p4, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 5:
                tela.blit(p5, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 6:
                tela.blit(p6, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 7:
                tela.blit(p7, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 8:
                tela.blit(p8, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 9:
                tela.blit(p9, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 10:
                tela.blit(p10, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 11:
                tela.blit(p11, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 12:
                tela.blit(p12, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 13:
                tela.blit(p13, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 14:
                tela.blit(p14, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 15:
                tela.blit(p15, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 16:
                tela.blit(p16, (coluna*24,linha*24))
                
            if mapa[linha][coluna] == 17:
                tela.blit(p17, (coluna*24,linha*24))            

            if mapa[linha][coluna] == 18:
                tela.blit(p19, (coluna*24,linha*24))             

                
              
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    
    #Setas
    pressed_keys = pygame.key.get_pressed()
    #Esquerda
    
    if pressed_keys[K_LEFT]:  
        for indice in move_esquerda:
            if pacman["rect"].contains(indice):                
                pacman["tecla"] = "esquerda"         
        
    #Direita
    elif pressed_keys[K_RIGHT]:
        for indice in move_direita:
            if pacman["rect"].contains(indice):
                pacman["tecla"] = "direita"        
        
    #Cima
    elif pressed_keys[K_UP]:
        for indice in move_cima:
            if pacman["rect"].contains(indice):                
                pacman["tecla"] = "cima" 
        
    #Baixo
    elif pressed_keys[K_DOWN]:
        for indice in move_baixo:
            if pacman["rect"].contains(indice):                
                pacman["tecla"] = "baixo" 
        
    #Movimentacao
    for indice in fantasmas:
        indice["laco"] += 1
        if (indice["lado_esquerdo"] == False) or (indice["lado_direito"] == False) or (indice["para_cima"] == False) or (indice["para_baixo"] == False):
            tecla_random(indice)
        if indice["laco"] == 25:
            tecla_random(indice)
            indice["laco"] = 0

    pac_morrendo()

    fantasma_fraco()
        
    #puxa as funcoes para executar as movimentacoes dos objetos (pac e fantasmas)
    
    if morrendo == False: #se o pac colidir com fantasma, para de executar seus movimentos e começa a printar ele morrendo
        direcao(pacman["tecla"],pacman)        
        direcao(fantasma["tecla"],fantasma)
        direcao(fantasma2["tecla"],fantasma2)
        direcao(fantasma3["tecla"],fantasma3)
        direcao(fantasma4["tecla"],fantasma4)  
        
        #print do pacman
        #Direita
        if ((pacman["cont"] == 0) or (pacman["cont"] == 1)) and (pacman["direita"] > 0) : tela.blit(pac_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 2) or (pacman["cont"] == 3)) and (pacman["direita"] > 0) : tela.blit(pac2_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 4) or (pacman["cont"] == 5)) and (pacman["direita"] > 0) : tela.blit(pac3_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 6) or (pacman["cont"] == 7)) and (pacman["direita"] > 0) : tela.blit(pac4_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 8) or (pacman["cont"] == 9)) and (pacman["direita"] > 0) : tela.blit(pac5_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 10) or (pacman["cont"] == 11)) and (pacman["direita"] > 0) : tela.blit(pac6_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 12) or (pacman["cont"] == 13)) and (pacman["direita"] > 0) : tela.blit(pac7_d, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 14) or (pacman["cont"] == 15)) and (pacman["direita"] > 0) : tela.blit(pac8_d, (pacman["rect"].x,pacman["rect"].y))

        #Esquerda
        if ((pacman["cont"] == 0) or (pacman["cont"] == 1)) and (pacman["esquerda"] > 0) : tela.blit(pac_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 2) or (pacman["cont"] == 3)) and (pacman["esquerda"] > 0) : tela.blit(pac2_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 4) or (pacman["cont"] == 5)) and (pacman["esquerda"] > 0) : tela.blit(pac3_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 6) or (pacman["cont"] == 7)) and (pacman["esquerda"] > 0) : tela.blit(pac4_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 8) or (pacman["cont"] == 9)) and (pacman["esquerda"] > 0) : tela.blit(pac5_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 10) or (pacman["cont"] == 11)) and (pacman["esquerda"] > 0) : tela.blit(pac6_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 12) or (pacman["cont"] == 13)) and (pacman["esquerda"] > 0) : tela.blit(pac7_e, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 14) or (pacman["cont"] == 15)) and (pacman["esquerda"] > 0) : tela.blit(pac8_e, (pacman["rect"].x,pacman["rect"].y))

        #Cima
        if ((pacman["cont"] == 0) or (pacman["cont"] == 1)) and (pacman["cima"] > 0) : tela.blit(pac_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 2) or (pacman["cont"] == 3)) and (pacman["cima"] > 0) : tela.blit(pac2_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 4) or (pacman["cont"] == 5)) and (pacman["cima"] > 0) : tela.blit(pac3_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 6) or (pacman["cont"] == 7)) and (pacman["cima"] > 0) : tela.blit(pac4_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 8) or (pacman["cont"] == 9)) and (pacman["cima"] > 0) : tela.blit(pac5_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 10) or (pacman["cont"] == 11)) and (pacman["cima"] > 0) : tela.blit(pac6_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 12) or (pacman["cont"] == 13)) and (pacman["cima"] > 0) : tela.blit(pac7_c, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 14) or (pacman["cont"] == 15)) and (pacman["cima"] > 0) : tela.blit(pac8_c, (pacman["rect"].x,pacman["rect"].y))

        #Baixo
        if ((pacman["cont"] == 0) or (pacman["cont"] == 1)) and (pacman["baixo"] > 0) : tela.blit(pac_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 2) or (pacman["cont"] == 3)) and (pacman["baixo"] > 0) : tela.blit(pac2_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 4) or (pacman["cont"] == 5)) and (pacman["baixo"] > 0) : tela.blit(pac3_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 6) or (pacman["cont"] == 7)) and (pacman["baixo"] > 0) : tela.blit(pac4_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 8) or (pacman["cont"] == 9)) and (pacman["baixo"] > 0) : tela.blit(pac5_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 10) or (pacman["cont"] == 11)) and (pacman["baixo"] > 0) : tela.blit(pac6_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 12) or (pacman["cont"] == 13)) and (pacman["baixo"] > 0) : tela.blit(pac7_b, (pacman["rect"].x,pacman["rect"].y))
        if ((pacman["cont"] == 14) or (pacman["cont"] == 15)) and (pacman["baixo"] > 0) : tela.blit(pac8_b, (pacman["rect"].x,pacman["rect"].y))
        
        if (pacman["direita"] == 0) and (pacman["esquerda"] == 0) and (pacman["cima"] == 0) and (pacman["baixo"] == 0):
            tela.blit(pacman_, (pacman["rect"].x,pacman["rect"].y))
        

    #Limites do movimento do pac na tela
    if pacman["rect"].x > (len(mapa[0])-1)*24:
        pacman["rect"].x = 0
    if pacman["rect"].x < 0:
        pacman["rect"].x = (len(mapa[0])-1)*24
    if pacman["rect"].y > (len(mapa)-1)*24:
        pacman["rect"].y = 0
    if pacman["rect"].y < 0:
        pacman["rect"].y = (len(mapa)-1)*24

    #Contador das imagens do pac
    if pacman["cont"] > 14:
        pacman["cont"] = 0   
    
    

    #Controle da Fruta
    laco += 1
    
    if laco == tempo: #Tempo: escolhido aleatoriamente
        fruta_random()
        fruta_rect()
    if laco > 100:
        if rect_fruta != None:        
            fruta_blit()         

    #Fantasma Blit    

    #Fantasma no seu estado normal
    for indice in fantasmas:
        #Direita
        if (indice["direita"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_direita, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_direita, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_direita, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_direita, (indice["rect"].x,indice["rect"].y))                

        elif (indice["direita"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_direita2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_direita2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_direita2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_direita2, (indice["rect"].x,indice["rect"].y))

        #Esquerda
        if (indice["esquerda"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_esquerda, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_esquerda, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_esquerda, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_esquerda, (indice["rect"].x,indice["rect"].y))

        elif (indice["esquerda"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_esquerda2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_esquerda2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_esquerda2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_esquerda2, (indice["rect"].x,indice["rect"].y))

        #Cima
        if (indice["cima"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_cima, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_cima, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_cima, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_cima, (indice["rect"].x,indice["rect"].y))

        elif (indice["cima"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_cima2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_cima2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_cima2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_cima2, (indice["rect"].x,indice["rect"].y))
        
        #Baixo
        if (indice["baixo"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_baixo, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_baixo, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_baixo, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_baixo, (indice["rect"].x,indice["rect"].y))

        elif (indice["baixo"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == False) and (morrendo == False):
            if indice == fantasma:
                tela.blit(vermelho_baixo2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma2:
                tela.blit(azul_baixo2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma3:
                tela.blit(laranja_baixo2, (indice["rect"].x,indice["rect"].y))
            elif indice == fantasma4:
                tela.blit(rosa_baixo2, (indice["rect"].x,indice["rect"].y))

    #Fantasma no estado vulneravel
    for indice in fantasmas:
        t = tempo_fantasma_vulneravel
        if ((t > 240) and (t < 260)) or ((t > 280) and (t < 300)) or ((t > 320) and (t < 340)) or ((t > 360) and (t < 380)) or ((t > 400) and (t < 420)):
            if (indice["direita"] > 0) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(olho_direita, (indice["rect"].x,indice["rect"].y))
                
            if (indice["esquerda"] > 0) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(olho_esquerda, (indice["rect"].x,indice["rect"].y))
                
            if (indice["cima"] > 0) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(olho_cima, (indice["rect"].x,indice["rect"].y))
                
            if (indice["baixo"] > 0) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(olho_baixo, (indice["rect"].x,indice["rect"].y))
                
        else:
            #Direita
            if (indice["direita"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_direita, (indice["rect"].x,indice["rect"].y))                

            elif (indice["direita"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_direita2, (indice["rect"].x,indice["rect"].y))

            #Esquerda
            if (indice["esquerda"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_esquerda, (indice["rect"].x,indice["rect"].y))

            elif (indice["esquerda"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_esquerda2, (indice["rect"].x,indice["rect"].y))

            #Cima
            if (indice["cima"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_cima, (indice["rect"].x,indice["rect"].y))
                

            elif (indice["cima"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_cima2, (indice["rect"].x,indice["rect"].y))
            
            #Baixo
            if (indice["baixo"] > 0) and (indice["cont"] <= 10) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_baixo, (indice["rect"].x,indice["rect"].y))

            elif (indice["baixo"] > 0) and (indice["cont"] >= 11 ) and (indice["fraco"] == True) and (morrendo == False):
                tela.blit(fraco_baixo2, (indice["rect"].x,indice["rect"].y))
        
        #Nao deixa o fantasma sair da tela
        if indice["rect"].x > (len(mapa[0])-1)*24:
            indice["rect"].x = 0
        if indice["rect"].x < 0:
            indice["rect"].x = (len(mapa[0])-1)*24
        if indice["rect"].y > (len(mapa[0])-1)*24:
            indice["rect"].y = 0
        if indice["rect"].y < 0:
            indice["rect"].y = (len(mapa[0])-1)*24

        #Contador de controle das imagens do fantasma
        indice["cont"] += 1
        if indice["cont"] == 22:
            indice["cont"] =0        

        #Vida Extra:
        if placar - extra >= 0:
            extra += 10000
            if pacman["vida"] < 3:
                pacman["vida"] += 1                
                vida_extra.play()


            
#    _______________
#___/ Barra Lateral \___________________________________________
            
    

    score = fonte.render("Pontuação:", True, (255,255,255))
    tela.blit(score,(500,135))
    
    pontuacao2 = fonte.render(str(placar), True, (255,255,255))
    tela.blit(pontuacao2,(500,150))

    stringvida = fonte.render("Vida:", True, (255,255,255))
    tela.blit(stringvida,(500,185))
    
    if pacman["vida"] >= 1:
        tela.blit(vida,(500,200))
    if pacman["vida"] >= 2:
        tela.blit(vida,(515,200))
    if pacman["vida"] >= 3:
        tela.blit(vida,(530,200))

    pastilha_restante = fonte.render("Pastilhas:", True, (255,255,255))
    restante = fonte.render(str(len(pastilha)), True, (255,255,255))
    tela.blit(pastilha_restante,(500,235)) 
    tela.blit(restante,(500,250))

    if (fraco == True) and (tempo_fantasma_vulneravel > 0) and (tempo_fantasma_vulneravel <= 420):
        tela.blit(fraco_direita,(500,350))
        if quantidade_fantasma_comido == 0:
            nota = fonte.render("0", True, (255,255,255))
        if quantidade_fantasma_comido == 1:
            nota = fonte.render("200", True, (255,255,255))
        if quantidade_fantasma_comido == 2:
            nota = fonte.render("400", True, (255,255,255))
        if quantidade_fantasma_comido == 3:
            nota = fonte.render("800", True, (255,255,255))
        if quantidade_fantasma_comido == 4:
            nota = fonte.render("1600", True, (255,255,255))
        tela.blit(nota,(530,356))    
        
#     ______________
#____/ Morte do Pac \_____________________________________________

    if morrendo == True:
        #simula a morte do pacman

        #Para todos os Sons
        vida_extra.stop()
        som_super_pastilha.stop()
        
        relogio.tick(5)
        if morrendo_laco == 1:
            
            #som é colocado nesse if para executar apenas 1 vez
            musica = pygame.mixer.music.load("sons/pac_morte.wav")
            pygame.mixer.music.play(0)
            
            tela.blit(morte1, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 2:
            tela.blit(morte2, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 3:
            tela.blit(morte3, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 4:
            tela.blit(morte4, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 5:
            tela.blit(morte5, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 6:
            tela.blit(morte6, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 7:
            tela.blit(morte7, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 8:
            tela.blit(morte8, (pacman["rect"].x,pacman["rect"].y))
        if morrendo_laco == 9:
            tela.blit(morte9, (pacman["rect"].x,pacman["rect"].y))

        morrendo_laco += 1
        if morrendo_laco > 10:                   
            
            zerador_objeto() #faz retornar os fantasma e o pac a origem      
            pacman["vida"] -= 1 #retira 1 vida do pac

            morrendo = False
            morrendo_laco = 1

        if pacman["vida"] < 0:
            fim_jogo = True   

#    ______
#___/ Tela \_____________________________________________________

    #Relogio
    relogio.tick(75)
    
    pygame.display.update() #Atualiza tela
    
#    ____________ 
#___/ Introduçao \________________________________________________

# introdução é feita abaixo da atualização de tela caso contrario
# a tela continua preta

    if intro == True:       
        musica = pygame.mixer.music.load("sons/intro.wav")
        pygame.mixer.music.play(0)
        pygame.time.delay(4400)
        intro = False

    
#    _______________
#___/ Troca de fase \_____________________________________________
    
    if (len(pastilha) == 0):

        if (fase == 5) and (fase_final == True ): #Se for a ultima fase o jogo é finalizado
            fim_jogo = True

        if fim_jogo == False:
            fase += 1
            zerador()
            mapa = escolhe_mapa(fase)
            mapa_rect(mapa)
            
            zerador_objeto() #faz retornar os fantasma e o pac a origem

            intro = True
        
        #Para todos os Sons
        vida_extra.stop()
        som_super_pastilha.stop()

    if (fase == 5) and (laco == 100):
        fase_final = True

    
        
    #Ao resetar as listas remove-se as pastilhas que foram colididas com o pac
    pastilha = []
    super_pastilha = []
    
    

#Fim do laco

#    __________
#___/ Recordes \_____________________________________________

while fim_jogo == True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()
            pygame.quit()
        if evento.type == KEYDOWN:
            if evento.key == K_RETURN:
                exit()
                pygame.quit()
            
    arquivo = open("recorde.txt","r")
    placar_antigo = int(arquivo.readline())

    if placar > placar_antigo:
        arquivo = open("recorde.txt","w")
        arquivo.write(str(placar))
        arquivo.close()

    fonte =  pygame.font.SysFont('Comics Sans', 50)
    placar_final = fonte.render((str(placar)), True, (255,255,255))
    tela.blit(fim, (0,0))
    tela.blit(placar_final, (250,220))

    pygame.display.update()
