import pygame

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((600,600))

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

player_health = 300

run = True
while run:
    clock.tick(60)
    display.fill(BLACK)

    pygame.draw.rect(display, RED,(150, 450, 300, 10)) #직사각형 만드는 함수 #(X, Y, width, height)
    pygame.draw.rect(display, GREEN,(150, 450, player_health, 10))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
           

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #(마우스 좌클릭) 체력 감소
            player_health -= 20

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #(마우스 우클릭) 체력 증가
            player_health += 20

        if player_health > 300:
            player_health = 300

        if player_health == 0:
            run = False

    pygame.display.update()


pygame.quit()
