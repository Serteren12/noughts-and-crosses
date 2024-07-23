class engine:
    def __init__(self):
        self.setup()
        self.play_game()

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
            # Determines current player
            if (cycle % 2) == 1:
                player = "X"
                print("Crosses' turn!")
            
            else:
                player = "0"
                print("Nought's turn!")
            
            print("")
            self.print_board()
            print("")

            # Inputs and sanitises the X and Y co-ordinates
            valid = False
            while valid == False:
                x = input("Enter X co-ordinate: ")
                valid = self.input_check(x)
            x = int(x) - 1
            
            valid = False
            while valid == False:
                y = input("Enter Y co-ordinate: ")
                valid = self.input_check(y)
            y = int(y) - 1 

            # Marks the input on the board
            if self.board[y][x] == "-":
                cycle += 1
                valid = True
                self.board[y][x] = player
            else:
                print("Space already taken!")

            if self.win_check() == "draw":
                print("The game was a draw!")
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
        # Checks all spaces are filled
        space = False
        for list in self.board:
            for item in list:
                if item == "-":
                    space = True
        if space == False:
            return "draw"

engine = engine()