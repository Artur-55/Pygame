import pygame
from pygame.locals import *
from sys import exit


def tabuleiro():
    pygame.draw.line(display, (255, 255, 255), (200, 0), (200, 600), 5)
    pygame.draw.line(display, (255, 255, 255), (400, 0), (400, 600), 5)
    pygame.draw.line(display, (255, 255, 255), (0, 200), (600, 200), 5)
    pygame.draw.line(display, (255, 255, 255), (0, 400), (600, 400), 5)

def peca(pos):
    global turno
    x, y = pos
    if turno == 'jogador2':
        img1 = pygame.image.load('Marca.O.png').convert_alpha()
        imgR1 = pygame.transform.scale(img1, (100, 100))
        display.blit(imgR1, (x - 50, y - 50))

    else:
        img2 = pygame.image.load('Marca.X.jpg').convert_alpha()
        imgR2 = pygame.transform.scale(img2, (100, 100))
        display.blit(imgR2, (x - 50, y - 50))

def pos():
    for p in rect:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(pos_mouse):
            if p == rect1:
                confirm(0, [100, 100])
            if p == rect2:
                confirm(1, [300, 100])
            if p == rect3:
                confirm(2, [500, 100])
            if p == rect4:
                confirm(3, [100, 300])
            if p == rect5:
                confirm(4, [300, 300])
            if p == rect6:
                confirm(5, [500, 300])
            if p == rect7:
                confirm(6, [100, 500])
            if p == rect8:
                confirm(7, [300, 500])
            if p == rect9:
                confirm(8, [500, 500])

def confirm(indice, pos):
    global escolha, turno, espaco
    if marcacao[indice] == 'X':
        print('X')
    elif marcacao[indice] == 'O':
        print('O')
    else:
        marcacao[indice] = escolha
        peca(pos)
        print(marcacao)
        if turno == 'jogador1':
            turno = 'jogador2'
        else:
            turno = 'jogador1'
        espaco = espaco + 1

def cond_vitoria(l):
    return ((marcacao[0] == l and marcacao[1] == l and marcacao[2] == l) or
            (marcacao[3] == l and marcacao[4] == l and marcacao[5] == l) or
            (marcacao[6] == l and marcacao[7] == l and marcacao[8] == l) or
            (marcacao[0] == l and marcacao[3] == l and marcacao[6] == l) or
            (marcacao[1] == l and marcacao[4] == l and marcacao[7] == l) or
            (marcacao[2] == l and marcacao[5] == l and marcacao[8] == l) or
            (marcacao[0] == l and marcacao[4] == l and marcacao[8] == l) or
            (marcacao[2] == l and marcacao[4] == l and marcacao[6] == l))

def vitoria(j):
    fonte = pygame.font.SysFont('times new roman', 50)
    msg = 'O Jogador {} foi o Vencedor'.format(j)
    if j == 'empate':
        msg_vitoria = fonte.render('Empatou... Deu Velha', True, (255, 255, 255), 0)
        display.blit(msg_vitoria, (85, 265))
    else:
        msg_vitoria = fonte.render(msg, True, (0, 255, 255), 0)
        display.blit(msg_vitoria, (20, 265))

def reset():
    global escolha, turno, estado, marcacao, espaco
    estado = 'jogando'
    turno = 'jogador1'
    escolha = 'X'
    espaco = 0
    marcacao = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
    ]
    display.fill(0)

pygame.init()


display = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Jogo da Velha')

icone = pygame.image.load('Icone.png')
pygame.display.set_icon(icone)

estado = 'jogando'
turno = 'jogador1'
escolha = 'X'
espaco = 0
marcacao = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200, 200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

rect = [
    rect1, rect2, rect3,
    rect4, rect5, rect6,
    rect7, rect8, rect9,
]

while True:
    pos_mouse = pygame.mouse.get_pos()
    if estado == 'jogando':
        tabuleiro()

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                if turno == 'jogador1':
                    escolha = 'X'
                    pos()
                else:
                    escolha = 'O'
                    pos()
        if cond_vitoria('X'):
            print('Vencedor: Jogador 1')
            vitoria('1')
            estado = 'reset'
        elif cond_vitoria('O'):
            print('Vencedor: Jogador 2')
            vitoria('2')
            estado = 'reset'
        elif espaco >= 9:
            print('Empatou')
            vitoria('empate')
            estado = 'reset'

    else:
        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
                reset()
                tabuleiro()
    pygame.display.flip()