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

print("Here are are my resource descriptions!")