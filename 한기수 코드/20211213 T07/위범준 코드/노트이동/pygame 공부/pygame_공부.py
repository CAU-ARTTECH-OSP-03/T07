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


right_go = True


# SB 가 0 일 동안에는 계속 파이게임 창이 켜져있고, X 버튼을 누르면 SB가 1이 되게 만들어서, 파이게임 창에서 나가도록 (루프 탈출) 구현
SB = 0
while SB == 0:

    # FPS 설정
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
              
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

