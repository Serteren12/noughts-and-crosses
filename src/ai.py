class ai:
    def __init__(self):
        """

        This is where you define any variables you might want to use.
        When defining them, write them in the form self.(variable name).
        
        If you want to make some more functions, make sure to include "self" as
        a parameter and your variables will be included automaticly.

        To find out more about classes, go to https://www.w3schools.com/python/python_classes.asp.    
        
        """
        pass

    def turn(self, engine):
        """
        
        This is where you interface with the Noughts and Crosses engine.
        
        In order to make your turn, use the command I've given you at the bottom of this function,
        replacing X and Y with the co-ordinates you want to plot.

        If a space has not yet been taken, the value of engine.board[x, y] will be an empty string.
        
        Your program should *not* overwrite an exisiting move, so try and add some protection to make
        sure this doesn't happen.

        """
        x = 0
        y = 0

        engine.board[x, y] = "X"
        return engine