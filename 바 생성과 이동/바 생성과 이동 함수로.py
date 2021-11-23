import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 640 # 화면가로 크기  가로:640
screen_height = 480 # 화면세로 크기  세로:480

screen = pygame.display.set_mode((screen_width, screen_height))  #스크린 크기 설정

# 화면 타이틀(제목) 설정
pygame.display.set_caption("bar move") #게임 이름

#캐릭터,배경 설정
background = pygame.image.load("C:\방준우 로컬디스크c\Bg.png")  #원본배경 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
character=pygame.image.load("C:\방준우 로컬디스크c\zoom_bg.jpg")  #원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
character_width,character_height=60,120           #캐릭터 가로,세로  설정   가로:60  세로:120
real_char=pygame.transform.scale(character,(60,120))   #원본캐릭터에서에서 원하는 크기로 커스텀
real_bg=pygame.transform.scale(background,(640,480))   #원본배경에서 원하는 크기로 커스텀

def barmove():
    xpos=screen_width-character_width    #캐릭터의 x좌표위치
    ypos=screen_height-character_height   #캐릭터의 y좌표위치
    to_x = 0       #캐릭터가 x좌표로 이동하는 정도
    to_y = 0       #캐릳터가 y 좌표로 이동하는 정도
    character_speed=0.5 #캐릭터의 속도


    clock=pygame.time.Clock()   #게임의 프레임을 맞추기 위한 변수



#pygame에서는 이벤트 루프가 있어야 창이 꺼지지않음
# 이벤트 루프
    running = True # 게임이 진행중인지 확인하기


    while running:
    
#pygame에서는 이벤트 루프가 있어야 창이 꺼지지않음
# 이벤트 루프
    
        dt=clock.tick(60)   #게임의 프레임을 60프레임 으로 설정


        for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
            if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
                running = False # 게임이 진행중이 아님



            if event.type ==pygame.MOUSEBUTTONDOWN: #마우스가 눌렸는지
                if event.button == 4:   #마우스휠 올리기
                    to_y = -character_speed #캐릭터를 위로 캐릭터의 속도만큼 올리기




                if event.button == 5:    #마우스휠내리기
                    to_y = +character_speed #캐릭터를 아래로 캐릭터의 속도만큼 내리기



#경계설정
        if ypos < 0:        #캐릭터가 창을 넘어가려 하면 멈춤
            ypos = 0


        elif ypos > screen_height - character_height:   #캐릭터가 창을 넘어가려하면 멈춤
            ypos= screen_height - character_height




        xpos += to_x * dt  # 캐릭터의 포지션을 x만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
        ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임

        screen.blit(real_bg, (0, 0))  # 배경 그리기(background 가 표시되는 위치)
        screen.blit(real_char, (xpos, ypos))  #캐릭터 그리기

        pygame.display.update() # 게임화면을 지속적으로 그리기(for문도는동안 계속)

# pygame 종료
barmove()
pygame.quit()


