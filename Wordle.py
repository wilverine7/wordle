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
        if s.lower() in FIVE_LETTER_WORDS:
            currentRow = gw.get_current_row()
            if currentRow < N_ROWS - 1:
                currentCol = 0
                while currentCol < N_COLS:
                    gw.set_square_letter(currentRow, currentCol, s[currentCol])
                    currentCol += 1
                gw.set_current_row(currentRow + 1)
                # gw.show_message(row)
            else:
                gw.show_message("You have reached the end of the board. You lose.")
        else:
            gw.show_message("That is not a valid word.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
