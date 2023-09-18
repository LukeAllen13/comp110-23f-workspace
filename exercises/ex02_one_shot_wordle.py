"""EX02 - One Shot Wordle - Give it your best shot!"""
__author__ = "730704135"
secret = "python"
secret_guess: str = input(f"What is your {len(secret)} letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

boxes = " "
idx_secret_guess = str(secret_guess[0])
idx_secret = str(secret[0])



while len(secret_guess) != len(secret):
    secret_guess: str = input(f"That was not {len(secret)} letters! Try again: ")

y = 0
p = 0

while len(secret_guess) == len(secret) and p == 0:
    if secret_guess == secret:
        print("Woo! You got it!")
        p += 1
    else:
        print("Not quite. Play again soon!")
        p += 1

while int(idx_secret_guess) < int(len(secret)) and y == 0:
    if idx_secret_guess == idx_secret:
        boxes += str(GREEN_BOX)
        y += 1
    else:
        boxes += str(WHITE_BOX)
        y += 1
print(str(boxes))
