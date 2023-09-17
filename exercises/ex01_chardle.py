"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730704135"

five_char_word: str = input("Enter a 5-character word: ")

if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_char: str = input("Enter a single character: ")

if len(single_char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_char + " in " + five_char_word)
    
i = 0
num_chars = 0
if five_char_word[i] == single_char:
    print(single_char + " found at index " + str(i))
    i += 1
    num_chars += 1
else:
    i += 1

if five_char_word[i] == single_char:
    print(single_char + " found at index " + str(i))
    i += 1
    num_chars += 1

else:
    i += 1

if five_char_word[i] == single_char:
    print(single_char + " found at index " + str(i))
    i += 1
    num_chars += 1

else:
    i += 1

if five_char_word[i] == single_char:
    print(single_char + " found at index " + str(i))
    i+=1
    num_chars += 1

else:
    i += 1

if five_char_word[i] == single_char:
    print(single_char + " found at index " + str(i))
    i += 1
    num_chars += 1

if num_chars == 1:
    print(str(num_chars) + " instance of " + single_char + " found in " + five_char_word)
elif num_chars > 0:
    print(str(num_chars) + " instances of " + single_char + " found in " + five_char_word)
elif num_chars == 0:
    print("No instances of " + single_char + " found in " + five_char_word)
    
