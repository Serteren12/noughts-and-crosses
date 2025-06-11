class engine:
    def __init__(self, ai):
        self.ai = ai
        self.setup()

    def setup(self):
        # Assembles the game board using a 2D array
        row1 = [
            "-",
            "-",
            "-"
        ]

        row2 = [
            "-",
            "-",
            "-"
        ]

        row3 = [
            "-",
            "-",
            "-"
        ]

        self.board = [
            row1,
            row2,
            row3
        ]

    def print_board(self):
        # Prints each of the "row" lists
        for item in self.board:
            print(item)

    def play_game(self):
        # Loops until the game is complete
        playing = True
        cycle = 1
        
        while playing:
            print("")
            self.print_board()
            print("")

            # Determines current self.player
            if (cycle % 2) == 1:
                self.player = "X"
                print("Crosses' turn!")
                self = self.ai.turn(self)
                cycle += 1
            
            else:
                # Inputs and sanitises the X and Y co-ordinates
                self.player = "0"
                print("Nought's turn!")
                
                valid = False
                while valid == False:
                    self.x = input("Enter X co-ordinate: ")
                    valid = self.input_check(self.x)
                self.x = int(self.x) - 1
                
                valid = False
                while valid == False:
                    self.y = input("Enter Y co-ordinate: ")
                    valid = self.input_check(self.y)
                self.y = int(self.y) - 1 
            
                # Marks the input on the board
                if self.board[self.y][self.x] == "-":
                    cycle += 1
                    valid = True
                    self.board[self.y][self.x] = self.player
                else:
                    print("Space already taken!")

            result = self.win_check()
            
            if result == "draw":
                print("The game was a draw!")
                self.print_board()
                playing = False

            elif result == "0":
                print("Noughts win!")
                self.print_board()
                playing = False
            
            elif result == "X":
                print("Crosses win!")
                self.print_board()
                playing = False

    def input_check(self, input):
        # Sanitises the input
        valid = True
        try:
            int(input)
        except:
            valid = False

        if valid == True:
            input = int(input)
            valid = (1 <= input <= 3)
        
        return valid
    
    def win_check(self):
        # Checks if either player has won
        
        # Rows
        for row in self.board:
            noughts = 0
            crosses = 0
            for item in row:
                if item == "0":
                    noughts += 1
                elif item == "X":
                    crosses += 1
            if noughts == 3:
                return "0"
            elif crosses == 3:
                return "X"
            
        # Columns
        for column in range(0,3):
            noughts = 0
            crosses = 0
            for row in range(0,3):
                if self.board[row][column] == "0":
                    noughts += 1
                elif self.board[row][column] == "X":
                    crosses += 1
            if noughts == 3:
                return "0"
            elif crosses == 3:
                return "X"
                
        # Diagonals
        for num in range(1,3):
            noughts = 0
            crosses = 0
            if num == 1:
                if self.board[0][0] == "0" and self.board[1][1] == "0" and self.board[2][2] == "0":
                    return "0"
                elif self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X":
                    return "X"
            elif num == 2:
                if self.board[0][2] == "0" and self.board[1][1] == "0" and self.board[2][0] == "0":
                    return "0"
                elif self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X":
                    return "X"

        # Checks for a draw
        space = False
        for list in self.board:
            for item in list:
                if item == "-":
                    space = True
        if space == False:
            return "draw"

