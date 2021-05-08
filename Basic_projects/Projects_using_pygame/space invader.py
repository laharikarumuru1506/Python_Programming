import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("space invader")

# player attributes
playerImg = pygame.image.load("D:\Lahari Karumuru\space-invaders.png")
playerX = 210
playerY = 400
playerX_change = 0
playerY_change = 0

# bullet attributes
bulletImg = pygame.image.load("D:\Lahari Karumuru\weapon.png")
bulletX = 210
bulletY = 400
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# enemy attributes
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_enemies = 6
for i in range(no_enemies):
    enemyImg.append(pygame.image.load("D:\Lahari Karumuru\octopus.png"))
    enemyX.append(random.randint(0, 436))
    enemyY.append(random.randint(0, 300))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

run = True
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

testX = 10
testY = 10


def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def collision(enemyX, enemyY, bulletX, bulletY):
    global distance
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
                # playerX += playerX_change
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
                # playerX += playerX_change
            if event.key == pygame.K_UP:
                playerY_change = -0.5
                # playerY += playerY_change
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
                # playerY += playerY_change

    # FOR PLAYER
    if playerX <= 0:
        playerX = 0
    elif playerX >= 436:
        playerX = 436
    if playerY <= 0:
        playerY = 0
    elif playerY >= 436:
        playerY = 436

    screen.fill((0, 0, 255))
    player(playerX, playerY)
    playerX += playerX_change
    # playerY += playerY_change

    for i in range(no_enemies):
        enemyX[i] += enemyX_change[i]
        # enemyY += enemyY_change

        # FOR ENEMY
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 436:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        # collision

        collide = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collide:
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, 436)
            enemyY[i] = (random.randint(0, 300))

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    # bulletX += bulletX_change

    show_score(testX, testY)
    pygame.display.update()
pygame.display.quit()
