import pygame
import time
import threading
import tkinter

    # functions

# function for a timer, that will later be used for timed rounds
def timer():
    global running, minutes, seconds, current_player, move_time, timer_on
    while running:
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if timer_on:
            if move_time[1] != 0 or move_time[0] != 0:
                if minutes == move_time[0] and seconds == move_time[1]:
                    # if the time is up the player that didnt make the move will be switched
                    if current_player == "light":
                        current_player = "dark"
                    else:
                        current_player = "light"
        clock.tick(1)
    
# function to reset the game
def reset_game():
    print("reseting game")
    global light_pieces, dark_pieces
    # for now this function will delete all the pieces and set them up again
    light_pieces.clear()
    dark_pieces.clear()

    # remaking all the tiles, this is done because sometimes the tiles can bug out and change their color to the wrong one(white to black and vice versa)
    global board_tiles
    board_tiles.clear()

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                board_tiles.append(Board_tile(i, j, 0))
            else:
                board_tiles.append(Board_tile(i, j, 1))

    # reseting cursor
    global custom_cursor
    custom_cursor = False
    
    # setting up the pieces again
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

    # seting the current player to light
    global current_player
    current_player = players[0]

    # resetting the timer
    reset_timer()

# function for resetting the timer
def reset_timer():
    global minutes, seconds
    minutes = 0
    seconds = 0

# function for applying settings
def apply_settings(window, var, var1, var2, entry, entry2):
    global screen, timer_on
    if int(entry) > 60 or int(entry) < 0 or int(entry2) > 60 or int(entry2) < 0:
        print("Invalid input")
        return
    # closing window
    window.destroy()
    # applying resizability selected
    if var1 == 1:
        screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    else:
        screen = pygame.display.set_mode((600, 400))
    # applying timer selection
    if var2 == 1:
        timer_on = True
    else:
        timer_on = False
    # applying the timer settings
    move_time[0] = int(entry)
    move_time[1] = int(entry2)

    # reseting game to apply the changes
    reset_game()

