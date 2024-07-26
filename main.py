import pygame
import time
import threading

    # functions




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
        if self.color == 0:
            self.moves.append((self.x, self.y+1))
        else:
            self.moves.append((self.x, self.y-1))
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
tile_selected_original_color = []

# setting up list of pieces for both players and the scores
light_pieces = []
score1 = 0
dark_pieces = []
score2 = 0
# seting up player turns variables
players = ["light", "dark"]
current_player = players[0]
available_moves = []
tiles_selected = []

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

# main loop
running = True
while running:

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

    # drawing a label displaying the current player
    text = font.render(str(current_player) + "'s turn", True, (0, 0, 0))
    screen.blit(text, (450, 100))
    
    # checking for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting the coordinates of the click, and determining the tile that was clicked
            x, y = pygame.mouse.get_pos()
            x = x // 50
            y = y // 50

            # finding the tile that was clicked and marking it as 2
            if len(tile_selected_original_color) == 0:
                for tile in board_tiles:
                    if tile.x == x and tile.y == y:
                        tile_selected_original_color.append(tile.color)
                        tile.color = 2
                        tiles_selected.append((tile.x, tile.y))

            # finding the piece that was clicked
            piece_selected = False
            if current_player == "light":
                for piece in light_pieces:
                    if piece.x == x and piece.y == y:
                        piece_selected = True
                        # getting the possible moves of the piece
                        piece.possible_moves()
                        # marking the possible moves as 3
                        for move in piece.moves:
                            for tile in board_tiles:
                                if tile.x == move[0] and tile.y == move[1]:
                                    tile_selected_original_color.append(tile.color)
                                    tile.color = 3
                                    available_moves.append((tile.x, tile.y))
                                    tiles_selected.append((tile.x, tile.y))
            else:
                for piece in dark_pieces:
                    if piece.x == x and piece.y == y:
                        piece_selected = True
                        # getting the possible moves of the piece
                        piece.possible_moves()
                        # marking the possible moves as 3
                        for move in piece.moves:
                            for tile in board_tiles:
                                if tile.x == move[0] and tile.y == move[1]:
                                    tile_selected_original_color.append(tile.color)
                                    tile.color = 3
                                    available_moves.append((tile.x, tile.y))
                                    tiles_selected.append((tile.x, tile.y))
            #print(tile_selected_original_color)

            if not piece_selected:
                # reseting the color of the empty tile
                for tile in board_tiles:
                    if tile.color == 2 or tile.color == 3:
                        for i in range(len(tiles_selected)):
                            if tile.x == tiles_selected[i][0] and tile.y == tiles_selected[i][1]:
                                tile.color = tile_selected_original_color[i]
                        #tile_selected_original_color.clear()

            # checking if the player clicked on a possible move
            for move in available_moves:
                if move[0] == x and move[1] == y:
                    # recoloring to original colors
                    if current_player == "light":
                        for piece in light_pieces:
                            if piece.x == x and piece.y == y:
                                piece.x = x
                                piece.y = y
                                #for tile in board_tiles:
                                    #if tile.color == 2 or tile.color == 3:
                                        #print(tile_selected_original_color)
                                        #tile.color = tile_selected_original_color[0]
                                        #tile_selected_original_color.remove(tile_selected_original_color[0])
                                        #tile_selected_original_color.clear()
                    else:
                        print("dark")
                        for piece in dark_pieces:
                            if piece.x == x and piece.y == y:
                                print("dark2")
                                piece.x = x
                                piece.y = y
                                #for tile in board_tiles:
                                #    if tile.color == 2 or tile.color == 3:
                                  #      print(tile_selected_original_color)
                                 #       tile.color = tile_selected_original_color[0]
                                #        tile_selected_original_color.remove(tile_selected_original_color[0])

                    # changing the player
                    if current_player == "light":
                        current_player = players[1]
                    else:
                        current_player = players[0]

                    # clearing the available moves
                    available_moves.clear()

                    # clearing the original color of the tiles
                    if len(tile_selected_original_color) > 0:
                        for tile in board_tiles:
                            if tile.color == 2 or tile.color == 3:
                                tile.color = tile_selected_original_color[0]
                                tile_selected_original_color.remove(tile_selected_original_color[0])
                        tile_selected_original_color.clear()
                        tiles_selected.clear()
                    # clearing the possible moves of the pieces
                    for piece in light_pieces:
                        piece.moves = []
                    for piece in dark_pieces:
                        piece.moves = []
                
    #print(tile_selected_original_color)
    
    # updating the screen
    clock.tick(60)
    pygame.display.update()