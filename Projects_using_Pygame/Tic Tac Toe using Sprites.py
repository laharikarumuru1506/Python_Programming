import pygame

pygame.init()

screen = pygame.display.set_mode((600, 450))

pygame.display.set_caption("Tic Tac Toe")

run = True
player = 1
game_over = 0
list = []
pos = []


def show_message(x):
    global game_over
    if x == 1:
        game_over = 1
        score = font.render("Player 1 Won", True, (255, 255, 255))
        screen.blit(score, (230, 230))

    else:
        game_over = 1
        score = font.render("Player 2 Won", True, (255, 255, 255))
        screen.blit(score, (230, 230))


def check():
    for i in range(3):
        j = 0
        if (list[i][j] == 1 and list[i][j + 1] == 1 and list[i][j + 2] == 1) or (
                list[j][i] == 1 and list[j + 1][i] == 1 and list[j + 2][i] == 1) or (
                list[0][0] == 1 and list[1][1] == 1 and list[2][2] == 1) or (
                list[0][2] == 1 and list[1][1] == 1 and list[2][0] == 1):
            show_message(1)

        elif (list[i][j] == 0 and list[i][j + 1] == 0 and list[i][j + 2] == 0) or (
                list[j][i] == 0 and list[j + 1][i] == 0 and list[j + 2][i] == 0) or (
                list[0][0] == 0 and list[1][1] == 0 and list[2][2] == 0) or (
                list[0][2] == 0 and list[1][1] == 0 and list[2][0] == 0):
            show_message(0)


class Player1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        if pos_x < 200 and pos_y < 150:
            self.rect.center = (100, 75)
            list[0][0] = 1
        elif pos_x > 200 and pos_x < 400 and pos_y < 150:
            self.rect.center = (300, 75)
            list[0][1] = 1
        elif pos_x > 400 and pos_x < 600 and pos_y < 150:
            self.rect.center = (500, 75)
            list[0][2] = 1
        elif pos_x < 200 and pos_y > 150 and pos_y < 300:
            self.rect.center = (100, 225)
            list[1][0] = 1
        elif pos_x < 200 and pos_y > 300 and pos_y < 450:
            self.rect.center = (100, 375)
            list[2][0] = 1
        elif pos_x > 200 and pos_x < 400 and pos_y > 150 and pos_y < 300:
            self.rect.center = (300, 225)
            list[1][1] = 1
        elif pos_x > 400 and pos_x < 600 and pos_y > 150 and pos_y < 300:
            self.rect.center = (500, 225)
            list[1][2] = 1
        elif pos_x > 200 and pos_x < 400 and pos_y > 300 and pos_y < 450:
            self.rect.center = (300, 375)
            list[2][1] = 1
        elif pos_x > 400 and pos_x < 600 and pos_y > 300 and pos_y < 450:
            self.rect.center = (500, 375)
            list[2][2] = 1


class Player2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        if pos_x < 200 and pos_y < 150:
            self.rect.center = (100, 75)
            list[0][0] = 0
        elif pos_x > 200 and pos_x < 400 and pos_y < 150:
            self.rect.center = (300, 75)
            list[0][1] = 0
        elif pos_x > 400 and pos_x < 600 and pos_y < 150:
            self.rect.center = (500, 75)
            list[0][2] = 0
        elif pos_x < 200 and pos_y > 150 and pos_y < 300:
            self.rect.center = (100, 225)
            list[1][0] = 0
        elif pos_x < 200 and pos_y > 300 and pos_y < 450:
            self.rect.center = (100, 375)
            list[2][0] = 0
        elif pos_x > 200 and pos_x < 400 and pos_y > 150 and pos_y < 300:
            self.rect.center = (300, 225)
            list[1][1] = 0
        elif pos_x > 400 and pos_x < 600 and pos_y > 150 and pos_y < 300:
            self.rect.center = (500, 225)
            list[1][2] = 0
        elif pos_x > 200 and pos_x < 400 and pos_y > 300 and pos_y < 450:
            self.rect.center = (300, 375)
            list[2][1] = 0
        elif pos_x > 400 and pos_x < 600 and pos_y > 300 and pos_y < 450:
            self.rect.center = (500, 375)
            list[2][2] = 0


def draw_Grid():
    for i in range(3):
        pygame.draw.line(screen, (128, 128, 128), (i * 200, 0), (i * 200, 450), 10)
        pygame.draw.line(screen, (128, 128, 128), (0, i * 150), (600, i * 150), 10)


font = pygame.font.Font("freesansbold.ttf", 32)
# pygame.mouse.set_visible(False)
player_list = pygame.sprite.Group()
for i in range(3):
    rows = [-1] * 3
    list.append(rows)
print(list)

while run:

    screen.fill((255, 200, 0))
    draw_Grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if player == 1:
                    player1 = Player1(x, y)
                    player_list.add(player1)
                else:
                    player2 = Player2(x, y)
                    player_list.add(player2)

                player *= -1

    check()
    player_list.draw(screen)
    pygame.display.update()

pygame.quit()
