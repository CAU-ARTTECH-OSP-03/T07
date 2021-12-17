import pygame
pygame.init()

#스크린 세팅
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
#점수판 위치
score_x=100
score_y=100
#점수판 세팅
score_value=0  #점수판 점수
font=pygame.font.Font("freesansbold.ttf",30) #점수판 글씨 폰트

#점수판 생성함수
def showscore(x, y):
    score = font.render("score:"+str(score_value), True, "red")
    SCREEN.blit(score,(x,y))






#루프문   일단 오른쪽키 누르면 점수+1, 왼쪽키 누르면 점수-1


while play:
    play = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                score_value+=1

            if event.key==pygame.K_LEFT:
                score_value-=1

    SCREEN.fill("black")
    showscore(score_x, score_y)



    pygame.display.flip()
