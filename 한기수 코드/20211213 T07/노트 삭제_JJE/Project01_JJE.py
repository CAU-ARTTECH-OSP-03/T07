#일단은 임시로 노트의 좌표가 판정선의 좌표와 일치할 때 배경색으로 덮는 방식으로 했어요.
#서서히 사라지는 방법을 찾아보려 했는데 이미지 파일을 쓰면 또 달라서...
#노트를 다른 방식으로 생성해보던지 더 찾아봐야 할 것 같아요.
#그리고 이미지 파일이 제 컴퓨터 기준이라서... 이것도

import pygame

pygame.init()  # 초기화(필수)

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("OpenSource Project")

# 스프라이트 불러오기
character = pygame.image.load("C:\\Users\JEONG\Desktop\찌\예공대\오픈소스프로그래밍\Project\\note.png")
character_size = character.get_rect().size  # 이미지 사이즈
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 0
character_y_pos = (screen_height / 2) - (character_height / 2)


line = pygame.image.load("C:\\Users\JEONG\Desktop\찌\예공대\오픈소스프로그래밍\Project\line.png")
line_x_pos = 600
line_y_pos = 0

#프레임 설정
clock = pygame.time.Clock()

# 이벤트 루프 (프로그램이 종료되지 않도록 대기)
running = True
while running:  # 게임이 실행중
    for event in pygame.event.get():  # 어떤 이벤트?
        if event.type == pygame.QUIT:  # 창이 닫힘
            running = False
#Game logic start

    character_x_pos += 1 #move 1 pixel
    if character_x_pos == 520: #판정선이랑 만났을 때
        character.fill((0, 0, 0)) #배경색으로 채우기

    screen.fill((0, 0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) #blit 이미지 나타낼 때
    screen.blit(line, (line_x_pos, line_y_pos))
    pygame.display.update()  # 프레임마다 게임 화면 그려주기
    clock.tick(60) #60 frames per sec

# pygame 종료
pygame.quit()