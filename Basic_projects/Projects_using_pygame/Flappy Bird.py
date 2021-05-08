import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

run = True
game_active = 0
score_value = 0

floor_x = 0
floor_speed = 0.5

bird_x = 20
bird_y = 300
bird_speed = 0
gravity = 0.1


def game_over():
    over_game = font.render("Game Over", True, (0, 0, 0))
    screen.blit(over_game, (180, 300))


def show_score():
    score = myfont.render("Score : " + str(int(score_value)), True, (0, 0, 0))
    screen.blit(score, (0, 0))


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= 0 or bird_rect.bottom >= 488:
        return False

    return True


def create_pipe():
    random_pos = random.randrange(300, 480)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pos))
    top_pipe = pipe_surface.get_rect(midtop=(500, random_pos - 600))
    return bottom_pipe, top_pipe


# for getting background on screen
class Background():
    def __init__(self):
        self.image = pygame.image.load("D:\Lahari Karumuru\screen.png").convert()
        self.image = pygame.transform.scale(self.image, (500, 600))
        self.rect = self.image.get_rect()


# for getting ground on screen
class Ground():
    def __init__(self):
        self.image = pygame.image.load("D:\Lahari Karumuru\ground.png").convert()
        self.image = pygame.transform.scale(self.image, (500, 112))
        self.rect = self.image.get_rect()


# for getting bird on screen

bird_surface = pygame.image.load("D:\Lahari Karumuru\player.png").convert()
bird_surface = pygame.transform.scale(bird_surface, (36, 30))
bird_rect = bird_surface.get_rect(center=(bird_x, bird_y))

# for getting green-pipe on screen
pipe_surface = pygame.image.load("D:\Lahari Karumuru\pipe-green.png").convert()

pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# creating the objects
bg = Background()
ground = Ground()

font = pygame.font.Font("freesansbold.ttf", 32)
myfont = pygame.font.Font("freesansbold.ttf", 25)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = 0
                bird_speed -= 3

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # for background
    screen.blit(bg.image, (0, 0))

    # for ground
    screen.blit(ground.image, (floor_x, 488))
    screen.blit(ground.image, (floor_x + 500, 488))

    floor_x -= floor_speed
    if floor_x <= -500:
        floor_x = 0
    if game_active == 0:
        # for green-pipe
        for pipe in pipe_list:
            pipe.centerx -= 2
            if pipe.bottom >= 480:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

        # for bluebird
        screen.blit(bird_surface, bird_rect)
        bird_speed += gravity
        bird_rect.centery += bird_speed

    # check collision occurs or not
    game_check = check_collision(pipe_list)
    if game_check:
        score_value += 0.01
    else:
        game_active = 1
        game_over()

    show_score()

    pygame.display.update()
    clock.tick(100)
pygame.quit()
