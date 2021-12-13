import pygame as pg

TITLE = "게임시작, 게임오버"

WIDTH = 600
HEIGHT = 600

FPS = 60

FONT_NAME = 'arial'


BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255, 255, 255)
player_health = 300


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # 게임화면 크기 설정
        pg.display.set_caption(TITLE) # 게임 창의 이름 설정
        self.clock = pg.time.Clock() # 게임 속도 조절에 사용 (프레임)
        self.running = True # 게임이 실행중인지 저장
        self.font_name = pg.font.match_font(FONT_NAME)
        


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS) # 게임 프레임 설정
            self.events()
            self.draw() 

    def events(self):
        self.clock.tick(FPS)
        self.screen.fill(BLACK)
        global player_health

        pg.draw.rect(self.screen, RED,(150, 450, 300, 10)) #직사각형 만드는 함수 #(X, Y, width, height)
        pg.draw.rect(self.screen, GREEN,(150, 450, player_health, 10))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: #(마우스 좌클릭) 체력 감소
               player_health -= 20

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3: #(마우스 우클릭) 체력 증가
               player_health += 20

            if player_health > 300:
                player_health = 300

            if player_health == 0:
                self.playing = False

            

        
           
    def draw(self):
        pg.display.update() # 화면 업데이트
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
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
    # 아무키나 눌렀다 때면 waiting이 False가 되고, 그 전까지는 무한루프


    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BLACK)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Arrows to move, Space to jump",
                       22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press any key to play",
                       22, WHITE, WIDTH/2, HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running: 
            return
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Press any key to play again",
                       22, WHITE, WIDTH/2, HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()


g = Game()
g.show_start_screen()

while g.running:
    g.run()
    player_health = 300
    g.show_go_screen()
    
pg.quit()


