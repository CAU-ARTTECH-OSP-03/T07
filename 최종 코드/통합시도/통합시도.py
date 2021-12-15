import pygame
from pygame.rect import *
import random
import pygame as pg
import sys

# 변수
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
move = Rect(0, 0, 0, 0)
delay = 0
score_x = 100  # 점수판 위치
score_y = 100
verdict = False  # 판정 시작 종료를 True False로 했습니다. 스페이스바를 누르면 True로 바뀌고 함수 실행후 Flase
TITLE = "게임시작, 게임오버"
FPS = 60


# 바 생성
bar = pygame.image.load("bar.png")  # 원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
bar_width, bar_height = 30, 160  # 캐릭터 가로,세로  설정   가로:60  세로:120
real_char = pygame.transform.scale(bar, (30, 160))  # 원본캐릭터에서에서 원하는 크기로 커스텀
xpos = 720  # 바의 x좌표위치
ypos = SCREENHEIGHT / 2 - bar_height / 2  # 바의 y좌표위치
to_y = 0  # 바가 y 좌표로 이동하는 정도
bar_speed = 0.5  # 바의 속도


# 노트생성
note = [pygame.image.load('노트 프로토.png') for i in range(13)]  # 노트 수
rectNote = [None for i in range(len(note))]
for i in range(len(note)):  # 노트생성을 pygame 기본 rect에 저장
    note[i] = pygame.transform.scale(note[i], (30, 100))  # 노트 크기변화
    rectNote[i] = note[i].get_rect()
    rectNote[i].x = -1


# 판정선 생성
line = pygame.image.load("line.png")
line_x_pos = 740
line_y_pos = 0


# 시간def
clock = pygame.time.Clock()


# 스크린생성
pygame.init()

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('노트랜덤생성')


# 점수판 세팅
score_value = 0  # 점수판 점수
font = pygame.font.Font("freesansbold.ttf", 30)  # 점수판 글씨 폰트


# 점수판 생성함수
def showscore(x, y):
    score = font.render("score:" + str(score_value), True, "red")
    SCREEN.blit(score, (x, y))


# 체력바, 게임 스타트, 오버
FONT_NAME = 'arial'
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
player_health = 300


# 놓친 노트 이펙트
noteF = pygame.image.load("노트 프로토.png")
noteF = noteF.convert_alpha()
noteF_width, noteF_height = 30, 100
noteF = pygame.transform.scale(noteF, (30, 100))  # 노트 크기변화
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
    noteTs[i] = pygame.transform.scale(noteTs[i], (30, 100))  # 노트 크기변화
    image = noteTs[i]
    rectNoteT = image.get_rect()
    rectNoteT.x = rectNoteF.x
