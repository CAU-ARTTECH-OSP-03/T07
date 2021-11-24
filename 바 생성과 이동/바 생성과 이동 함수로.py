import pygame

pygame.init()  # 초기화

play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
move = pygame.rect.Rect(0, 0, 0, 0)
delay = 0

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('노트랜덤생성')

# 바 생성

bar_image = pygame.image.load("bar.png")  # 원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
bar_width, bar_height = 30, 160  # 캐릭터 가로,세로  설정   가로:60  세로:120
bar_real = pygame.transform.scale(bar_image, (30, 160))  # 원본캐릭터에서에서 원하는 크기로 커스텀
bar_xpos = 720  # 바의 x좌표위치
bar_ypos = SCREENHEIGHT / 2 - bar_height / 2  # 바의 y좌표위치
bar_to_y = 0  # 바가 y 좌표로 이동하는 정도
bar_speed = 0.5  # 바의 속도

clock = pygame.time.Clock()
dt = clock.tick(60)


def movebar():
    play = True
    bar_to_y = 0

    while play:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스가 눌렸는지
                if event.button == 4:  # 마우스휠 올리기
                    bar_to_y -= bar_speed

                # 캐릭터를 위로 캐릭터의 속도만큼 올리기

                if event.button == 5:  # 마우스휠내리기
                    bar_to_y += bar_speed  # 캐릭터를 아래로 캐릭터의 속도만큼 내리기
                else:
                    continue
        bar_ypos = SCREENHEIGHT / 2 - bar_height / 2

        bar_ypos += bar_to_y * dt

        if bar_ypos < 0:  # 캐릭터가 창을 넘어가려 하면 멈춤
            bar_ypos = 0


        elif bar_ypos > SCREENHEIGHT - bar_height:  # 캐릭터가 창을 넘어가려하면 멈춤
            bar_ypos = SCREENHEIGHT - bar_height

        SCREEN.fill((0, 0, 0))

        SCREEN.blit(bar_real, (bar_xpos, bar_ypos))  # 캐릭터 그리기

        pygame.display.flip()


movebar()

pygame.quit()


