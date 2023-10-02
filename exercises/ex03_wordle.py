"""EX03 - Wordle - 6 tries to guess the word!"""
__author__ = "730704135"

def contains_char(rand_string: str, char_guess: str) -> bool:
    """When given two strings, one with any length, and one with a single character, it will return true if the single character is found in any index of the word with any length."""
    assert len(char_guess) == 1
    idx_secret = 0
    while int(idx_secret) < int(len(rand_string)):
        if str(rand_string[idx_secret]) == str(char_guess):
            return True
        idx_secret += 1 
    return False

def emojified(guess: str, secret: str) -> str:
    idx_secret = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    boxes = " "
    assert len(guess) == len(secret)
    while int(idx_secret) < int(len(secret)):
        if secret[idx_secret] == guess[idx_secret]:
            boxes += GREEN_BOX
        else:
            if contains_char(secret, str(guess[idx_secret])) is True:
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX
        idx_secret += 1
    return boxes

def input_guess(guess_length: int) -> str:
    secret_guess = input(f"Enter a {int(guess_length)} letter word: ")
    while len(secret_guess) != guess_length:
        secret_guess = input(f"That wasn't {int(guess_length)} chars! Try again: ")
    return secret_guess

def main() -> None:
    """The entrypoint of the program and teh main game loop."""
    secret_word = "codes" 
    turns = 1
    while turns < 7:
        print(f"=== Turn {turns}/6 ===")
        secret_guess = input_guess(len(secret_word))
        print(emojified(secret_guess, secret_word))
        if str(secret_guess) == str(secret_word):
            print(f"You won in {turns}/6 turns!")
            exit()
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
        


    
                        