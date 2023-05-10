from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=70, height=70):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed


width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Pin_pong')
window.fill((130, 100, 200))
clock = time.Clock()
# background = transform.scale(image.load(''), (width, height))
font.init()
font = font.Font(None, 44)
lose1 = font.render("PLAYER 1 LOOSE", True, (255, 0, 0))
lose2 = font.render("PLAYER 2 LOOSE", True, (255, 0, 0))


raket1 = Player('platform_v.png', 25, 150, 3, 25, 70)
raket2 = Player('platform_v.png', 650, 150, 3, 25, 70)
ball = GameSprite('football.png', 250, 150, 3, 50, 50)

game = True
finish = False
speed_x = 3
speed_y = 3

while game:
    # window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((130, 100, 200))
        raket1.update_l()
        raket2.update_r()

        ball.reset()
        raket1.reset()
        raket2.reset()

        ball.rect.x += speed_x
        ball.rect.y -= speed_y

    if ball.rect.y <= 0 or ball.rect.y >= 500-50:
        speed_y *= -1

    if sprite.collide_rect(ball, raket1) or sprite.collide_rect(ball, raket2):
        speed_x *= -1

    if ball.rect.x <= 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x >= 650:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()
    clock.tick(60)