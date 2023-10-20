"""EX03 - Wordle - 6 tries to guess the word!"""
__author__ = "730704135"
# PID


def contains_char(rand_string: str, char_guess: str) -> bool:
    """When given two strings, one with any length, and one with a single character, it will return true if the single character is found in any index of the word with any length."""
    assert len(char_guess) == 1
    idx_secret = 0
    # Primary goal is to create a bool to be used in the emojified function. It directly compares the indexes of each word. 
    while int(idx_secret) < int(len(rand_string)):
        if str(rand_string[idx_secret]) == str(char_guess):
            return True
        idx_secret += 1 
    return False


def emojified(guess_parameter: str, secret: str) -> str:
    """Compares the index of both the secret word and the guess word and replaces the letters with their corresponding box."""
    assert len(guess_parameter) == len(secret)
    idx_secret = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # main goal is to add an emoji onto the string "boxes" from left to right so the user knows if their guess has simlar letters or not
    boxes = ""
    while int(idx_secret) < int(len(secret)):
        if secret[idx_secret] == guess_parameter[idx_secret]:
            boxes += GREEN_BOX
        else:
            if contains_char(secret, str(guess_parameter[idx_secret])) is True:
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX

        idx_secret += 1
    return boxes


def input_guess(guess_length: int) -> str:
    """Checks to see if the length of the guessed word is equal to the length of the secret word. This is necessary because you want to continue to ask for a word if it is being given in the incorrect format (length)."""
    secret_guess = input(f"Enter a {guess_length} character word: ")
    # tells the user to input another guess beacause their last one was incorrect. Of course, they only get 6 attempts.
    while len(secret_guess) != guess_length:
        secret_guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return secret_guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret_word = "chess" 
    # allows the user 6 attempts to guess a word of any length. They must have the correct amount of letters in their guess for it to count and tell them how close they were. 
    # at the end, if you run out of guesses, you are either told you won in x/6 turns or you are told to try again tomorrow.
    # this is because the actual wordle game has one word a day. So, if you were to fail the word completely, you would have to return the next day to try a new one. 
    turns = 1
    loop = False
    while turns < 7 and loop is False:
        print(f"=== Turn {turns}/6 ===")
        secret_guess = input_guess(len(secret_word))
        print(emojified(secret_guess, secret_word))
        if str(secret_guess) == str(secret_word):
            print(f"You won in {turns}/6 turns!")
            loop = True
        turns += 1

    print("X/6 - Sorry, try again tomorrow!")
# makes it possible to run the python code as a module
# makes it possible for other modules to import your functions and reuse them


if __name__ == "__main__":
    main()