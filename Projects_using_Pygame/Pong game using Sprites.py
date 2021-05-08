import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("pong game")
clock = pygame.time.Clock()

run = True
opponent_score = 0
player_score = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 80))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 100
        self.speed = 0

    def update(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y > 420:
            self.rect.y = 420
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed = -7
            self.rect.y += self.speed
        if keystate[pygame.K_d]:
            self.speed = 7
            self.rect.y += self.speed


class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 80))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 590
        self.rect.y = 200
        self.speed = 0

    def update(self):
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y > 420:
            self.rect.y = 420
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speed = -7
            self.rect.y += self.speed
        if keystate[pygame.K_DOWN]:
            self.speed = 7
            self.rect.y += self.speed


class Bob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(20, 580)
        self.rect.y = random.randrange(0, 490)
        self.speed_x = random.choice([-1, 1])
        self.speed_y = random.choice([-1, 1])

    def update(self):
        global opponent_score
        global player_score
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 490:
            self.speed_y *= -1
        if self.rect.left <= 0:
            opponent_score += 1
            self.image = pygame.Surface((10, 10))
            self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(20, 580)
            self.rect.y = random.randrange(0, 490)
            self.speed_x = random.choice([-1,1])
            self.speed_y = random.choice([-1,1])
        if self.rect.right >= 600:
            player_score += 1
            self.image = pygame.Surface((10, 10))
            self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(20, 580)
            self.rect.y = random.randrange(0, 490)
            self.speed_x = random.choice([-1, 1])
            self.speed_y = random.choice([-1, 1])

        if pygame.sprite.spritecollide(player, bobs, False) or pygame.sprite.spritecollide(opponent, bobs, False):
                self.speed_x *= -1


def show_score():
    score = font.render("Player 2 : " + str(opponent_score), True, (255, 255, 255))
    screen.blit(score, (450, 20))

    score = font.render("Player 1 : " + str(player_score), True, (255, 255, 255))
    screen.blit(score, (150, 20))


players = pygame.sprite.Group()
player = Player()
players.add(player)

opponents = pygame.sprite.Group()
opponent = Opponent()
# players.add(opponent)
opponents.add(opponent)

bobs = pygame.sprite.Group()
bob = Bob()
players.add(bob)
bobs.add(bob)

font = pygame.font.Font("freesansbold.ttf", 16)

while run:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 500), 3)

    players.update()
    players.draw(screen)

    opponents.update()
    opponents.draw(screen)

    bobs.update()
    bobs.draw(screen)

    show_score()

    clock.tick(60)
    pygame.display.update()
pygame.quit()
