import pygame
from pygame.rect import*
import random

#변수
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
move = Rect(0,0,0,0)
delay = 0
#노트생성
note = [pygame.image.load('Deemo_long.png') for i in range(33)] # 노트 수
rectNote = [None for i in range(len(note))]

delNote1 = pygame.image.load('Deemo_long_1.png')
delNote2 = pygame.image.load('Deemo_long_2.png')
delNote3 = pygame.image.load('Deemo_long_3.png')
delNote4 = pygame.image.load('Deemo_long_4.png')
delNote5 = pygame.image.load('Deemo_long_5.png')

#스크린생성
pygame.init()

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('노트랜덤생성')

#판정선 생성
line = pygame.image.load("line.png")
line_x_pos = 740
line_y_pos = 0

#시간def
clock = pygame.time.Clock()


def delayUpdate(): #노트생성 딜레이 def
    global delay  
    delay += 1
    if delay > 100: # 노트생성 딜레이 ex) 100 = 1000ms
        delay = 0
        return True
    return False


#노트생성def


def makeNote():
    if delayUpdate():
        index = random.randint(0, len(note)-1)
        if rectNote[index].x == -1:
            rectNote[index].y = random.randint(0, SCREENHEIGHT - 100)
            rectNote[index].x = 0 #x가 0일때 시작하기
#노트이동def
def moveNote():

    makeNote()
    for i in range(len(note)):
        if rectNote[i].x > 720: #판정선 좌표 -20
            rectNote[i].x = -110  #오른쪽 끝으로 넘어가면 노트가 다시 x좌표 -110 부터 시작
        if rectNote[i].x == -1:
            continue
        if rectNote[i].x == 720:  # 어떻게든 사라지는 모습...
            delNote1_x = 720
            delNote1_x += 5

        rectNote[i].x += 5 #노트속도

        SCREEN.blit(note[i], rectNote[i])



for i in range(len(note)): #노트생성을 pygame 기본 rect에 저장
    note[i] = pygame.transform.scale(note[i], (30, 100)) #노트 크기면화
    rectNote[i] = note[i].get_rect()
    rectNote[i].x = -1

#while문

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    #화면지우기
    SCREEN.fill((0, 0, 0))

    makeNote()
    moveNote()

    SCREEN.blit(line, (line_x_pos, line_y_pos))

    pygame.display.flip()
    clock.tick(60)    

pygame.quit()