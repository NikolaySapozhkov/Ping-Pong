from pygame import *
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, sprite_width, sprite_height):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (sprite_width, sprite_height))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    #класс-наследник для спрайта-игрока (управляется стрелками)
class Bat(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
#класс-наследник для спрайта-врага (перемещается сам)
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sprite_width, sprite_height):
            super().__init__(player_image, player_x, player_y, player_speed, sprite_width, sprite_height)
    def update(self):

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("field.png"), (win_width, win_height))

player1 = Bat('Rocket.png', 10, 200 , 4, 20, 100)
player2 = Bat('Rocket.png', 670, 200 , 4, 20, 100)
ball = Ball('ball.png', 340, 240, 5, 20, 20)

run = True
endgame = False
clock = time.Clock()
FPS = 60
#музыка
font.init()
font = font.SysFont("Arial", 25)
win = font.render("WIN!", True, (255, 255, 255))
lose = font.render("LOSE!", True, (255, 255, 255))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0, 0))

    if endgame != True:
        keys = key.get_pressed()
    

    player1.update()    
    player1.reset()
    player2.update()    
    player2.reset()
    ball.update()
    ball.reset()
    display.update()
    clock.tick(FPS)
    