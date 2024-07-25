import pygame
import time
import threading

    # functions

    # failed attempt at threading, it seems like pygame doesnt like when events are handled in a different thread
# function for selecting a piece
#def selecting():
#    global running, light_pieces, dark_pieces, board_tiles, clock
#    while running:
#        for event in pygame.event.get():
#            if event.type == pygame.MOUSEBUTTONDOWN:
#                print("clicked")
#                x, y = pygame.mouse.get_pos()
#                # finding the tile that was clicked
#                x = x // 50
#                y = y // 50
#                # finding the piece that was clicked
#
#
#                print(x, y)
#            if event.type == pygame.QUIT:
#                running = False
#        clock.tick(60)



    # classes
# class for board tiles
class Board_tile:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        # 0 = white
        if self.color == 0:
            pygame.draw.rect(screen, (255, 255, 255), (self.x*50, self.y*50, 50, 50))
        # 1 = black
        elif self.color == 1:
            pygame.draw.rect(screen, (0, 0, 0), (self.x*50, self.y*50, 50, 50))
        # 2 = selected, red
        elif self.color == 2:
            pygame.draw.rect(screen, (255, 0, 0), (self.x*50, self.y*50, 50, 50))
        # 3 = possible move, green
        elif self.color == 3:
            pygame.draw.rect(screen, (0, 255, 0), (self.x*50, self.y*50, 50, 50))

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
    # this is a very basic implementation of the possible moves, I will add more logic later
    def possible_moves(self):
        self.moves = []
        self.moves.append((self.x, self.y+1))
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
    # this is a very basic implementation of the possible moves, I will add more logic later
    def possible_moves(self):
        self.moves = []
        for i in range(8):
            self.moves.append((self.x, i))
        for i in range(8):
            self.moves.append((i, self.y))
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
    # this is a very basic implementation of the possible moves, I will add more logic later
    def possible_moves(self):
        self.moves = []
        self.moves.append((self.x+1, self.y+2))
        self.moves.append((self.x+1, self.y-2))
        self.moves.append((self.x-1, self.y+2))
        self.moves.append((self.x-1, self.y-2))
        self.moves.append((self.x+2, self.y+1))
        self.moves.append((self.x+2, self.y-1))
        self.moves.append((self.x-2, self.y+1))
        self.moves.append((self.x-2, self.y-1))
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
    # this is a very basic implementation of the possible moves, I will add more logic later
    def possible_moves(self):
        self.moves = []
        for i in range(8):
            self.moves.append((self.x+i, self.y+i))
        for i in range(8):
            self.moves.append((self.x-i, self.y+i))
        for i in range(8):
            self.moves.append((self.x+i, self.y-i))
        for i in range(8):
            self.moves.append((self.x-i, self.y-i))
# class for the queen
class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 9
        self.type = "queen"
        self.state = "alive"
        if self.color == 0:
            self.image = resized_light_queen
        else:
            self.image = resized_dark_queen
    def draw(self):
        screen.blit(self.image, (self.x*50, self.y*50))
    # this is a very basic implementation of the possible moves, I will add more logic later
    def possible_moves(self):
        self.moves = []
        for i in range(8):
            self.moves.append((self.x, i))
        for i in range(8):
            self.moves.append((i, self.y))
        for i in range(8):
            self.moves.append((self.x+i, self.y+i))
        for i in range(8):
            self.moves.append((self.x-i, self.y+i))
        for i in range(8):
            self.moves.append((self.x+i, self.y-i))
        for i in range(8):
            self.moves.append((self.x-i, self.y-i))
# class for the king
class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.value = 10
        self.type = "king"
        self.state = "alive"
        if self.color == 0:
            self.image = resized_light_king
        else:
            self.image = resized_dark_king
    def draw(self):
        screen.blit(self.image, (self.x*50, self.y*50))
    # this is a very basic implementation of the possible moves, I will add more logic later        
    def possible_moves(self):
        self.moves = []
        self.moves.append((self.x+1, self.y))
        self.moves.append((self.x-1, self.y))
        self.moves.append((self.x, self.y+1))
        self.moves.append((self.x, self.y-1))
        self.moves.append((self.x+1, self.y+1))
        self.moves.append((self.x-1, self.y+1))
        self.moves.append((self.x+1, self.y-1))
        self.moves.append((self.x-1, self.y-1))


# Initialize the game
pygame.init()
# setting up the screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()

# setting the tile size, this will be mainly used later in the development for resizability
tile_size = 50