# function for the settings window
def settings_window():
    # setting up the window
    window = tkinter.Tk()
    window.title("Settings")
    window.geometry("400x400")
    window.iconbitmap("settings_icon.ico")
    window.resizable(False, False)
    # setting up the main label
    label = tkinter.Label(window, text="Settings", font=("Arial", 24))
    label.pack()
    # setting frame for the settings
    frame = tkinter.Frame(window)
    frame.pack()
    # setting up a label for special moves
    label = tkinter.Label(frame, text="Special moves", font=("Arial", 16))
    label.grid(row=0, column=0)
    # setting up a checkbox for special moves
    var = tkinter.IntVar()
    checkbox = tkinter.Checkbutton(frame, variable=var)
    checkbox.grid(row=0, column=1)
    # setting up a label for resizability of the window
    label = tkinter.Label(frame, text="Resizability", font=("Arial", 16))
    label.grid(row=1, column=0)
    # setting up a checkbox for resizability
    var1 = tkinter.IntVar()
    checkbox = tkinter.Checkbutton(frame, variable=var1)
    checkbox.grid(row=1, column=1)
    # setting up a label for the timer
    label = tkinter.Label(frame, text="Timer", font=("Arial", 16))
    label.grid(row=2, column=0)
    # setting up a checkbox for the timer
    var2 = tkinter.IntVar()
    checkbox = tkinter.Checkbutton(frame, variable=var2)
    checkbox.grid(row=2, column=1)
    # creating a label for subsettings of the timer
    label = tkinter.Label(frame, text="Timer settings", font=("Arial", 16))
    label.grid(row=3, column=0, columnspan=2)
    # creating a label for the minutes setting
    label = tkinter.Label(frame, text="Minutes:", font=("Arial", 16))
    label.grid(row=4, column=0)
    # creating entry for the minutes setting
    e1 = tkinter.StringVar()
    e1.set(str(move_time[0]))
    entry = tkinter.Entry(frame, font=("Arial", 16), textvariable=e1)
    entry.grid(row=4, column=1)
    # creating a label for the seconds setting
    label = tkinter.Label(frame, text="Seconds:", font=("Arial", 16))
    label.grid(row=5, column=0)
    # creating entry for the seconds setting
    e2 = tkinter.StringVar()
    e2.set(str(move_time[1]))
    entry2 = tkinter.Entry(frame, font=("Arial", 16), textvariable=e2)
    entry2.grid(row=5, column=1)

    # creating apply button
    apply_button = tkinter.Button(window, text="Apply", font=("Arial", 16), command=lambda:apply_settings(window, var.get(), var1.get(), var2.get(), entry.get(), entry2.get()))
    apply_button.pack(side="bottom")

    window.mainloop()


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
        if self.state == "alive":
            screen.blit(self.image, (self.x*50, self.y*50))
    # this is a good enough implementation of the possible moves
    def possible_moves(self):
        self.moves = []
        if self.color == 0:
            self.moves.append((self.x, self.y+1))
        else:
            self.moves.append((self.x, self.y-1))
        # removing the moves that are out of the board
        for move in self.moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                self.moves.remove(move)
        # removing the tile if its already occupied by allied piece or enemy piece
        for piece in light_pieces:
            for move in self.moves:
                if piece.x == move[0] and piece.y == move[1]:
                    self.moves.remove(move)
        for piece in dark_pieces:
            for move in self.moves:
                if piece.x == move[0] and piece.y == move[1]:
                    self.moves.remove(move)
        # adding the moves for taking pieces
        if self.color == 0:
            # checking that there is some piece to takk
            for piece in dark_pieces:
                if piece.x == self.x+1 and piece.y == self.y+1:
                    self.moves.append((self.x+1, self.y+1))
            for piece in dark_pieces:
                if piece.x == self.x-1 and piece.y == self.y+1:
                    self.moves.append((self.x-1, self.y+1))
        else:
            # checking that there is some piece to take
            for piece in light_pieces:
                if piece.x == self.x+1 and piece.y == self.y-1:
                    self.moves.append((self.x+1, self.y-1))
            for piece in light_pieces:
                if piece.x == self.x-1 and piece.y == self.y-1:
                    self.moves.append((self.x-1, self.y-1))

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
        if self.state == "alive":
            screen.blit(self.image, (self.x*50, self.y*50))
    # finaly a good implementation of the possible moves for the rook
    def possible_moves(self):
        self.moves = []

        # getting the coordinates of the rook
        x = self.x 
        y = self.y

        # row
        # getting all the moves from x to 0
        temp = True
        while x > 0 and temp:
            self.moves.append((x-1, y))
            # if there is a piece than the rook can't go further so the loop will stop
            for piece in light_pieces:
                if piece.x == x-1 and piece.y == y and piece.state == "alive":
                    temp = False
            for piece in dark_pieces:
                if piece.x == x-1 and piece.y == y and piece.state == "alive":
                    temp = False
            x -= 1
        # getting all the moves from x to 7
        x = self.x
        temp1 = True
        while x < 7 and temp1:
            self.moves.append((x+1, y))
            # if there is a piece than the rook can't go further so the loop will stop
            for piece in light_pieces:
                if piece.x == x+1 and piece.y == y and piece.state == "alive":
                    temp1 = False
            for piece in dark_pieces:
                if piece.x == x+1 and piece.y == y and piece.state == "alive":
                    temp1 = False
            x += 1

        # column
        # getting all the moves from y to 0
        x = self.x
        y = self.y
        temp2 = True
        while y > 0 and temp2:
            self.moves.append((x, y-1))
            for piece in light_pieces:
                if piece.x == x and piece.y == y-1 and piece.state == "alive":
                    temp2 = False
            for piece in dark_pieces:
                if piece.x == x and piece.y == y-1 and piece.state == "alive":
                    temp2 = False
            y -= 1
        # getting all the moves from y to 7
        y = self.y
        temp3 = True
        while y < 7 and temp3:
            self.moves.append((x, y+1))
            for piece in light_pieces:
                if piece.x == x and piece.y == y+1 and piece.state == "alive":
                    temp3 = False
            for piece in dark_pieces:
                if piece.x == x and piece.y == y+1 and piece.state == "alive":
                    temp3 = False
            y += 1

                # these conditions are now easily replacable, but I will leave them here just for now
        # removing the moves that are out of the board
        for move in self.moves:
            if move[0] < 0 or move[0] > 8 or move[1] < 0 or move[1] > 8:
                self.moves.remove(move)
        
        # removing the coordinate of the piece itself
        for move in self.moves:
            if move[0] == self.x and move[1] == self.y:
                self.moves.remove(move)

        # removing the tiles that are already controled by allied pieces
        if self.color == 0:
            for piece in light_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)
        else:
            for piece in dark_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)

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
        if self.state == "alive":
            screen.blit(self.image, (self.x*50, self.y*50))
    # this is a good enough implementation of the possible moves
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
        # removing the moves that are out of the board
        for move in self.moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                self.moves.remove(move)
        # removing the tiles that are already by allied pieces
        if self.color == 0:
            for piece in light_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)
        else:
            for piece in dark_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)
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
        if self.state == "alive":
            screen.blit(self.image, (self.x*50, self.y*50))
    # this is a very basic implementation of the possible moves, I will add more logic later
    def possible_moves(self):
        self.moves = []
       # getting the coordinates of the bishop
        x = self.x
        y = self.y

        # getting all the moves towards top left corner, until one of the values is below 0
        temp = True
        while x > 0 and y > 0 and temp:
            self.moves.append((x-1, y-1))
            for piece in light_pieces:
                if piece.x == x-1 and piece.y == y-1 and piece.state == "alive":
                    temp = False
            for piece in dark_pieces:
                if piece.x == x-1 and piece.y == y-1 and piece.state == "alive":
                    temp = False
            x -= 1
            y -= 1
        # getting all the moves towards top right corner, until one of the values is below 0
        x = self.x
        y = self.y
        temp1 = True
        while x < 7 and y > 0 and temp1:
            self.moves.append((x+1, y-1))
            for piece in light_pieces:
                if piece.x == x+1 and piece.y == y-1 and piece.state == "alive":
                    temp1 = False
            for piece in dark_pieces:
                if piece.x == x+1 and piece.y == y-1 and piece.state == "alive":
                    temp1 = False
            x += 1
            y -= 1
        # getting all the moves towards bottom left corner, until one of the values is below 0
        x = self.x
        y = self.y
        temp2 = True
        while x > 0 and y < 7 and temp2:
            self.moves.append((x-1, y+1))
            for piece in light_pieces:
                if piece.x == x-1 and piece.y == y+1 and piece.state == "alive":
                    temp2 = False
            for piece in dark_pieces:
                if piece.x == x-1 and piece.y == y+1 and piece.state == "alive":
                    temp2 = False
            x -= 1
            y += 1
        # getting all the moves towards bottom right corner, until one of the values is below 0
        x = self.x
        y = self.y
        temp3 = True
        while x < 7 and y < 7 and temp3:
            self.moves.append((x+1, y+1))
            for piece in light_pieces:
                if piece.x == x+1 and piece.y == y+1 and piece.state == "alive":
                    temp3 = False
            for piece in dark_pieces:
                if piece.x == x+1 and piece.y == y+1 and piece.state == "alive":
                    temp3 = False
            x += 1
            y += 1

            # these are replacable
        # removing the moves that are out of the board
        for move in self.moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                self.moves.remove(move)
        # removing the tiles that are already by allied pieces
        if self.color == 0:
            for piece in light_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)

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
        if self.state == "alive":
            screen.blit(self.image, (self.x*50, self.y*50))

    # queen uses a combination of rook and bishop moves, so I just copied the code from those classes
    def possible_moves(self):
        self.moves = []
        # getting the coordinates of the queen
        x = self.x
        y = self.y

        # getting all the moves towards top left corner, until one of the values is below 0
        temp = True
        while x > 0 and y > 0 and temp:
            self.moves.append((x-1, y-1))
            for piece in light_pieces:
                if piece.x == x-1 and piece.y == y-1 and piece.state == "alive":
                    temp = False
            for piece in dark_pieces:
                if piece.x == x-1 and piece.y == y-1 and piece.state == "alive":
                    temp = False
            x -= 1
            y -= 1
        # getting all the moves towards top right corner, until one of the values is below 0
        x = self.x
        y = self.y
        temp1 = True
        while x < 7 and y > 0 and temp1:
            self.moves.append((x+1, y-1))
            for piece in light_pieces:
                if piece.x == x+1 and piece.y == y-1 and piece.state == "alive":
                    temp1 = False
            for piece in dark_pieces:
                if piece.x == x+1 and piece.y == y-1 and piece.state == "alive":
                    temp1 = False
            x += 1
            y -= 1
        # getting all the moves towards bottom left corner, until one of the values is below 0
        x = self.x
        y = self.y
        temp2 = True
        while x > 0 and y < 7 and temp2:
            self.moves.append((x-1, y+1))
            for piece in light_pieces:
                if piece.x == x-1 and piece.y == y+1 and piece.state == "alive":
                    temp2 = False
            for piece in dark_pieces:
                if piece.x == x-1 and piece.y == y+1 and piece.state == "alive":
                    temp2 = False
            x -= 1
            y += 1
        # getting all the moves towards bottom right corner, until one of the values is below 0
        x = self.x
        y = self.y
        temp3 = True
        while x < 7 and y < 7 and temp3:
            self.moves.append((x+1, y+1))
            for piece in light_pieces:
                if piece.x == x+1 and piece.y == y+1 and piece.state == "alive":
                    temp3 = False
            for piece in dark_pieces:
                if piece.x == x+1 and piece.y == y+1 and piece.state == "alive":
                    temp3 = False
            x += 1
            y += 1

        # row and column system from the rook class
        # getting all the moves from x to 0
        x = self.x
        y = self.y
        temp4 = True
        while x > 0 and temp4:
            self.moves.append((x-1, y))
            # if there is a piece than the queen can't go further so the loop will stop
            for piece in light_pieces:
                if piece.x == x-1 and piece.y == y and piece.state == "alive":
                    temp4 = False
            for piece in dark_pieces:
                if piece.x == x-1 and piece.y == y and piece.state == "alive":
                    temp4 = False
            x -= 1
        # getting all the moves from x to 7
        x = self.x
        temp5 = True
        while x < 7 and temp5:
            self.moves.append((x+1, y))
            # if there is a piece than the queen can't go further so the loop will stop
            for piece in light_pieces:
                if piece.x == x+1 and piece.y == y and piece.state == "alive":
                    temp5 = False
            for piece in dark_pieces:
                if piece.x == x+1 and piece.y == y and piece.state == "alive":
                    temp5 = False
            x += 1

        # getting all the moves from y to 0
        x = self.x
        y = self.y
        temp6 = True
        while y > 0 and temp6:
            self.moves.append((x, y-1))
            for piece in light_pieces:
                if piece.x == x and piece.y == y-1 and piece.state == "alive":
                    temp6 = False
            for piece in dark_pieces:
                if piece.x == x and piece.y == y-1 and piece.state == "alive":
                    temp6 = False
            y -= 1
        # getting all the moves from y to 7
        y = self.y
        temp7 = True
        while y < 7 and temp7:
            self.moves.append((x, y+1))
            for piece in light_pieces:
                if piece.x == x and piece.y == y+1 and piece.state == "alive":
                    temp7 = False
            for piece in dark_pieces:
                if piece.x == x and piece.y == y+1 and piece.state == "alive":
                    temp7 = False
            y += 1
        
        # removing the moves that are out of the board
        for move in self.moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                self.moves.remove(move)
                
        # removing the tiles that are already by allied pieces
        if self.color == 0:
            for piece in light_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)
        else:
            for piece in dark_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)

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
        if self.state == "alive":
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
        # removing the moves that are out of the board
        for move in self.moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                self.moves.remove(move)
        # removing the tiles that are already by allied pieces
        if self.color == 0:
            for piece in light_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)
        else:
            for piece in dark_pieces:
                for move in self.moves:
                    if piece.x == move[0] and piece.y == move[1]:
                        self.moves.remove(move)

