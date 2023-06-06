"""
This runs a command line version of battleship. A computer opponent is used, it only plays random guesses.
The boards for both players are printed out, hits are marked with 'X' and misses are marked with 'O'.
A class for a human player and a computer player is created from the imported classes in Battleship_Player.
"""
from random import choice
from Battleship_Player import *
from time import sleep
# the game class is created, containing the functions to create the board, place ships, 
# take guesses, check for hits/misses, and check for win/loss
class Battleship:
    def __init__(self):
        self.current_winner = None
    # print the ship in the command line
    def print_board(self, p2):
        print(f"\n\n\t\t{p2.name.upper()} BOARD\n")
        print("\t  1   2   3   4   5   6   7   8   9   10")
        for x, row in enumerate(p2.board):
            print("     " + str(x+1) + "\t| " + " | ".join(row) + " |")
    # checks for a ship being sunk
    def sunk_battleship(self, p2: Player, guess: tuple):
        for target in p2.ships:
            if guess in target:
                target.remove(guess)
            if len(target) == 0:
                p2.ships.remove(target)
                return True
        return False
    # check if the guess made is a hit, miss, and if it is a win
    def take_guess(self, guess, p1: Player, p2: Player):
        guess = guess
        if p2.board[guess[0]][guess[1]] == " ":
            g1, g2 = guess[0] + 1, guess[1] + 1
            print(f"\n{p1.name} fires on {g1}, {g2}!")
            sleep(0.5)
            if guess in p2.ship_points:
                p2.board[guess[0]][guess[1]] = "X"
                print("\nHit!")
                p2.ship_points.remove(guess)
                sunk = self.sunk_battleship(p2, guess)
                if sunk is True:
                    print("\nYou have sunk a battleship!")
            else:
                p2.board[guess[0]][guess[1]] = "O"
                print("\nMiss!")
            if self.winner(p2):
                self.current_winner = p1.name
            return True
        return False
    # check for winner
    def winner(self, p2: Player):
        if len(p2.ship_points) == 0:
            return True
        else: return False
# create a function to run the game, parameters are the game class, player class, and to print the game
def play(game: Battleship, player: Player, comp: Player):
    sec = 0.8
    print("Let's Play Battleship!\nYou are playing against the computer.\n")
    player.place_ships()
    comp.place_ships()
    game.print_board(player)
    game.print_board(comp)
    sleep(sec)
    current_player, opp = player, comp
    while True:
        print("\n-----------------------------------------------------------")
        print(f"\n{current_player.name} Turn.")
        sleep(sec)
        guess = current_player.make_guess()
        sleep(sec)
        game.take_guess(guess=guess, p1=current_player, p2=opp)
        sleep(sec)
        game.print_board(opp)
        sleep(sec)
        if game.current_winner:
            return print(f"\n{game.current_winner} Wins!")
        current_player, opp = opp, current_player
# assign the player and game class, and input parameters to the play function
if __name__ == "__main__":
    player = HumanPlayer()
    comp = ComputerPlayer()
    game = Battleship()
    play(game=game, player=player, comp=comp)