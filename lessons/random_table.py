list_players: list[str] = ["Matthew G", "Luke", "Zach", "Matthew R", "Dylan", "Scott", "Jesse", "Gavin", "Kevin", "Morgan", "Dairyanne", "Andrew"]
from random import randint
i: str = 0
while i < 13:
    random: int = randint(0, len(list_players))
    print(f"In spot number {i}, we have {list_players[random]}!")
    g: int = 0
    while g < len(list_players):
        if list_players[g] == list_players[random]:
            list_players.pop(g)
        g += 1
    i += 1