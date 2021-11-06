# Copilot CLI Games

This repository contains a series of simple games, ie. tic-tac-toe, hangman and guess-a-number.
They are written as Python CLI programs that take user input via `stdin`. They are implemented by Github Copilot with some human guidance.


## Performance review

In the following section of this document we specify how well Github Copilot did for every game.

1. Hangman (`hangman.py`): Github Copilot could generate the "main" function `game()` containing the game loop with no issues, but referenced non-existing helper functions. These it could generate without problems once a human started typing their def header.
   
2.  Guess-a-number (`number.py`): Github Copilot generated the `main()` function directly.
    
3. Tic-tac-toe (`tic-tac-toe.py`): Github Copilot had some major difficulties with this game. At the beginning we tried the approach that worked with the previous two games, as in letting Copilot know what game we were playing and waiting for it to generate the game loop. This was done rather badly and did not work at all. As such, after about 4 attempts we started writing the game loop ourselves. The function `print_board()` was written entirely by us. The game loop structure was written by us, as in we typed some comments about what to do next and Github Copilot could generate the code. Interestingly it was finally able to pickup the final intention of checking if the game was over and generated the final part directly. Remarkably it could also generate the name and body of the function `map_number_to_coordinates()`, but failed to realize user (string) input had to be converted to `int`.
   
4. Quiz (`quiz.py`): Github Copilot could work out a format to store the questions and answers, but failed to generate code within the `main()` function correctly, as in read in the format it had produced, although it started with the right approach. Interestingly it caught a bug in my own code (I had forgotten to add the last batch of buffered answers once the loop terminates). Despite the deserialization issues, it was able to generate the rest of the code (`ask_question()` and `quiz()`) correctly, and had the interesting idea of displaying the score. One thing that is bugging me, however, is that Copilot decieded that the correct answer would always be the first, which is not supposed to be the case. This corroborates my conclusion (see below).

5. Nim (`nim.py`): Github Copilot really needed to be told what to do exactly. When the instructions were not clear, it would often guess very close but still wrong. Sometimes one line hint would be enough for it to pick up on the procedure and emit more comment lines with what it thought would need to be done. It is interesting that Copilot itself chose to go with an object oriented approach, starting out by instantiting a not yet existing Pyramid() object.

In general, a human was required to write the comment about asking to play again and Github Copilot could generate the code following that.

All in all, we can confirm Github Copilot is a valuable asset to achieve "small programming", as in, finding a "short" algorithm and/or implementing it. For complex problems though, the logic/structure of the program had to be at least hinted to by a human as Copilot could sometimes only work out the mechanical implementation of the next step without picking up on the grander design, and even then it would often need to be told what exactly should be done to achieve the next step.


## License

The code is released into the public domain (see `UNLICENSE` file).