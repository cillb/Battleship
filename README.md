# Battleship

This is a command line version of the game battleship. The user is playing against a computer opponent that makes random guesses against them. Indexed boards for both players are printed out for the user to see throughout the game. Input from the user is prompted to make guesses against the computer. The game runs until a player has sunk all of the other's ships.

## Player

A player module is included, containing multiple classes that are imported into the game module. A base player class sets up the overall version of a "Player". There are two more classes, a human player and computer player, which inherit the base class.

These classes based on whether the user needs to provide input to the program, how are guesses made against an opponent etc. Each player class stores it's own information on their board, ships, guesses made. Currently the computer will only make random guesses. If it hits a ship it does not follow up with specific actions.

## Game

The game module contains the game class, which contains functions of the game, and then a game function which runs the game in it's entirety. The player module is imported and two players, a human and computer player are created.

The game class holds the functions that make the game work, such as print a player's board to show any changes to it, taking a guess from a player and playing it against the oppoonents board, checking if a ship was sunk when it is hit, and checking for a winner when a ship is sunk.

The game function runs the functions in the correct sequence until a winner is detected.