"""
This program is a command line version of battleship. It is played against the computer, with the 
player making guesses to where the computer has placed it's ships. There is set number of turns 
that the player has to find all of the battleships. A class which the player uses to interact with 
the game is imported.
"""
from random import choice
from Battleship_Player import HumanPlayer
from time import sleep
# the game class is created, containing the functions to create the board, place ships, 
# take guesses, check for hits/misses, and check for win/loss
class Battleship:
    def __init__(self):
        self.board = [([" "] * 10) for i in range(10)]
        self.current_winner = None
        self.available_positions = []
        for m in range(len(self.board)):
            for n in range(len(self.board)):
                self.available_positions.append((m, n))
        self.all_ship_positions = []
        self.individual_ships = []
        self.fill_ocean()
    # print the ship in the command line
    def print_board(self):
        print("\t  1   2   3   4   5   6   7   8   9   10")
        for x, row in enumerate(self.board):
            print("     " + str(x+1) + "\t| " + " | ".join(row) + " |")
    # find a direction a given ship length can be placed in from it's starting position
    def arrange_ship(self, first, second, direction, length):
        points = set()
        if direction == "h":
            for i in range(1, length):
                x = first, second + i
                if x not in self.available_positions:
                    for j in range(1, length):
                        x = first, second - j
                        if x not in self.available_positions:
                            return points
                        points.add(x)
                        if len(points) == (length - 1):
                            return points
                points.add(x)
                if len(points) == (length - 1):
                    return points
        if direction == "v":
            for i in range(1, length):
                x = first + i, second
                if x not in self.available_positions:
                    for j in range(1, length):
                        x = first - j, second
                        if x not in self.available_positions:
                            return points
                        points.add(x)
                        if len(points) == (length - 1):
                            return points
                points.add(x)
                if len(points) == (length - 1):
                    return points
    # take a starting position for a ship, and find an orientation for it, if it is not possible, 
    # a new position will be used until a valid layout for a ship can be found
    def create_ship(self, length):
        while True:
            startposition = choice(self.available_positions)
            orientation = choice(["h", "v"])
            start_row, start_col = startposition[0], startposition[1]
            shippoints = set()
            ship = self.arrange_ship(start_row, start_col, orientation, length)
            if len(ship) == (length - 1):
                shippoints.add(startposition)
                for x in ship:
                    shippoints.add(x)
                return shippoints
            else:
                orientation = "h" if orientation == "v" else "v"
                ship = self.arrange_ship(start_row, start_col, orientation, length)
                if len(ship) == (length - 1):
                    shippoints.add(startposition)
                    for x in ship:
                        shippoints.add(x)
                    return shippoints
                else:
                    break
    # list the length of each ship being placed, create each ship and store the positions each ship covers
    def make_ships(self):
        ship_lengths = [5, 4, 4, 3, 2]
        for e in ship_lengths:
            ind_ship = []
            ship = self.create_ship(e)
            for y in ship:
                self.all_ship_positions.append(y)
                ind_ship.append(y)
                self.available_positions.remove(y)
            self.individual_ships.append(ind_ship)
    # run the functions to place the ships on the board
    def fill_ocean(self):
        self.make_ships()
        return True
    # checks for a ship being sunk
    def sunk_battleship(self, guess):
        for target in self.individual_ships:
            if guess in target:
                target.remove(guess)
            if len(target) == 0:
                self.individual_ships.remove(target)
                return True
        return False
    # check if the guess made is a hit, miss, and if it is a win
    def make_guess(self, guess):
        guess = guess
        if self.board[guess[0]][guess[1]] == " ":
            p1, p2 = guess[0] + 1, guess[1] + 1
            print(f"\nPlayer fires on {p1}, {p2}!")
            sleep(0.5)
            if guess in self.all_ship_positions:
                self.board[guess[0]][guess[1]] = "X"
                print("\nHit!")
                self.all_ship_positions.remove(guess)
                sunk = self.sunk_battleship(guess)
                if sunk is True:
                    print("\nYou have sunk a battleship!")
            else:
                self.board[guess[0]][guess[1]] = "O"
                print("\nMiss!")
            if self.winner():
                self.current_winner = "Player"
            return True
        return False
    # check for winner
    def winner(self):
        if len(self.all_ship_positions) == 0:
            return True
        else: return False
# create a function to run the game, parameters are the game class, player class, and to print the game
def play(game, player, print_game=True):
    if print_game:# print the board, set the turns
        game.print_board()
        turn = 67# the actual number of turns will be turn - 1
        sec = 0.5
    while True:
        if turn > 0:# run the game until there is a win or no turns left
            turn -= 1
            print(f"\nYou have {turn} shots remaining...")
            sleep(sec)
            guess = player.get_guess()
            sleep(sec)
            if game.make_guess(guess):
                if print_game:
                    sleep(sec)
                    game.print_board()
                    print("")
                    sleep(sec)
                if game.current_winner:
                    return print("\nPlayer has sunk all of the ships! Player Wins!")
        else: return print("\nOut of turns... Better luck next time!")
# assign the player and game class, and input parameters to the play function
if __name__ == "__main__":
    player = HumanPlayer()
    battle = Battleship()
    play(battle, player, print_game=True)