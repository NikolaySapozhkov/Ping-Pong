from pygame import *
#класс-родитель для 

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
    def __init__(self, player_image, player_x, player_y, player_speed, sprite_width, sprite_height):
        super().__init__(player_image, player_x, player_y, player_speed, sprite_width, sprite_height)
#класс-наследник для спрайта-врага (перемещается сам) 

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sprite_width, sprite_height):
        super().__init__(player_image, player_x, player_y, player_speed, sprite_width, sprite_height)
        self.x_speed = 3
        self.y_speed = 3
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.y >= 500:   
            self.y_speed *= -1
        if self.rect.y <= 0:
            self.y_speed *= -1
            
player1 = Bat('Rocket.png', 10, 200 , 4, 20, 100)
player2 = Bat('Rocket.png', 670, 200 , 4, 20, 100)
ball = Ball('ball.png', 340, 240, 5, 20, 20)

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
font = font.Font(None, 25)
player1Win = font.render("Player1 WIN!", True, (255, 255, 255))
player2Win = font.render("Player2 WIN!", True, (255, 255, 255))   
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0, 0))

    if endgame != True:
        keys = key.get_pressed()
        if keys[K_UP] and player1.rect.y > 0:
            player1.rect.y -= player1.speed
        if keys[K_DOWN] and player1.rect.y < 400:
            player1.rect.y += player1.speed
        if keys[K_w] and player2.rect.y > 0:
            player2.rect.y -= player2.speed
        if keys[K_s] and player2.rect.y < 400:
            player2.rect.y += player2.speed
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        ball.x_speed *= -1

    if ball.rect.x >= 700:
        endgame = True
        window.blit(player1Win, (290, 230))
    if ball.rect.x <= 0:
        endgame = True
        window.blit(player2Win, (290, 230))
    

      
    player1.reset()      
    player2.reset()
    ball.update()
    ball.reset()
    display.update()
    clock.tick(FPS)
    