# loading the images
light_pawn = pygame.image.load("light_pawn.png")
dark_pawn = pygame.image.load("dark_pawn.png")
resized_light_pawn = pygame.transform.scale(light_pawn, (tile_size, tile_size))
resized_dark_pawn = pygame.transform.scale(dark_pawn, (tile_size, tile_size))
light_bishop = pygame.image.load("light_bishop.png")
dark_bishop = pygame.image.load("dark_bishop.png")
resized_light_bishop = pygame.transform.scale(light_bishop, (tile_size, tile_size))
resized_dark_bishop = pygame.transform.scale(dark_bishop, (tile_size, tile_size))
light_rook = pygame.image.load("light_rook.png")
dark_rook = pygame.image.load("dark_rook.png")
resized_light_rook = pygame.transform.scale(light_rook, (tile_size, tile_size))
resized_dark_rook = pygame.transform.scale(dark_rook, (tile_size, tile_size))
light_horse = pygame.image.load("light_horse.png")
dark_horse = pygame.image.load("dark_horse.png")
resized_light_horse = pygame.transform.scale(light_horse, (tile_size, tile_size))
resized_dark_horse = pygame.transform.scale(dark_horse, (tile_size, tile_size))
light_queen = pygame.image.load("light_queen.png")
dark_queen = pygame.image.load("dark_queen.png")
resized_light_queen = pygame.transform.scale(light_queen, (tile_size, tile_size))
resized_dark_queen = pygame.transform.scale(dark_queen, (tile_size, tile_size))
light_king = pygame.image.load("light_king.png")
dark_king = pygame.image.load("dark_king.png")
resized_light_king = pygame.transform.scale(light_king, (tile_size, tile_size))
resized_dark_king = pygame.transform.scale(dark_king, (tile_size, tile_size))

# setting up font for the score
font = pygame.font.Font(None, 36)

# setting up game board
board_tiles = []
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            board_tiles.append(Board_tile(i, j, 0))
        else:
            board_tiles.append(Board_tile(i, j, 1))

# getting all the coordinates of the board
coords = []
for i in range(8):
    for j in range(8):
        coords.append((i*tile_size, j*tile_size))

# more random variables that will be used throughout the code
tile_selected_original_color = None

# setting up list of pieces for both players and the scores
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
# setting up the bishops
for i in range(2):
    light_pieces.append(Bishop(i*3+2, 0, 0))
    dark_pieces.append(Bishop(i*3+2, 7, 1))
# setting up the queens
light_pieces.append(Queen(3, 0, 0))
dark_pieces.append(Queen(3, 7, 1))
# setting up the kings
light_pieces.append(King(4, 0, 0))
dark_pieces.append(King(4, 7, 1))

# setting up a thread for the selecting
#select_thread = threading.Thread(target=selecting)

# main loop
running = True
while running:

    # starting the thread for selecting
    #if not select_thread.is_alive():
        #select_thread.start()

    # getting the new score by counting the value of the living pieces
    score1 = 0
    score2 = 0
    for piece in light_pieces:
        if piece.state == "alive":
            score1 += piece.value
    for piece in dark_pieces:
        if piece.state == "alive":
            score2 += piece.value
    
    # fill the screen with gray
    screen.fill((200, 200, 200))

    # drawing board
    for tile in board_tiles:
        tile.draw()
    # drawing all the white pieces
    for piece in light_pieces:
        piece.draw()
    # drawing all the black pieces
    for piece in dark_pieces:
        piece.draw()

    
    # drawing the score
    text = font.render(str(score1) + " x " +str(score2), True, (0, 0, 0))
    screen.blit(text, (450, 50))
    
    # checking for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting the coordinates of the click, and determining the tile that was clicked
            x, y = pygame.mouse.get_pos()
            print(x, y)
            x = x // 50
            y = y // 50
            print(x, y)
            # finding the tile that was clicked and marking it as 2
            for tile in board_tiles:
                if tile.x == x and tile.y == y:
                    tile_selected_original_color = tile.color
                    tile.color = 2
            # finding the piece that was clicked
                # eventually I will make this player based, so each player can only move their pieces
            piece_selected = False
            for piece in light_pieces:
                if piece.x == x and piece.y == y:
                    print(piece.type)
                    piece_selected = True
                    # here I will make logic for displaying the possible moves
            for piece in dark_pieces:
                if piece.x == x and piece.y == y:
                    print(piece.type)
                    piece_selected = True
            if not piece_selected:
                # reseting the color of the empty tile
                for tile in board_tiles:
                    if tile.color == 2:
                        tile.color = tile_selected_original_color
                        tile_selected_original_color = None

                    # here I will make logic for displaying the possible moves

    # updating the screen
    clock.tick(60)
    pygame.display.update()