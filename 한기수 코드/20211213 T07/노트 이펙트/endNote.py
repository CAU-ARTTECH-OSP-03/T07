import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 320))

background=pygame.Surface((screen.get_rect().width, screen.get_rect().height))
background.fill((0, 0, 0))

noteF = pygame.image.load("Deemo_long.png")
noteF = noteF.convert_alpha()
rectNoteF = noteF.get_rect()
#rectNoteF.y = 740
alpha = 255



#프레임 설정
clock = pygame.time.Clock()

def endNote():
    #if 노트가 판정선 만났을 때
    #if event.type ==pygame.MOUSEBUTTONDOWN:
        #판정선 위치에서 break이펙트
    #else:
    global alpha
    # rectNoteF.y = rectNote[i].y  # 시작하는 위치를 맞춰야하는데
    noteF.set_alpha(alpha)
    rectNoteF.x += 5
    alpha -= 10
    if alpha == 0:
        return





run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    endNote()

    screen.fill((255, 255, 255))
    screen.blit(background, background.get_rect())
    screen.blit(noteF, rectNoteF)

    pygame.display.update()  # 프레임마다 게임 화면 그려주기
    clock.tick(60) #60 frames per sec

pygame.quit()
sys.exit()

