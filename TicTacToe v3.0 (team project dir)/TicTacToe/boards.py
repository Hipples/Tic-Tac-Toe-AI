"""TODO: Module docstring...."""
import numpy as np
from players import Players

class TicTacToeBoard:
    """TODO: class docstring...."""

    def __init__(self):
        """Initialize an empty game board and default values."""
        self.board = []  # empty gameboard
        self.default = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # default board size

    def create_board(self):
        """Create a 3x3 gameboard."""
        for i in np.arange(1, 10).astype(str):  # nine numbers, as strings, because we replace
            self.board.append(i)  # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns    

    def display_board(self):
        """Display current gameboard."""
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         |')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------')

    def reset_board(self):
        """Reset the gameboard."""
        self.board = [] # reset to an empty list

    def get_coords(self, player):
        """Determines the coordinates of the 'empty' square value provided."""
        player = Players()
        move = player.player_turn(player) # retrieve player move from human_moves() method
        coords = [] # declare empty list to store move coordinates
        coords = np.where(self.board == move) # determine move coordinates
        return coords # return move coordinates

    def place_marker(self, row, col, player):
        """Places the player marker (X or O) in the designated square."""
        self.board[row][col] = player # use move coordinates to place marker in the chosen square

    def player_move(self, player):
        player = Players()
        """Capture, record, and fulfill human player moves while handling exceptions."""
        while True: # exception catching loop
            try: # attempt to initialize coords, by retrieving the player's input,
                coords = self.get_coords(player) # through get_coords() method,
                row, col = int(coords[0]), int(coords[1]) # then assign the proper index of the move
            except KeyboardInterrupt: # enable Ctrl + c to end program during player input
                print("\n\n\tGood bye!") # program says good bye,
                exit() # then ends
            # except: # continue looping until valid input is accepted
            #     print("\n\tBad input! Try again.\n") # announce when input is invalid
            else: # otherwise, reverse engineer our player move by using our determined index
                move = self.board[row][col] # and assign it to move
                with open(player.match_records, 'a') as record: # then open our match records and
                    record.write(f"{player}:{move} ") # append each valid player move
                self.place_marker(row, col, player) # as it happens
                return False # before ending our loop

    def is_board_full(self):
        """Determines if gameboard is full (DRAW)."""
        for row in self.board: # for each row on the board,
            for square in row: # and for each square in said row,
                if square in self.default: # if the square value is in our list of empty squares
                    return False # return False
        return True # otherwise return True

    def is_winner_by_row(self, board, player):
        """Checks for horizontal winning patterns."""
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == player:
                    return True

    def is_winner_by_col(self, board, player):
        """Checks for vertical winning patterns."""
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == player:
                    return True

    def is_winner_by_diag(self, board, player):
        """Checks for diagonal winning patterns."""  
        # check descending diagonal for win
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == player:
                return True
        # check ascending diagonal for win
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == player:
                return True

    def is_winner(self, board, player):
        win = False
        if self.is_winner_by_row(board, player):
            win = True
        if self.is_winner_by_col(board, player):
            win = True
        if self.is_winner_by_diag(board, player):
            win = True
        return win
