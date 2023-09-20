"""EX02 - One Shot Wordle - Give it your best shot!"""
__author__ = "730704135"
secret = "python"
# asks for an inputed guess that matches the length of the secret word
secret_guess: str = input(f"What is your {len(secret)} letter guess? ")

# list of variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
boxes = " "
idx_secret = 0
compare_char = False
secret_char = 0

# for every guess that is not the correct length, you get another guess
while len(secret_guess) != len(secret):
    secret_guess = input(f"That was not {len(secret)} letters! Try again: ")
    
# first section checks to see if the current index of the guess (as the index increases) has a string value matching that of the secret word
# if so it adds a green box onto the boxes string which tells you the which letter is in the correct position
while int(idx_secret) < int(len(secret)):
    if secret[idx_secret] == secret_guess[idx_secret]:
        boxes += GREEN_BOX
        idx_secret += 1

# the else takes all str values that do not equal the secret and throws them into a while loop to run through each letter of secret
# if a letter of secret matches the current index of the guess, a yellow box will be added to the string. If not, a white box will be added to the string
    else:
        while compare_char is False and secret_char < int(len(secret)):
            if secret[secret_char] == secret_guess[idx_secret]:
                compare_char is True
            else:
                secret_char += 1  

        if compare_char == True:
            boxes += YELLOW_BOX
        else:
                boxes += WHITE_BOX
                
        idx_secret += 1

# prints the boxes
print(boxes)

# tells the user if they correctly guessed the word or not (already seen through the boxes but just for insurance)
if secret_guess == secret:
    print("Woo! You got it!")        
else:
    print("Not quite. Play again soon!")