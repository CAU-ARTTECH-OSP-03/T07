import pygame


pygame.init()


size = [900,400]
screen = pygame.display.set_mode(size)

title = 'My game'
pygame.display.set_caption(title)


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
ddrnote.x = size[0]/2 - ddrnote.sx/2
ddrnote.y = size[1]/2 - ddrnote.sy/2
ddrnote.move = 15

left_go = False
right_go = False

color = (0, 0, 0)



SB = 0
while SB == 0:

    
    clock.tick(60)

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False

                


    
    if left_go == True:
       ddrnote.x -= ddrnote.move
       if ddrnote.x <= 0:
           ddrnote.x = 0
    elif right_go == True:
        ddrnote.x += ddrnote.move
        if ddrnote.x >= size[0] - ddrnote.sx:
            ddrnote.x = size[0] - ddrnote.sx


    
    screen.fill(color)
    ddrnote.show()

  
    pygame.display.flip()


pygame.quit()

