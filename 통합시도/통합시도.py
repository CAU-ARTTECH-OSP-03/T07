import pygame
from pygame.rect import*
import random

#변수
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
move = Rect(0,0,0,0)
delay = 0
verdict = False #판정 시작 종료를 True False로 했습니다. 스페이스바를 누르면 True로 바뀌고 함수 실행후 Flase

#바 생성
bar=pygame.image.load("bar.png")  #원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
bar_width,bar_height=30,160           #캐릭터 가로,세로  설정   가로:60  세로:120
real_char=pygame.transform.scale(bar,(30,160))   #원본캐릭터에서에서 원하는 크기로 커스텀
xpos= 720    #바의 x좌표위치
ypos= SCREENHEIGHT/2- bar_height/2 #바의 y좌표위치
to_y = 0   #바가 y 좌표로 이동하는 정도
bar_speed=0.5 #바의 속도



#노트생성
note = [pygame.image.load('Deemo_long.png') for i in range(13)] # 노트 수
rectNote = [None for i in range(len(note))]

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
    if delay > 200: # 노트생성 딜레이 ex) 100 = 1000ms
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
        if rectNote[i].x > 800: #판정선 너머로 지나가면
            rectNote[i].x = -607 
            rectNote[i].y = random.randint(0, SCREENHEIGHT - 100)  #오른쪽 끝으로 넘어가면 노트가 다시 랜덤 y 좌표  부터 시작
        if rectNote[i].x == -1:
            continue

        rectNote[i].x += 5#노트속도

        SCREEN.blit(note[i], rectNote[i])

#판정 def

def judge():
    if verdict:
       if 740 > rectNote[i].x > 700: #판정 범위
            if ypos - 50 > rectNote[i].y + 50 > ypos + 210: #노트 높이 = 100, 바높이 = 160 
               rectNote[i].x = -random.randint(607, 809)
               rectNote[i].y = random.randint(0, SCREENHEIGHT - 100) #왼쪽 랜덤 좌표로 이동
               #여기에 점수증가, 체력증가
               #같은 형식으로 여러개 만들면 될 것같아요

               SCREEN.blit(note[i], rectNote[i])
    verdict = False

    





for i in range(len(note)): #노트생성을 pygame 기본 rect에 저장
    note[i] = pygame.transform.scale(note[i], (30, 100)) #노트 크기변화
    rectNote[i] = note[i].get_rect()
    rectNote[i].x = -1

#while문

while play:
    dt=clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type ==pygame.MOUSEBUTTONDOWN: #마우스가 눌렸는지
            if event.button == 4:   #마우스휠 올리기
                to_y = -bar_speed #캐릭터를 위로 캐릭터의 속도만큼 올리기
            if event.button == 5:    #마우스휠내리기
                to_y = +bar_speed #캐릭터를 아래로 캐릭터의 속도만큼 내리기
        if event.type ==pygame.KEYDOWN and event.key ==pygame.K_SPACE: #스페이스바를 누르면 judge함수 실행
            verdict = True
            



    if ypos < 0:        #캐릭터가 창을 넘어가려 하면 멈춤
            ypos = 0


    elif ypos > SCREENHEIGHT - bar_height:   #캐릭터가 창을 넘어가려하면 멈춤
            ypos= SCREENHEIGHT - bar_height

    ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
    #화면지우기
    SCREEN.fill((0, 0, 0))

  

    makeNote() #노트 생성
    moveNote() #노트 이동
    judge() # 노트 판정

    SCREEN.blit(line, (line_x_pos, line_y_pos))
    SCREEN.blit(real_char, (xpos, ypos))  #캐릭터 그리기

    pygame.display.flip()

pygame.quit()