import pygame
import time

    # classes
# class for all the pieces
class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
# class for the pawn
class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 1
        self.type = "pawn"
        self.state = "alive"
        if self.color == 0:
            self.image = resized_light_pawn
        else:
            self.image = resized_dark_pawn
    def draw(self):
        screen.blit(self.image, (self.x*50, self.y*50))
# class for the rook
class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 5
        self.type = "rook"
        self.state = "alive"
        if self.color == 0:
            self.image = resized_light_rook
        else:
            self.image = resized_dark_rook
    def draw(self):
        screen.blit(self.image, (self.x*50, self.y*50))
# class for the knight
class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 3
        self.type = "knight"
        self.state = "alive"
        if self.color == 0:
            self.image = pygame.transform.rotate(resized_light_horse, 180)
        else:
            self.image = resized_dark_horse
    def draw(self):
        screen.blit(self.image, (self.x*50, self.y*50))
# class for the bishop
class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 3
        self.type = "bishop"
        self.state = "alive"
        if self.color == 0:
            self.image = resized_light_bishop
        else:
            self.image = resized_dark_bishop
    def draw(self):
        screen.blit(self.image, (self.x*50, self.y*50))
# class for the queen
class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 9
        self.type = "queen"
        self.state = "alive"
    def draw(self):
        pass



# Initialize the game
pygame.init()
# setting up the screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()

# loading the images
light_pawn = pygame.image.load("light_pawn.png")
dark_pawn = pygame.image.load("dark_pawn.png")
resized_light_pawn = pygame.transform.scale(light_pawn, (50, 50))
resized_dark_pawn = pygame.transform.scale(dark_pawn, (50, 50))
light_bishop = pygame.image.load("light_bishop.png")
dark_bishop = pygame.image.load("dark_bishop.png")
resized_light_bishop = pygame.transform.scale(light_bishop, (50, 50))
resized_dark_bishop = pygame.transform.scale(dark_bishop, (50, 50))
light_rook = pygame.image.load("light_rook.png")
dark_rook = pygame.image.load("dark_rook.png")
resized_light_rook = pygame.transform.scale(light_rook, (50, 50))
resized_dark_rook = pygame.transform.scale(dark_rook, (50, 50))
light_horse = pygame.image.load("light_horse.png")
dark_horse = pygame.image.load("dark_horse.png")
resized_light_horse = pygame.transform.scale(light_horse, (50, 50))
resized_dark_horse = pygame.transform.scale(dark_horse, (50, 50))

# setting up font for the score
font = pygame.font.Font(None, 36)

# setting up game board
board = []
color = 0
for i in range(8):
    row = []
    for j in range(8):
        row.append(color)
        color = 1 - color
    board.append(row)
    color = 1 - color
# getting all the coordinates of the board
coords = []
for i in range(8):
    for j in range(8):
        coords.append((i*50, j*50))

# setting up list of pieces for both plaers
light_pieces = []
score1 = 0
dark_pieces = []
score2 = 0

    # setting up the pieces
# setting up the pawns
for i in range(8):
    light_pieces.append(Pawn(i, 1, 0))
    dark_pieces.append(Pawn(i, 6, 1))
# setting up the rooks
for i in range(2):
    light_pieces.append(Rook(i*7, 0, 0))
    dark_pieces.append(Rook(i*7, 7, 1))
# setting up the knights
for i in range(2):
    light_pieces.append(Knight(i*5+1, 0, 0))
    dark_pieces.append(Knight(i*5+1, 7, 1))


# main loop
running = True
while running:
    
    # fill the screen with white
    screen.fill((255, 255, 255))

    # drawing board
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (i*50, j*50, 50, 50))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (i*50, j*50, 50, 50))
        
    # drawing all the white pieces
    for piece in light_pieces:
        piece.draw()
    # drawing all the black pieces
    for piece in dark_pieces:
        piece.draw()

    
    # drawing the score
    text = font.render(str(score1) + " x " +str(score2), True, (0, 0, 0))
    screen.blit(text, (475, 50))
    
    # checking for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # updating the screen
    clock.tick(60)
    pygame.display.update()