# Battleship

This is a command line version of the game battleship. An indexed board is printed to the user, and the user is prompted to input a row and column index separately. The game functions by having the player make guesses against the computers board. There are a set number of turns that the player has to take before the game ends in a loss.

## Player

A player module is included, containing a Player class that is imported into the game module. The player class takes the input of a row and column from the player. It ensures only valid inputs are put through to the game class functions.

## Game

The game module contains a game class, which holds the logic of the game. It initialises the board, a list of the board's coordinates, and places ships down on the board.

A game function is also in the module, which takes parameters of the game and player classes, and contains the sequence of functions that makes the game run for the user.