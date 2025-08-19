import random

class ai:
    def __init__(self):
        # This is the memory of the AI.
        # It stores which moves were good or bad in different board positions.
        self.memory = {}
        self.game_history = []

    def turn(self, engine):
        # Convert the board into a string so we can save it in memory
        state = str(engine.board)

        # Find all empty spaces on the board
        available_moves = [(x, y) for x in range(3) for y in range(3) if engine.board[x, y] == ""]

        # If this board position has not been seen before, add it to memory
        if state not in self.memory:
            self.memory[state] = {move: 0 for move in available_moves}

        # With a 30% chance, make a random move (exploration)
        if random.random() < 0.3:
            move = random.choice(available_moves)
        else:
            # Otherwise choose the move with the best score so far
            moves_scores = self.memory[state]
            move = max(available_moves, key=lambda m: moves_scores.get(m, 0))

        # Place "X" on the board in the chosen position
        x, y = move
        engine.board[x, y] = "X"

        # Save this move in the game history so we can reward or punish it later
        self.game_history.append((state, move))

        return engine

    def update_memory(self, result):
        """
        This is called after the game finishes.
        result = +1 if AI wins, -1 if AI loses, 0 for a draw
        """
        for (state, move) in self.game_history:
            if state not in self.memory:
                self.memory[state] = {}
            if move not in self.memory[state]:
                self.memory[state][move] = 0

            # Add the result to the score of this move
            self.memory[state][move] += result

        # Reset history for the next game
        self.game_history = []
