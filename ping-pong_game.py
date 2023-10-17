#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, images, rx, ry, a, b, speed):
        super().__init__()
        self.image = transform.scale(image.load(images), (a ,b))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rx
        self.rect.y = ry
        self.a = a
        self.b = b
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<345:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<345:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('поля.png'),(700, 500))

rocket = GameSprite('цыганский мяч.png', 320, 220, 50, 50, 4)
p1 = Player('плётфорка_л.png', 5, 10, 50, 150, 4)
p2 = Player('плётфорка_п.png', 645, 340, 50, 150, 4)


bullets = sprite.Group() 

game = True
finish = False

font.init()

font2 = font.SysFont('Arial', 70)
win1 = font2.render('Выиграл игрок №1 :)', True, (0, 255, 0))
win2 = font2.render('Выиграл игрок №2 :)', True, (0, 255, 0))

wx = 4
wy = 4

clock = time.Clock()
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
                



    if finish != True:
        window.blit(background, (0, 0))

        rocket.reset()
        rocket.rect.x += wx
        rocket.rect.y -= wy

        if rocket.rect.y <= 5 or rocket.rect.y >= 445:
            wy = wy * -1
        if sprite.collide_rect(p1, rocket) or sprite.collide_rect(p2, rocket):
            wx = wx * -1
        if rocket.rect.x >= 650:
            finish = True
            window.blit(win1, (80, 200))
        if rocket.rect.x <= 0:
            finish = True
            window.blit(win2, (80,200)) 

        p1.reset()
        p2.reset()
        p1.update_r()
        p2.update_l()

    display.update()
    clock.tick(60)