# Initialize the game
pygame.init()
# setting up the screen
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()

# setting the tile size, this will be mainly used later in the development for resizability
tile_size = 50

# loading the images and resizing them all
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
settings = pygame.image.load("settings.png")
resized_settings = pygame.transform.scale(settings, (tile_size, tile_size))

# custom cursor images
cursor = None
# images for the cursor
white_pawn = pygame.image.load("white_pawn.png")
resized_white_pawn = pygame.transform.scale(white_pawn, (tile_size//2, tile_size//2))
black_pawn = pygame.image.load("black_pawn.png")
resized_black_pawn = pygame.transform.scale(black_pawn, (tile_size//2, tile_size//2))
white_bishop = pygame.image.load("white_bishop.png")
resized_white_bishop = pygame.transform.scale(white_bishop, (tile_size//2, tile_size//2))
black_bishop = pygame.image.load("black_bishop.png")
resized_black_bishop = pygame.transform.scale(black_bishop, (tile_size//2, tile_size//2))
white_rook = pygame.image.load("white_rook.png")
resized_white_rook = pygame.transform.scale(white_rook, (tile_size//2, tile_size//2))
black_rook = pygame.image.load("black_rook.png")
resized_black_rook = pygame.transform.scale(black_rook, (tile_size//2, tile_size//2))
white_horse = pygame.image.load("white_horse.png")
resized_white_horse = pygame.transform.scale(white_horse, (tile_size//2, tile_size//2))
black_horse = pygame.image.load("black_horse.png")
resized_black_horse = pygame.transform.scale(black_horse, (tile_size//2, tile_size//2))
white_queen = pygame.image.load("white_queen.png")
resized_white_queen = pygame.transform.scale(white_queen, (tile_size//2, tile_size//2))
black_queen = pygame.image.load("black_queen.png")
resized_black_queen = pygame.transform.scale(black_queen, (tile_size//2, tile_size//2))
white_king = pygame.image.load("white_king.png")
resized_white_king = pygame.transform.scale(white_king, (tile_size//2, tile_size//2))
black_king = pygame.image.load("black_king.png")
resized_black_king = pygame.transform.scale(black_king, (tile_size//2, tile_size//2))

# setting up the timer
minutes = 0
seconds = 0

# setting up font for the texts
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

# varible used for reseting the colors of the tiles
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
custom_cursor = False

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

# creating a thread for the timer
timer_thread = threading.Thread(target=timer)
timer_on = True
move_time = [0, 0]

# main loop
running = True
# starting the timer
timer_thread.start()
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

    # if the cursor is custom, then a new cursor will be drawn
    if custom_cursor:
        # hiding the original cursor
        pygame.mouse.set_visible(False)
        # drawing the cursor image
        screen.blit(cursor, pygame.mouse.get_pos())
    else:
        # showing the original cursor
        pygame.mouse.set_visible(True)
    
    # drawing the score
    text = font.render(str(score1) + " x " +str(score2), True, (0, 0, 0))
    screen.blit(text, (500- text.get_width()/2, 50))

    # drawing a label displaying the current player
    text1 = font.render(str(current_player) + "'s turn", True, (0, 0, 0))
    screen.blit(text1, (500- text1.get_width()/2, 100))

    # drawing the settings button
    screen.blit(resized_settings, (500 - resized_settings.get_width()/2, 150))

    # drawing the timer
    if timer_on:
        text2 = font.render("Timer: "+str(minutes) +":"+ str(seconds), True, (0, 0, 0))
        screen.blit(text2, (500- text2.get_width()/2, 250))
    
    # checking for events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checking if the settings button was clicked
            x, y = pygame.mouse.get_pos()
            if x > 500 - resized_settings.get_width()/2 and x < 500 + resized_settings.get_width()/2 and y > 150 and y < 150 + resized_settings.get_height():
                settings_window()

            # determining the tile that was clicked, if it was clicked
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
                        if piece.state == "alive":
                            piece_selected = True
                            selected = piece
                            # setting the cursor to the piece that was selected
                            custom_cursor = True
                            if piece.type == "pawn":
                                cursor = resized_white_pawn
                            elif piece.type == "bishop":
                                cursor = resized_white_bishop
                            elif piece.type == "rook":
                                cursor = resized_white_rook
                            elif piece.type == "knight":
                                cursor = resized_white_horse
                            elif piece.type == "queen":
                                cursor = resized_white_queen
                            elif piece.type == "king":
                                cursor = resized_white_king

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
                        if piece.state == "alive":
                            piece_selected = True
                            selected = piece
                            # setting the cursor to the piece that was selected
                            custom_cursor = True
                            if piece.type == "pawn":
                                cursor = resized_black_pawn
                            elif piece.type == "bishop":
                                cursor = resized_black_bishop
                            elif piece.type == "rook":
                                cursor = resized_black_rook
                            elif piece.type == "knight":
                                cursor = resized_black_horse
                            elif piece.type == "queen":
                                cursor = resized_black_queen
                            elif piece.type == "king":
                                cursor = resized_black_king
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

            if not piece_selected:
                # reseting the colors
                for tile in board_tiles:
                    if tile.color == 2 or tile.color == 3:
                        for i in range(len(tiles_selected)):
                            if tile.x == tiles_selected[i][0] and tile.y == tiles_selected[i][1]:
                                tile.color = tile_selected_original_color[i]
                # reseting the cursor
                custom_cursor = False

            # checking if the player clicked on a possible move
            for move in available_moves:
                if move[0] == x and move[1] == y:

                    # if there is a piece in the tile for the move, it will be taken and marked as dead
                    for piece in light_pieces:
                        if piece.x == x and piece.y == y:
                            if piece.state == "alive":
                                piece.state = "dead"
                    for piece in dark_pieces:
                        if piece.x == x and piece.y == y:
                            if piece.state == "alive":
                                piece.state = "dead"

                    # moving the piece to the new tile
                    selected.x = x
                    selected.y = y

                    # reseting cursor
                    custom_cursor = False

                    # changing the player
                    if current_player == "light":
                        current_player = players[1]
                    else:
                        current_player = players[0]

                    # clearing the available moves
                    available_moves.clear()

                    # setting the tgiles to their original color
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
                    
                    # reseting timer
                    reset_timer()
    
    # updating the screen
    clock.tick(60)
    pygame.display.update()