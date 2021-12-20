import pygame
import sys

pygame.init() # 초기화 (필수)
screen = pygame.display.set_mode((640, 320)) # 화면 크기

background=pygame.Surface((screen.get_rect().width, screen.get_rect().height))
background.fill((0, 0, 0))

# 놓친 노트
noteF = pygame.image.load("노트 프로토.png")
noteF = noteF.convert_alpha()
rectNoteF = noteF.get_rect()
#rectNoteF.y = 740
alpha = 255

# 판정 노트
frame_index = 0
animation_speed = 0.25

Key = False

#프레임 설정
clock = pygame.time.Clock()



def endNoteF():
    global alpha
    # rectNoteF.y = rectNote[i].y  # 시작하는 위치를 맞춰야하는데
    noteF.set_alpha(alpha)
    if alpha <= 0:
        alpha = 255
        rectNoteF.x = 0
    if alpha > 0:
        alpha -= 10
        rectNoteF.x += 5

def import_character_assets(self):
    noteTs = [pygame.image.load("노트 프로토.png"),
              pygame.image.load("깨진 노트 프로토1.png"),
              pygame.image.load("깨진 노트 프로토2.png"),
              pygame.image.load("깨진 노트 프로토3.png"),
              pygame.image.load("깨진 노트 프로토4.png")]


def endNoteT():
    global frame_index
    global animation_speed
    global Key
    noteTs = [pygame.image.load("노트 프로토.png"),
              pygame.image.load("깨진 노트 프로토1.png"),
              pygame.image.load("깨진 노트 프로토2.png"),
              pygame.image.load("깨진 노트 프로토3.png"),
              pygame.image.load("깨진 노트 프로토4.png")]

    for i in range(len(noteTs)):
        image = noteTs[i]
        rect = image.get_rect()
        rect.x = 300
        rect.y = 150

    # loop over frame index
    if Key:
        frame_index += animation_speed
        if frame_index >= len(noteTs):
            frame_index = 0
            Key = False

        image = noteTs[int(frame_index)]

        screen.blit(image, rect)









run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(background, background.get_rect()) #배경이 먼저 깔려야 위에 bilt

    for event in pygame.event.get(): # (필수)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            Key = True


    endNoteF()
    endNoteT()




    screen.blit(noteF, rectNoteF)

    pygame.display.update()  # 프레임마다 게임 화면 그려주기 (필수)
    clock.tick(60) # 60 frames per sec

pygame.quit()
sys.exit()

