import os
import sys
import pygame
import time
import random

# 1 ... 10
#Game Settings
DIFFICULTY = 10
START_LENGTH = 12
RES = [1000, 700]
WAIT	= 0.1 / DIFFICULTY

#Initial Values
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BRWON = (165,80,42)

RADIUS	= 10
WALL	= []
BUG     = ()
pygame.init()
score = 0
corner = pygame.font.Font(None, 50)

#Screen Set up
SCREEN = pygame.display.set_mode(RES)
pygame.display.set_caption("Snake by Yousef")

class Mob():
    """class for moving objects
    """
    def __init__(self):
        #Where the snakes position starts
        self.headx = 100
        self.heady = 100
        self.length = START_LENGTH
        self.elements = [[self.headx, self.heady]]

        #Builds Snake untill starting length is reaches
        while len(self.elements) != (self.length - 1):
            self.elements.append([self.headx, self.heady])
        
        #Sets initial direction of movment
        self.speed = [RADIUS * 2, 0]

        #Draws green head of snake
        pygame.draw.circle(SCREEN, YELLOW, (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()

    def move(self):
        """move function
        """
        pygame.draw.circle(SCREEN, BLACK, (self.elements[-1][0],
            self.elements[-1][1]), RADIUS)
        self.elements.pop()

        #directs snake movement
        self.headx += self.speed[0]
        self.heady += self.speed[1]
        self.elements = [[self.headx, self.heady]] + self.elements[0:]
        self.check_dead()

        #Draws as many body parts as their are indexes in the list
        for element in self.elements[1:]:
            pygame.draw.circle(SCREEN, YELLOW, (element[0], element[1]),
                RADIUS) 
        pygame.draw.circle(SCREEN, GREEN, (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()
        #checks if the snake has eaten a bug after every movement
        self.check_bug()

    def check_dead(self):
        """check_dead function
        """
        #Exits game if snake hits its self
        if [self.headx, self.heady] in self.elements[8:]:
            exit_dead()
        #Exits game if snake hits the wall
        if [self.headx, self.heady] in WALL:
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
        # checks if the snake has eaten a bug after every movement by comparing the x and y cordinants
        global score
        if (self.headx, self.heady) == BUG:
            self.elements.append(self.elements[-1])
            #Calls for new bug as soon as previous one is consumed
            score += 1
            pygame.draw.rect(SCREEN, BLACK, [0, 0, 200, 30])
            SCREEN.blit(corner.render("Score: " + str(score), True, GREEN), [20, 0])
            create_bug()


def draw_map():
    """draw_map function
    """
    #Draws the map borders on the edge of the screen with adjustable settings
    '''for n in range(20, RES[0], 20):
        pygame.draw.circle(SCREEN, BLUE, (n, 40), 10)
        WALL.append([n, 40])
        pygame.draw.circle(SCREEN,BLUE,(n, RES[1] - 20), 10)
        WALL.append([n, RES[1] - 20])
    for n in range(40, RES[1], 20):
        pygame.draw.circle(SCREEN, BLUE,(20, n), 10)
        WALL.append([20, n])
        pygame.draw.circle(SCREEN, BLUE, (RES[0] - 20, n), 10)
        WALL.append([RES[0] - 20 , n])'''
    board = corner.render("Score: " + str(score), True, GREEN)
    SCREEN.blit(board, [20, 0])
    pygame.display.flip()

def create_bug():
    """create_bug function
    """
    global BUG
    BUG = ()
    #Checks that the bug is not randomly generated on to the wall or snakes body and then displays it
    while ( list(BUG) in WALL ) or ( list(BUG) in SNAKE.elements) or (not BUG):
        BUG = (random.randrange(40, RES[0] - 40, 20),
            (random.randrange(40, RES[1] - 40, 20)))

    # Generates the bug
    pygame.draw.circle(SCREEN, (165,80,42), BUG, RADIUS)
    pygame.display.flip()

def event_loop():
    """main event loop
    """

    while True:
        time.sleep(WAIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #Makes sure user input isn't opposite to current moving direction and the changes movement
                if (event.key == pygame.K_DOWN)	and \
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
        SNAKE.move()
        pygame.draw.rect(SCREEN, BLACK, [0, 0, 200, 30])
        SCREEN.blit(corner.render("Score: " + str(score), True, GREEN), [20, 0])

def exit_dead():
    """exit_dead function
    """

    #Text Display
    centerFont = pygame.font.Font(None, 200)
    bottomFont = pygame.font.Font(None, 50)
    gameOver = centerFont.render("Game Over", True, RED)
    restart = bottomFont.render("Press SPACE to play again!", True, GREEN)
    text_rect = gameOver.get_rect()
    text_x = SCREEN.get_width() / 2 - text_rect.width / 2
    text_y = SCREEN.get_height() / 2 - text_rect.height / 2
    pygame.display.update(SCREEN.blit(gameOver, [text_x, text_y]))
    pygame.display.update(SCREEN.blit(restart, [text_x + 150, text_y + 200]))

    #Command line score display
    print("")
    print("Difficulty:\t%d" % DIFFICULTY)
    print("")
    print("Bugs eaten:\t%d" % (len(SNAKE.elements) - START_LENGTH + 1))
    print("")
    print("Score:\t\t%d" % ((len(SNAKE.elements) - START_LENGTH + 1) * DIFFICULTY))
    print("")

    #Pause screen to ask user if they would like to replay
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    os.system("python3 snake.py")
                    pygame.quit()
                    sys.exit()

#Main calls
if __name__ == "__main__":
    draw_map()
    SNAKE = Mob()
    create_bug()
    event_loop()
