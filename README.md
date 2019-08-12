# Letter_game

To run the python file :
1. comman prompt:  C:\python27\python.exe guess.py
2. use the pycharm software.


Four letter word finder using Python

The user will be asked to guess 4-letter words. To make this realistic, we must utilize a large list of possible words. For this purpose, I have provided a text file containing 4030 4-letter English words.
Your Python application will read the file from disk and load all strings into a data structure of your choice. To simplify things, you should place the file with the 4-letter words in the same folder as
your Python files.
The program will randomly select a string and ask the user to guess the string. Initially, the string will be listed as “----“. The user will have the choice to try to guess the string directly or to guess a
letter at a time. The initial screen might look like this:

** The great guessing game **
Current Guess: ----

g = guess, t = tell me, l for a letter, and q to quit

If the letter option is chosen (“l”), the user will enter a possible letter and the program will indicate
how many such letters there are in this string. It will then replace one or more of the “-“ values with

this letter and redisplay the result. It might look like this, if ‘a’ is chosen:
l
Enter a letter:
a
You found 1 letters
Current Guess: --a

g = guess, t = tell me, l for a letter, and q to quit
This process continues until the user either gets the answer right or gives up.This process continues until the user either gets the answer right or gives up.

