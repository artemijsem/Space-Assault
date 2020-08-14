import pygame, sys, time, os
from pygame.locals import *

# int
LENGTH = 1280
WIDTH = 720
FPS = 30
P_YSide = 64  # half of the player's sprite in Y axis
FPSCLOCK = pygame.time.Clock()
BLACK = pygame.Color('black')
YELLOW = pygame.Color('yellow')
RED = pygame.Color('red')
StartXPos = LENGTH // 2
StartYPos = WIDTH - P_YSide
MOVERATE = 0
bullets = []
previous_time = pygame.time.get_ticks()
# images
player_img_path = os.path.join('C:\Games\Space Assault\Data\Sprites', 'player64.png')
bullet_img_path = os.path.join('C:\Games\Space Assault\Data\Sprites', 'Bullet.png')


# classes
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.state = "OFF"
        self.x = StartXPos + 64
        self.y = StartYPos - 32
        self.image = pygame.image.load(bullet_img_path)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, surface):
        if self.state == "ON":
            self.y -= 5
            surface.blit(self.image, (self.x, self.y))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(player_img_path)
        self.x = StartXPos
        self.y = StartYPos
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, surface):
        surface.blit(self.image, (self.x, self.y))


# object
Player1 = Player()
new_bullet = Bullet()
bullets = []

# main
pygame.init()
screen = pygame.display.set_mode((LENGTH, WIDTH))

# loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MOVERATE = -15
            if event.key == pygame.K_RIGHT:
                MOVERATE = 15
            if event.key == pygame.K_SPACE:
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > 500:
                    previous_time = current_time
                    bullets.append(Bullet())
                    new_bullet.state = "ON"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                MOVERATE = 0
    screen.fill(BLACK)
    new_bullet.update(screen)
    if Player1.x > LENGTH - 64:
        Player1.x = LENGTH - 64
        event.type == pygame.KEYUP
    if Player1.x < 0:
        Player1.x = 0

    if new_bullet.y < 0:
        new_bullet.state = "OFF"
    if new_bullet.state == "OFF":
        new_bullet.x = Player1.x + 16
        new_bullet.y = Player1.y - 32
    else:
        new_bullet.x = new_bullet.x
    for new_bullet in bullets:
        new_bullet.update(screen)

    if Player1.x != LENGTH  or Player1.x != 0:
        Player1.x += 1 * MOVERATE
        Player1.update(screen)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
