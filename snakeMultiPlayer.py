import sys
import pygame
import time
import random

# 1 ... 10


DIFFICULTY = 10

START_LENGTH = 9
WAIT	= 0.1 / DIFFICULTY
RADIUS	= 10
RES	= [900, 600]

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (165,80,42)
ORANGE = (255, 100, 0)


WALL	= []
BUG     = ()
pygame.init()
score1 = 0
score2 = 0
corner = pygame.font.Font(None, 50)

SCREEN = pygame.display.set_mode(RES)
pygame.display.set_caption("Snake by Yousef")

class Mob():
    """class for moving objects
    """
    def __init__(self):
        self.headx = RES[0]-100
        self.heady = RES[1]-100
        self.length = START_LENGTH
        self.elements = [[self.headx, self.heady]]

        while len(self.elements) != (self.length - 1):
            self.elements.append([self.headx, self.heady])
        self.speed = [-2 * RADIUS, 0]
        pygame.draw.circle(SCREEN, YELLOW, (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()

    def move(self):
        """move function
        """
        pygame.draw.circle(SCREEN, BLACK, (self.elements[-1][0],
            self.elements[-1][1]), RADIUS)
        self.elements.pop()
        self.headx += self.speed[0]
        self.heady += self.speed[1]
        self.elements = [[self.headx, self.heady]] + self.elements[0:]
        self.check_dead()
        for element in self.elements[1:]:
            pygame.draw.circle(SCREEN, GREEN, (element[0], element[1]),
                RADIUS)
        pygame.draw.circle(SCREEN, YELLOW, (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()
        self.check_bug()

    def check_dead(self):
        """check_dead function
        """
        global score1
        if [self.headx, self.heady] in self.elements[5:]:
            score1 = 0
            exit_dead()

        if [self.headx, self.heady] in WALL:
            score1 = 0
            exit_dead()

        if self.headx > RES[0]:
            self.headx -= RES[0]
            SNAKE.move()
        if self.headx < 0:
            self.headx += RES[0]
            SNAKE.move()
        if self.heady > RES[1]:
            self.heady -= RES[1]
            SNAKE.move()
        if self.heady < 0:
            self.heady += RES[1]
            SNAKE.move()

    def check_bug(self):
        """check_bug function
        """
        global score1
        if (self.headx, self.heady) == BUG:
            self.elements.append(self.elements[-1])
            # Calls for new bug as soon as previous one is consumed
            score1 += 1
            SCREEN.blit(corner.render("Score: " + str(score1), True, GREEN), [10, 0])
            create_bug()

class Mob2():
    """class for moving objects
    """
    def __init__(self):
        self.headx = 100
        self.heady = 100
        self.length = START_LENGTH
        self.elements2 = [[self.headx, self.heady]]

        while len(self.elements2) != (self.length - 1):
            self.elements2.append([self.headx, self.heady])
        self.speed = [RADIUS * 2, 0]
        pygame.draw.circle(SCREEN, BLACK, (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()

    def move(self):
        """move function
        """
        pygame.draw.circle(SCREEN, BLACK, (self.elements2[-1][0],
            self.elements2[-1][1]), RADIUS)
        self.elements2.pop()
        self.headx += self.speed[0]
        self.heady += self.speed[1]
        self.elements2 = [[self.headx, self.heady]] + self.elements2[0:]
        self.check_dead()
        for element in self.elements2[1:]:
            pygame.draw.circle(SCREEN, ORANGE, (element[0], element[1]),
                RADIUS)
        pygame.draw.circle(SCREEN, YELLOW, (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()
        self.check_bug()

    def check_dead(self):
        """check_dead function
        """
        global score2
        if [self.headx, self.heady] in self.elements2[5:]:
            score2 = 0
            exit_dead()

        if [self.headx, self.heady] in WALL:
            score2 = 0
            exit_dead()

        if self.headx > RES[0]:
            self.headx -= RES[0]
            SNAKE2.move()
        if self.headx < 0:
            self.headx += RES[0]
            SNAKE2.move()
        if self.heady > RES[1]:
            self.heady -= RES[1]
            SNAKE2.move()
        if self.heady < 0:
            self.heady += RES[1]
            SNAKE2.move()

    def check_bug(self):
        """check_bug function
        """
        global score2
        if (self.headx, self.heady) == BUG:
            self.elements2.append(self.elements2[-1])
            # Calls for new bug as soon as previous one is consumed
            score2 += 1
            SCREEN.blit(corner.render("Score: " + str(score2), True, ORANGE), [RES[0]-165, 0])
            create_bug()

def draw_map():
    """draw_map function
    """
    pygame.draw.rect(SCREEN, BLACK, [0, 0, RES[0], RES[1]])
    #Draws the map borders on the edge of the screen with adjustable settings
    '''for n in range(20, RES[0], 20):
        pygame.draw.circle(SCREEN, (0, 0, 255), (n, 40), 10)
        WALL.append([n, 40])
        pygame.draw.circle(SCREEN,(0, 0, 255),(n, RES[1] - 20), 10)
        WALL.append([n, RES[1] - 20])
    for n in range(40, RES[1], 20):
        pygame.draw.circle(SCREEN, (0, 0, 255),(20, n), 10)
        WALL.append([20, n])
        pygame.draw.circle(SCREEN, (0, 0, 255), (RES[0] - 20, n), 10)
        WALL.append([RES[0] - 20 , n])'''
    board1 = corner.render("Score: " + str(score1), True, GREEN)
    board2 = corner.render("Score: " + str(score1), True, ORANGE)
    SCREEN.blit(board1, [10, 0])
    SCREEN.blit(board2, [RES[0]-165, 0])
    pygame.display.flip()


def create_bug():
    """create_bug function
    """
    global BUG
    BUG = ()
    while (list(BUG) in WALL ) or ( list(BUG) in SNAKE.elements) or (not BUG):
        BUG = (random.randrange(40, RES[0] - 40 , 20),
            (random.randrange(40, RES[1] - 40 , 20)))

    pygame.draw.circle(SCREEN, (165,80,42), BUG, RADIUS)
    pygame.display.flip()

def event_loop():
    """main event loop
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_DOWN) and \
                    (SNAKE.speed != [0, -2*RADIUS]):
                    SNAKE.speed = [0, 2*RADIUS]
                elif (event.key == pygame.K_UP) and \
                    (SNAKE.speed != [0, 2*RADIUS]):
                    SNAKE.speed = [0, -2*RADIUS]
                elif (event.key == pygame.K_RIGHT) and \
                    (SNAKE.speed != [-2* RADIUS, 0]):
                    SNAKE.speed = [2*RADIUS, 0]
                elif (event.key == pygame.K_LEFT) and \
                    (SNAKE.speed != [2* RADIUS, 0]):
                    SNAKE.speed = [-2*RADIUS, 0]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if (event.key == pygame.K_s)    and \
                    (SNAKE2.speed != [0, -2*RADIUS]):
                    SNAKE2.speed = [0, 2*RADIUS]
                elif (event.key == pygame.K_w) and \
                    (SNAKE2.speed != [0, 2*RADIUS]):
                    SNAKE2.speed = [0, -2*RADIUS]
                elif (event.key == pygame.K_d) and \
                    (SNAKE2.speed != [-2* RADIUS, 0]):
                    SNAKE2.speed = [2*RADIUS, 0]
                elif (event.key == pygame.K_a) and \
                    (SNAKE2.speed != [2* RADIUS, 0]):
                    SNAKE2.speed = [-2*RADIUS, 0]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        SNAKE.move()
        pygame.draw.rect(SCREEN, BLACK, [0, 0, 200, 30])
        SCREEN.blit(corner.render("Score: " + str(score1), True, GREEN), [10, 0])
        SNAKE2.move()
        pygame.draw.rect(SCREEN, BLACK, [RES[0] - 165, 0, 200, 30])
        SCREEN.blit(corner.render("Score: " + str(score2), True, ORANGE), [RES[0] - 165, 0])


def exit_dead():
    """exit_dead function
    """
    global SNAKE
    global SNAKE2
    centerFont = pygame.font.Font(None, 200)
    bottomFont = pygame.font.Font(None, 60)

    gameOver = centerFont.render("Game Over", True, (255, 0, 0))
    restart = bottomFont.render("Press SPACE to play again!", True, GREEN)
    text_rect = gameOver.get_rect()
    text_x = SCREEN.get_width() / 2 - text_rect.width / 2
    text_y = SCREEN.get_height() / 2 - text_rect.height / 2

    pygame.display.update(SCREEN.blit(gameOver, [text_x, text_y]))
    pygame.display.update(SCREEN.blit(restart, [text_x + 120, text_y + 200]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SNAKE = Mob()
                    SNAKE2 = Mob2()
                    main()

SNAKE = Mob()
SNAKE2 = Mob2()
def main():
    draw_map()
    create_bug()
    event_loop()

main()
