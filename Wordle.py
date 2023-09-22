# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter as tk
from tkinter import messagebox
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def show_language_theme_dialog():
    def start_game():
        language = language_var.get()
        theme = theme_var.get()
        dialog.destroy()
        wordle(language, theme)

    dialog = tk.Toplevel()
    dialog.title("Language and Theme Selection")
    dialog.geometry("500x700")

    # Language Selection
    language_label = tk.Label(dialog, text="Select Language:")
    language_label.pack()
    language_var = tk.StringVar()
    language_var.set("English")  # Default selection
    language_options = ["English", "Italian"]
    language_menu = tk.OptionMenu(dialog, language_var, *language_options)
    language_menu.pack()

    # Theme Selection
    theme_label = tk.Label(dialog, text="Select Theme:")
    theme_label.pack()
    theme_var = tk.StringVar()
    theme_var.set("Light")  # Default selection
    theme_options = ["Light", "Gross"]
    theme_menu = tk.OptionMenu(dialog, theme_var, *theme_options)
    theme_menu.pack()

    # Start Button
    start_button = tk.Button(dialog, text="Start Game", command=start_game)
    start_button.pack()

    dialog.mainloop()


def wordle(language, theme):
    solution = random.choice(FIVE_LETTER_WORDS)
    print(solution)
    if theme == "Light":
        CORRECT_COLOR = "#66BB66"  # Light green for correct letters
        PRESENT_COLOR = "#CCBB66"  # Brownish yellow for misplaced letters
        MISSING_COLOR = "#999999"  # Gray for letters that don't appear

    elif theme == "Gross":
        CORRECT_COLOR = "#e07c00"  # Dark green for correct letters
        PRESENT_COLOR = "#ff0601"  # Dark yellow for misplaced letters
        MISSING_COLOR = "#92fffd"  # Dark Gray for letters that don't appear

    def enter_action(s):
        if s.lower() == solution:
            currentRow = gw.get_current_row()
            currentCol = 0
            while currentCol < N_COLS:
                gw.set_square_letter(currentRow, currentCol, s[currentCol])
                gw.set_square_color(currentRow, currentCol, CORRECT_COLOR)
                gw.set_key_color(s[currentCol], CORRECT_COLOR)

                currentCol += 1
            gw.show_message("You win!")
        elif s.lower() in FIVE_LETTER_WORDS:
            currentRow = gw.get_current_row()
            currentCol = 0

            while currentCol < N_COLS:
                gw.set_square_letter(currentRow, currentCol, s[currentCol])
                if s[currentCol].lower() == solution[currentCol]:
                    gw.set_square_color(currentRow, currentCol, CORRECT_COLOR)
                    gw.set_key_color(s[currentCol], CORRECT_COLOR)
                currentCol += 1

            letter_counts_solution = {}
            letter_counts_guess = {}

            for i in range(N_COLS):
                letter_solution = solution[i].lower()
                letter_guess = s[i].lower()

                if letter_solution == letter_guess:
                    continue

                letter_counts_solution[letter_solution] = (
                    letter_counts_solution.get(letter_solution, 0) + 1
                )
                letter_counts_guess[letter_guess] = (
                    letter_counts_guess.get(letter_guess, 0) + 1
                )

            currentCol = 0
            while currentCol < N_COLS:
                color = gw.get_square_color(currentRow, currentCol)
                if s[currentCol].lower() in solution and color != CORRECT_COLOR:
                    if letter_counts_solution.get(
                        s[currentCol].lower(), 0
                    ) >= letter_counts_guess.get(s[currentCol].lower(), 0):
                        gw.set_square_color(currentRow, currentCol, PRESENT_COLOR)
                        gw.set_key_color(s[currentCol], PRESENT_COLOR)
                    else:
                        gw.set_square_color(currentRow, currentCol, MISSING_COLOR)
                        gw.set_key_color(s[currentCol], MISSING_COLOR)
                elif s[currentCol].lower() not in solution:
                    gw.set_square_color(currentRow, currentCol, MISSING_COLOR)
                    gw.set_key_color(s[currentCol], MISSING_COLOR)
                currentCol += 1

            gw.set_current_row(currentRow + 1)
        elif s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("That is not a valid word.")

    gw = WordleGWindow(language, theme)
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    show_language_theme_dialog()
