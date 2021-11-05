# Copilot CLI Games

This repository contains a series of simple games, ie. tic-tac-toe, hangman and guess-a-number.
They are written as Python CLI programs that take user input via `stdin`. They are implemented by Github Copilot with some human guidance.


## Performance review

In the following section of this document we specify how well Github Copilot did for every game.

1. Hangman (`hangman.py`): Github Copilot could generate the "main" function `game()` containing the game loop with no issues, but referenced non-existing helper functions. These it could generate without problems once a human started typing their def header.
2.  Guess-a-number (`number.py`): Github Copilot generated the `main()` function directly. 
3. Tic-tac-toe (`tic-tac-toe.py`): Github Copilot had some major difficulties with this game. At the beginning we tried the approach that worked with the previous two games, as in letting Copilot know what game we were playing and waiting for it to generate the game loop. This was done rather badly and did not work at all. As such, after about 4 attempts we started writing the game loop ourselves. The function `print_board()` was written entirely by us. The game loop structure was written by us, as in we typed some comments about what to do next and Github Copilot could generate the code. Interestingly it was finally able to pickup the final intention of checking if the game was over and generated the final part directly. Remarkably it could also generate the name and body of the function `map_number_to_coordinates()`, but failed to realize user (string) input had to be converted to `int`.

In general, a human was required to write the comment about asking to play again and Github Copilot could generate the code following that.

All in all, we can confirm Github Copilot is a valuable asset to achieve "small programming", as in, finding a "short" algorithm and/or implementing it. For complex problems though, the logic/structure of the program had to be at least hinted to by a human as Copilot could sometimes only work out the mechanical implementation of the next step without picking up on the grander design.


## License

The code is released into the public domain (see `UNLICENSE` file).