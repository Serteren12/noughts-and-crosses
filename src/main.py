"""

This is the main script you should run when testing your code.

If you want to take a peek into the engine script, feel free! I've added some
comments to help make some sense of my code, however if something confuses you let
me know and I'll do my best to help!

Please don't edit the engine script, if there are any problems or if you need some
help, email me at theotsmith@protonmail.com. I may be away so it might be a little while
before you get a response.

"""

from engine import engine
from ai import ai

engine = engine(ai())
engine.play_game()
