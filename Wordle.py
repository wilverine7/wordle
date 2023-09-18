# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    solution = random.choice(FIVE_LETTER_WORDS)
    print(solution)
    correct_guess = False  # Track if the user has guessed the word correctly
    rows_remaining = N_ROWS  # Track the remaining rows

    # def enter_action(s):
    #     # s is the string that the user enters all strings are lowered in the list
    #     if s.lower() in FIVE_LETTER_WORDS:
    #         currentRow = gw.get_current_row()
    #         # if current row is greater than or equal to total rows then the user is out of guesses
    #         if currentRow < N_ROWS - 1:
    #             currentCol = 0
    #             # while the current column is less than max columns set the square letter to the current row and column
    #             while currentCol < N_COLS:
    #                 gw.set_square_letter(currentRow, currentCol, s[currentCol])
    #                 currentCol += 1
    #             gw.set_current_row(currentRow + 1)
    #         else:
    #             gw.show_message("You have reached the end of the board. You lose.")
    #     else:
    #         gw.show_message("That is not a valid word.")

    def enter_action(s):
        nonlocal correct_guess
        nonlocal rows_remaining

        # s is the string that the user enters, all strings are lowered in the list
        if s.lower() in FIVE_LETTER_WORDS:
            solution_word = list(solution)
            entered_word = list(s.lower())

            currentRow = gw.get_current_row()

            # Ensure the entered word is exactly 5 characters long
            if len(entered_word) == N_COLS:
                currentCol = 0

                # Iterate through the entered word and compare with the solution word
                for i in range(N_COLS):
                    square_letter = entered_word[i]
                    solution_letter = solution_word[i]

                    if square_letter == solution_letter:
                        # Set the tile color to green for correct letters
                        gw.set_square_color(currentRow, currentCol, "#66BB66")  # Green
                    elif square_letter in solution_word:
                        # Set the tile color to yellow for misplaced letters
                        gw.set_square_color(currentRow, currentCol, "#CCBB66")  # Yellow
                    else:
                        # Set the tile color to grey for letters that don't appear
                        gw.set_square_color(currentRow, currentCol, "#999999")  # Grey

                    currentCol += 1

                gw.set_current_row(currentRow + 1)
                rows_remaining -= 1

                if entered_word == solution_word:
                    correct_guess = True  # User guessed the word correctly
            else:
                gw.show_message("The entered word must be exactly 5 characters long.")
        else:
            gw.show_message("That is not a valid word.")

        # Check if the game should stop
        if correct_guess:
            gw.show_message("Great job, Bro!")
        elif rows_remaining == 0:
            gw.show_message("You suck! The word was: " + solution)

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
