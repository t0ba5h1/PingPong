from pygame import *
from random import randint


#основной класс Sprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс для игрока    
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed




#класс для врага
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0, 600)
            self.speed = randint(1,3)
            lost += 1

img_back = '03b16f9acac46c4b31d235a34383372a.jpg'
img_player = 'rocket.png'
img_ball = 'ball.png'

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
display.set_caption('Ping-Pong')

game = True
finish = False

clock = time.Clock()
F_P_S = 60

rocket_l = Player(img_player, 30, 200, 20, 100, 5)
rocket_r = Player(img_player, 650, 200, 20, 100, 5)
ball = Enemy(img_ball, 350, 250, 50, 50, 5)

while game:
    

    for e in event.get():
        if e.type == QUIT:
            game = False

    #обновление экрана
    if finish != True:
        window.blit(background, (0,0))
        rocket_l.update_l()
        rocket_r.update_r()
        rocket_l.reset()
        rocket_r.reset()
        ball.reset()
    
        
        display.update()
    clock.tick(F_P_S)