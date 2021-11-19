#스페이스바가 게임 시작이라고 하면, 게임이 시작되고 나서 노트가 왼쪽에서 오른쪽으로 움직이도록 먼저 만듬.
#파이게임 창이 열리자마자 자동으로 노트가 움직이는 건 아직 모르겠습니다... 나중에 이 부분을 해결해야 할 것 같습니다..

import pygame

# 게임 초기화
pygame.init()

# 게임창 옵션 설정
size = [900,400]
screen = pygame.display.set_mode(size)

title = 'My game'
pygame.display.set_caption(title)

# 노트를 클래스로 구현
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, filename):
        if filename[-3:] == "png":
            self.img = pygame.image.load(filename).convert_alpha()
        else:
            self.img = pygame.image.load(filename)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img,(sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))


ddrnote = obj()
ddrnote.put_img("ddrnote.png")
ddrnote.change_size(80,80)
ddrnote.x = 0
ddrnote.y = size[1]/2 - ddrnote.sy/2
ddrnote.move = 15

color = (255, 255, 255)


right_go = False


# SB 가 0 일 동안에는 계속 파이게임 창이 켜져있고, X 버튼을 누르면 SB가 1이 되게 만들어서, 파이게임 창에서 나가도록 (루프 탈출) 구현
SB = 0
while SB == 0:

    # FPS 설정
    clock.tick(60)

    # 스페이스바 입력 감지 (스페이스바 = 시작 버튼)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_SPACE:
                right_go = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                right_go = True

                


    # 입력, 시간에 따른 노트의 변화
    
    if right_go == True:
        ddrnote.x += ddrnote.move
        if ddrnote.x >= size[0] - ddrnote.sx:
            ddrnote.x = size[0] - ddrnote.sx
    

    # 화면에 파이게임 창 그리기
    screen.fill(color)
    ddrnote.show()

    
    pygame.display.flip()

# 파이게임 창 종료
pygame.quit()

