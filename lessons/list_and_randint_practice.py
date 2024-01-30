"""IDST 101 6.4 reflection, last question answer."""

resources_list: list[str] = ["All in the Family", "Actively Moving Forward", "988 Lifeline"]
l = 0

while l <= len(resources_list) - 1:
    if l == 0:
        print(f"{resources_list[0]} helps students who come from difficult family dynamics. It exists to help them build connections, share about their experiences, and give and receive support. \n")
    if l == 1:
        print(f"{resources_list[1]} helps students who have lost a loved one. Not only do they provide a group of students that can all talk to each other, but they have events and resources for those who are involved to use. \n")
    if l == 2:
        print(f"{resources_list[2]} offers an option to call or text 988 or chat online if you’re thinking about suicide, are worried about a friend, or need emotional support. Also “offers ayuda en espanol.” \n")
    l += 1

print("Listed above are my resource descriptions! \n")

print("Now see how you do by week in fpl! \n")
weeks = 1
wins = 0
losses = 0
ties = 0

while weeks <= 21:
    my_stats: int = int(input("Enter your average pts per week and see how many points you will get when facing the bot!: "))
    
    from random import randint

    opponent_score: int = int(randint(5,70))
    print(f"Week {int(weeks)}/21")

    if int(my_stats) > int(opponent_score):
        print(f"You win! You get three points this week! Your opponent had {int(opponent_score)} points. \n")
        wins += 1
    elif my_stats == opponent_score:
        print(f"You tied! You each get 1 point. Your opponent had {int(opponent_score)} points. \n")
        ties += 1
    else:
        print(f"Unfortunate! You lost this week. Your opponent had {int(opponent_score)} points. \n")
        losses += 1
    weeks += 1
    print(f"You have {int(wins)} wins, {int(losses)} losses, and {int(ties)} ties. \n")
    if int(wins) < int(losses):
        print("Computer: hahahahaahahahaahahahahahaahahahhaha \n")


suits = ["spade", "heart", "club", "diamond"]
player1_starting_bank: int = 500
player2_starting_bank: int = 500
card1_num = int(randint(1,13))
card2_num = int(randint(1,13))
card3_num = int(randint(1,13))
card4_num = int(randint(1,13))
card5_num = int(randint(1,13))
card1_suit = str(suits[randint(0,3)])
card2_suit = str(suits[randint(0,3)])
card3_suit = str(suits[randint(0,3)])
card4_suit = str(suits[randint(0,3)])
card5_suit = str(suits[randint(0,3)])
player1_card_num = randint(1,13)
player2_card_num = randint(1,13)
player1_card_suit = str(suits[randint(0,3)])
player2_card_suit = str(suits[randint(0,3)])
player1_full_card = [player1_card_num, player1_card_suit]
player2_full_card = [player1_card_num, player1_card_suit]
turns = 0

# if player1_card_num > card1_num:
