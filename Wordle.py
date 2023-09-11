# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    def enter_action(s):
        # s is the string that the user enters all strings are lowered in the list
        if s.lower() in FIVE_LETTER_WORDS:
            currentRow = gw.get_current_row()
            # if current row is greater than or equal to total rows then the user is out of guesses
            if currentRow < N_ROWS - 1:
                currentCol = 0
                # while the current column is less than max columns set the square letter to the current row and column
                while currentCol < N_COLS:
                    gw.set_square_letter(currentRow, currentCol, s[currentCol])
                    currentCol += 1
                gw.set_current_row(currentRow + 1)
            else:
                gw.show_message("You have reached the end of the board. You lose.")
        else:
            gw.show_message("That is not a valid word.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
