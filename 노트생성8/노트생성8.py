import pygame
from pygame.rect import*
import random

#변수
play = True
SCREENWIDTH = 800
SCREENHEIGHT = 400
move = Rect(0,0,0,0)
time1000ms = 0

#스크린생성
pygame.init()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('노트랜덤생성')

#시간def
clock = pygame.time.Clock()

def timeUpdate1000ms(): # 노트생성 딜레이
    global time1000ms
    time1000ms += 1
    if time1000ms > 5:
        time1000ms = 0
        return True
    return False


#노트생성def

def makeNote():
    if timeUpdate1000ms():
        idex = random.randint(0, len(note)-1)
        if rectNote[idex].x == -1:
            rectNote[idex].y = random.randint(0, SCREENHEIGHT - 100)
            rectNote[idex].x = 0 #x가 0일때 시작하기
#노트이동def
def moveNote():
    makeNote()

    for i in range(len(note)):
        if rectNote[i].x == -1:
            continue

        rectNote[i].x += 5 #노트속도
        if rectNote[i].x > SCREENWIDTH:
            rectNote[i].x = -30 #오른쪽 끝으로 넘어가면 노트가 다시 x좌표 -30 부터 시작
        SCREEN.blit(note[i], rectNote[i])

#노트생성
note = [pygame.image.load('Deemo_long.png') for i in range(40)] # 노트 수
rectNote = [None for i in range(len(note))]
for i in range(len(note)):
    note[i] = pygame.transform.scale(note[i], (30, 100))
    rectNote[i] = note[i].get_rect()
    rectNote[i].x = -1

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    #화면지우기
    SCREEN.fill((0, 0, 0))

    makeNote()
    moveNote()

    pygame.display.flip()
    clock.tick(100)    

pygame.quit()