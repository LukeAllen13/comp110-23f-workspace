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

weeks = 0
while weeks <= 7:
    my_stats: int = int(input("Enter your pts per week and see how many points you will get: "))

    from random import randint

    opponent_score: int = int(randint(5,70))

    if int(my_stats) > int(opponent_score):
        print(f"You win! You get three points this week! Your opponent had {int(opponent_score)} points.")
    elif my_stats == opponent_score:
        print(f"You tied! You each get 1 point. Your opponent had {int(opponent_score)} points.")
    else:
        print(f"Unfortunate! You lost this week. Your opponent had {int(opponent_score)} points.")
    weeks += 1
