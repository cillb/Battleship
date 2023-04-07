"""
This program contains the player class that is used to interact with the battleship game class.
The generic class initialises a set of guesses made by the player which is used to check for
repeated guesses. The guess function takes input from the user, and checks if it is a valid guess
by making sure integer values are entered that fall inside of a valid range, and that it is not a
repeated guess.
"""
class Player:
    def __init__(self):
        self.guesses = set()

    def get_guess(self):
        pass

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def get_guess(self):
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
                if guess in self.guesses:
                    raise already_made_error
                self.guesses.add(guess)
                valid_guess = True
            except ValueError as ve:
                if ve is range_error:
                    print(f"\n{str(ve)}")
                elif ve is already_made_error:
                    print(f"\n{str(ve)}")
                else: print("\nThat is an invalid input, please try again.")
        return guess