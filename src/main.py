"""

This is the main script you should run when testing your code.

If you want to take a peek into the engine script, feel free - just don't edit it! I've added some
comments to help make some sense of my code, however if something confuses you let
me know and I'll do my best to help!

"""

from engine import engine
from ai import ai

engine = engine(ai())
engine.play_game()
