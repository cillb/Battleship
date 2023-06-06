"""
This program contains a base player class, which is inherited by human player and computer player classes.
The human player class takes input to choose placements for the ships, and to make guesses against the computer.
The inputs are validated and the player is notified of errors. The computer player only makes valid guesses and 
is written to only successfully place valid ships on it's board.
"""
from random import choice
# the base class for a player, attributes are the name, lists to store ship positions and check if a ship is hit, 
# and when a ship is sunk, the player's board that is printed during the game, and points on the board that are not covered by ships
class Player:
    def __init__(self):
        self.name = ""
        self.ship_points = []
        self.ships = []
        self.board = [([" "] * 10) for i in range(10)]
        self.available_points = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.available_points.append((i,j))
    # the two base functions for a player to perform is to place ships at the start of the game, and make guesses during
    def place_ships(self):
        pass

    def make_guess(self):
        pass
# the human player sets the name attribute, and adds a new attribute to remember if a guess had already been made
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Player"
        self.guesses_made = set()
    # the player is prompted to choose a start point for the ships, and whether to place it across or down the board, the input has to be validated to ensure no errors
    def place_ships(self):
        new_board = [([" "] * 10) for i in range(10)]
        def print_ships(new_board=new_board):# print the board with each new addition so the player knows where a ship can be placed
            print("\t  1   2   3   4   5   6   7   8   9   10")
            for x, row in enumerate(new_board):
                print("     " + str(x+1) + "\t| " + " | ".join(row) + " |")
        ship_lengths = [5, 4, 4, 3, 2]
        Direction_Error = ValueError("Please enter either 'd' or 'a'.")
        RangeError = ValueError("Please enter a position on the board.")
        NotAvailableError = ValueError("Please place ship on available points.")
        for length in ship_lengths:
            ship = []
            valid_placement = False
            while not valid_placement:
                print(f"\nPlacing ship, {length} spaces long.")
                startrow, startcol = input("Enter the starting row (1-10):\t\t"), input("Enter the starting column (1-10):\t")
                try:
                    direction = input("Place ship down or across? (d/a)\t").lower()
                    if direction not in ["d", "a"]:
                        raise Direction_Error
                    startpoint = int(startrow) - 1, int(startcol) - 1
                    if direction == "d":
                        for i in range(length):
                            if (startpoint[0]+i,startpoint[1]) not in self.available_points:
                                raise NotAvailableError
                    else:
                        for i in range(length):
                            if (startpoint[0],startpoint[1]+i) not in self.available_points:
                                raise NotAvailableError
                    for point in startpoint:
                        if point < 0 or point > 9:
                            raise RangeError
                    valid_placement = True
                except ValueError as ve:
                    if ve is RangeError:
                        print(f"{str(ve)}")
                    elif ve is Direction_Error:
                        print(f"{str(ve)}")
                    elif ve is NotAvailableError:
                        print(f"{str(ve)}")
                    else: print("Invalid placement, please try again.")
            if direction == "d":
                for point in [(startpoint[0]+i, startpoint[1]) for i in range(length)]:
                    ship.append(point)
                    self.available_points.remove(point)
                    new_board[point[0]][point[1]] = "X"
            else:
                for point in [(startpoint[0],startpoint[1]+i) for i in range(length)]:
                    ship.append(point)
                    self.available_points.remove(point)
                    new_board[point[0]][point[1]] = "X"
            self.ships.append(ship)
            self.ship_points.extend(ship)
            print_ships()
        print("\n-----------------------------------------------------------\n")
    # take input from the player to fire on the opponents board, the input is validate to ensure it is a legitimate move
    def make_guess(self):
        valid_guess = False
        range_error = ValueError("Please enter a postion on the board.")
        already_made_error = ValueError("You have already made that guess. Try again...")
        while not valid_guess:
            guess_row = input("\nEnter your row guess (1-10):\t")
            guess_col = input("\nEnter your column guess (1-10):\t")
            try:
                guess = (int(guess_row)-1, int(guess_col)-1)
                for num in guess:
                    if num < 0 or num > 9:
                        raise range_error
                if guess in self.guesses_made:
                    raise already_made_error
                self.guesses_made.add(guess)
                valid_guess = True
            except ValueError as ve:
                if ve is range_error:
                    print(f"\n{str(ve)}")
                elif ve is already_made_error:
                    print(f"\n{str(ve)}")
                else: print("\nThat is an invalid input, please try again.")
        return guess
# the computer player sets the name, and adds a copy of the available moves which will be used to make guesses against the player
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Comp"
        self.guesses_left = self.available_points
    # the functions originally created in the game class are moved to here, the create_ship function tries to create a ship randomly until a valid placement is chosen
    # when the arrange_ship function returns a ship of the desired length, the points the ship covers are added to the relevant lists
    def place_ships(self):
        ship_lengths = [5, 4, 4, 3, 2]
        for e in ship_lengths:
            ind_ship = []
            ship = self.create_ship(e)
            for y in ship:
                self.ship_points.append(y)
                ind_ship.append(y)
                self.available_points.remove(y)
            self.ships.append(ind_ship)
    # given the start point and direction, return the points of the ship up to the desired length if valid, else less will be returned
    def arrange_ship(self, first, second, direction, length):
        points = set()
        if direction == "h":
            for i in range(1, length):
                x = first, second + i
                if x not in self.available_points:
                    for j in range(1, length):
                        x = first, second - j
                        if x not in self.available_points:
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
                if x not in self.available_points:
                    for j in range(1, length):
                        x = first - j, second
                        if x not in self.available_points:
                            return points
                        points.add(x)
                        if len(points) == (length - 1):
                            return points
                points.add(x)
                if len(points) == (length - 1):
                    return points
    # try to create a random ship, when arrange_ship returns a ship with a valid length, it is stored in the ships and ship_points attributes
    def create_ship(self, length):
        while True:
            startposition = choice(self.available_points)
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
    # a random point in guesses_left is chosen and returned as the computer guess, it is also removed from the list, for now the computer does not focus on a hit point
    def make_guess(self):
        guess = choice(self.guesses_left)
        self.guesses_left.remove(guess)
        return guess
