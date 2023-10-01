word: str = input("Input a word: ")
index: int = int(input("Input an integer: "))



def mimic(word: str, index: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if index >= len(word):
    #you could do len(word) - 1 , as well becaseu it is the same thing
        return ("Too high of an index")
    return word[index]
    #dont need an else because it would exit if statement anyway if it didnt run. Then it would return the letter at the index. 

#(mimic(word, index))
