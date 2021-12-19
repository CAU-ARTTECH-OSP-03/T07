import pygame
from pygame.rect import*
import random

#변수
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
#move = Rect(0,0,0,0) (무슨 변수인지 몰라서 주석처리)
delay = 0




#시간def
clock = pygame.time.Clock()

#스크린생성
pygame.init()

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('통합')

# 바 생성
bar = pygame.image.load("bar.png")  # 원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
bar_width, bar_height = 20, 100  # 캐릭터 가로,세로  설정   가로:20  세로:100
real_char = pygame.transform.scale(bar, (20, 60))  # 원본캐릭터에서에서 원하는 크기로 커스텀
xpos = 730  # 바의 x좌표위치
ypos = (SCREENHEIGHT / 2) - (bar_height / 2)  # 바의 y좌표위치
to_y = 0  # 바가 y 좌표로 이동하는 정도
bar_speed = 0.5  # 바의 속도

#판정선 생성
line = pygame.image.load("line.png")
line_x_pos = 740
line_y_pos = 0

#노트생성
note = [pygame.image.load('노트 프로토.png') for i in range(33)] # 노트 수 # 리스트이다. (노트가 33개 들어가있는)
rectNote = [None for i in range(len(note))] # None을 note(리스트)의 길이 수 만큼 넣은 리스트

#노트생성을 pygame 기본 rect에 저장
for i in range(len(note)):
    note[i] = pygame.transform.scale(note[i], (60, 50)) #노트 크기변화
    rectNote[i] = note[i].get_rect()
    rectNote[i].x = -1



#노트생성 딜레이 def
def delayUpdate():
    global delay
    delay += 1
    if delay > 100: # 노트생성 딜레이 ex) 100 = 1000ms = 1s # 이 숫자를 줄이면 노트가 더 많이 쏟아짐
        delay = 0
        return True
    return False

#노트생성def
def makeNote():
    if delayUpdate():
        index = random.randint(0, len(note)-1) # 0에서 len(note)-1 까지 범위 중 랜덤으로 int 값을 index에 대입
        if rectNote[index].x == -1:
            rectNote[index].y = random.randint(0, SCREENHEIGHT - 100)
            rectNote[index].x = 0 #x가 0일때 시작하기


#노트이동def
def moveNote():
    makeNote()

    for i in range(len(note)):
        if rectNote[i].x > 708: #판정선 좌표 -20
            rectNote[i].x = -110  #오른쪽 끝으로 넘어가면 노트가 다시 x좌표 -110 부터 시작
        if rectNote[i].x == -1:
            continue

        rectNote[i].x += 5 #노트속도

        SCREEN.blit(note[i], rectNote[i])




# 놓친 노트 이펙트
noteF = pygame.image.load("노트 프로토.png")
#noteF = noteF.convert_alpha()
noteF_width, noteF_height = 30, 100
noteF = pygame.transform.scale(noteF, (60, 50))  # 노트 크기변화
rectNoteF = noteF.get_rect()
rectNoteF.x = 740 - noteF_width / 2  # 이펙트가 발생하는 x좌표 고정
alpha = 255


# 판정 노트 이펙트
noteTs = [pygame.image.load("노트 프로토.png"),
          pygame.image.load("깨진 노트 프로토1.png"),
          pygame.image.load("깨진 노트 프로토2.png"),
          pygame.image.load("깨진 노트 프로토3.png"),
          pygame.image.load("깨진 노트 프로토4.png")]
for i in range(len(noteTs)):
    noteTs[i] = pygame.transform.scale(noteTs[i], (60, 50))  # 노트 크기변화
    image = noteTs[i]
    rectNoteT = image.get_rect()
    rectNoteT.x = 708
frame_index = 0
animation_speed = 0.5
key = False


# verdictBar 생성
verdictBar = pygame.image.load("투명.png")
verdictBar = pygame.transform.scale(verdictBar, (10, 50))
rectVerdictBar = verdictBar.get_rect()
rectVerdictBar.centerx = (720)
rectVerdictBar.centery = (SCREENHEIGHT / 2)

# 판정 def
def judge():
    endNoteT()
    #global score_value, player_health
    for rectN in rectNote:
        if rectN.x == -1:
            continue
        if rectN.top < rectVerdictBar.bottom and rectVerdictBar.top < rectN.bottom and rectN.left < rectVerdictBar.right and rectVerdictBar.left < rectN.right:  # 노트가 판정bar와 만날 때 체력 20과 점수 100을 올림
            rectN.x = -607
            rectN.y = random.randint(0, SCREENHEIGHT - 100)
            #player_health += 20
            #score_value += 100
            break


## 노트 판정 이펙트 # 작동안함
#def endNote():  # 지나가는 노트
#    global key
#    ##   if verdict: # 노트를 쳤을 때 이펙트
#    if key is False and rectNote[i].x < -1:  # 반응 없이 지나치는 경우 (투명도 조절)
#        global alpha
#        rectNoteF.y = 150  # 시작하는 위치를 맞춰야하는데
#        noteF.set_alpha(alpha)
#        rectNoteF.x += 5
#        alpha -= 10
#        if alpha == 0:
#            return

def endNoteT():  # 부서지는 노트
    global frame_index
    global animation_speed
    global key

    rectNoteT.y = ypos + 5  # 노트의 y좌표 받는 게 관건일 것 같아요

    # loop over frame index
    if key is True:
        frame_index += animation_speed
        if frame_index >= len(noteTs):
            frame_index = 0
            key = False

        image = noteTs[int(frame_index)]

        SCREEN.blit(image, rectNoteT)


#while문

while play:
    #player_health = 300
    to_y = 0
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스가 눌렸는지
            if event.button == 4:  # 마우스휠 올리기
                to_y = -bar_speed  # 캐릭터를 위로 캐릭터의 속도만큼 올리기
            if event.button == 5:  # 마우스휠내리기
                to_y = +bar_speed  # 캐릭터를 아래로 캐릭터의 속도만큼 내리기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 스페이스바를 누르면 judge함수 실행
                judge()
                key = True

    if ypos < 0:  # 캐릭터가 창을 넘어가려 하면 멈춤
        ypos = 0

    elif ypos > SCREENHEIGHT - bar_height:  # 캐릭터가 창을 넘어가려하면 멈춤
        ypos = SCREENHEIGHT - bar_height

    ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
    #화면지우기
    SCREEN.fill((0, 0, 0))
    #makeNote() #moveNote()에서 이미 이 함수를 재귀호출함
    moveNote()
    #endNote()  # 실행안됨
    endNoteT()
    judge()

    SCREEN.blit(line, (line_x_pos, line_y_pos))
    SCREEN.blit(real_char, (xpos, ypos))  # 캐릭터 그리기 # real_char는 바 이미지를 의미

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