frame_index = 0
animation_speed = 0.25


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # 게임화면 크기 설정
        pg.display.set_caption(TITLE)  # 게임 창의 이름 설정
        self.clock = pg.time.Clock()  # 게임 속도 조절에 사용 (프레임)
        self.play = True  # 게임이 실행중인지 저장
        self.font_name = pg.font.match_font(FONT_NAME)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)  # 게임 프레임 설정
            self.events()
            self.draw()

    def events(self):
        self.clock.tick(FPS)
        self.screen.fill(BLACK)
        global player_health

        pg.draw.rect(self.screen, RED, (150, 450, 300, 10))  # 직사각형 만드는 함수 #(X, Y, width, height)
        pg.draw.rect(self.screen, GREEN, (150, 450, player_health, 10))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.play = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # (마우스 좌클릭) 체력 감소
                player_health -= 20

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:  # (마우스 우클릭) 체력 증가
                player_health += 20

            if player_health > 300:
                player_health = 300

            if player_health == 0:
                self.playing = False

    def draw(self):
        pg.display.update()  # 화면 업데이트
        self.screen.fill(BLACK)

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.play = False
                if event.type == pg.KEYUP:
                    waiting = False

    # 아무키나 눌렀다 때면 waiting이 False가 되고, 그 전까지는 무한루프

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, WHITE, SCREENWIDTH / 2, SCREENHEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump",
                       22, WHITE, SCREENWIDTH / 2, SCREENHEIGHT / 2)
        self.draw_text("Press any key to play",
                       22, WHITE, SCREENWIDTH / 2, SCREENHEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.play:
            return
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 48, WHITE, SCREENWIDTH / 2, SCREENHEIGHT / 4)
        self.draw_text("Press any key to play again",
                       22, WHITE, SCREENWIDTH / 2, SCREENHEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()


g = Game()
g.show_start_screen()




def delayUpdate():  # 노트생성 딜레이 def
    global delay
    delay += 1
    if delay > 200:  # 노트생성 딜레이 ex) 100 = 1000ms
        delay = 0
        return True
    return False


# 노트생성def
def makeNote():
    if delayUpdate():
        index = random.randint(0, len(note) - 1)
        if rectNote[index].x == -1:
            rectNote[index].y = random.randint(0, SCREENHEIGHT - 100)
            rectNote[index].x = 0  # x가 0일때 시작하기


# 노트이동def
def moveNote():
    makeNote()

    for i in range(len(note)):
        if rectNote[i].x > 800:  # 판정선 너머로 지나가면
            rectNote[i].x = -607
            rectNote[i].y = random.randint(0, SCREENHEIGHT - 100)  # 오른쪽 끝으로 넘어가면 노트가 다시 랜덤 y 좌표  부터 시작
        if rectNote[i].x == -1:
            continue

        rectNote[i].x += 5  # 노트속도

        SCREEN.blit(note[i], rectNote[i])


# 판정 def
def judge():
    endNoteT() # 판정 이펙트

    global verdict
    if verdict == True:
        if 740 > rectNote[i].x > 700:  # 판정 범위
            if ypos - 50 > rectNote[i].y + 50 > ypos + 210:  # 노트 높이 = 100, 바높이 = 160
                rectNote[i].x = -random.randint(607, 809)
                rectNote[i].y = random.randint(0, SCREENHEIGHT - 100)  # 왼쪽 랜덤 좌표로 이동
                # 여기에 점수증가, 체력증가
                # 같은 형식으로 여러개 만들면 될 것같아요

                SCREEN.blit(note[i], rectNote[i])
    verdict = False


# 노트 판정 이펙트
def endNote():  # 지나가는 노트
    global verdict
    ##   if verdict: # 노트를 쳤을 때 이펙트
    if verdict == False:  # 반응 없이 지나치는 경우 (투명도 조절)
        global alpha
        rectNoteF.y = rectNote[i].y  # 시작하는 위치를 맞춰야하는데
        noteF.set_alpha(alpha)
        rectNoteF.x += 5
        alpha -= 10
        if alpha == 0:
            return

def endNoteT():  # 부서지는 노트
    global frame_index
    global animation_speed
    global verdict

    rectNoteT.y = 150  # 노트의 y좌표 받는 게 관건일 것 같아요

    # loop over frame index
    if verdict:
        frame_index += animation_speed
        if frame_index >= len(noteTs):
            frame_index = 0
            Key = False

        image = noteTs[int(frame_index)]

        SCREEN.blit(image, rectNoteT)



# while문


while play:
    player_health = 300
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스가 눌렸는지
            if event.button == 4:  # 마우스휠 올리기
                to_y = -bar_speed  # 캐릭터를 위로 캐릭터의 속도만큼 올리기
            if event.button == 5:  # 마우스휠내리기
                to_y = +bar_speed  # 캐릭터를 아래로 캐릭터의 속도만큼 내리기
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # 스페이스바를 누르면 judge함수 실행
            verdict = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                score_value += 1

            if event.key == pygame.K_LEFT:
                score_value -= 1

    if ypos < 0:  # 캐릭터가 창을 넘어가려 하면 멈춤
        ypos = 0


    elif ypos > SCREENHEIGHT - bar_height:  # 캐릭터가 창을 넘어가려하면 멈춤
        ypos = SCREENHEIGHT - bar_height

    ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
    # 화면지우기
    SCREEN.fill((0, 0, 0))
    g.run()
    g.show_go_screen()
    showscore(score_x, score_y)
    makeNote()  # 노트 생성
    moveNote()  # 노트 이동
    judge()  # 노트 판정

    SCREEN.blit(line, (line_x_pos, line_y_pos))
    SCREEN.blit(real_char, (xpos, ypos))  # 캐릭터 그리기

    pygame.display.flip()

pygame.quit()