"""Choose a class to play on ROTMG!"""

from random import randint

Classes: list[str] = ["Knight", "Warrior", "Paladin", "Samurai", "Archer", "Huntress", "Bard", "Kensei", "Summoner", "Samurai", "Ninja", "Sorcerer", "Trickster", "Mystic", "Necromancer", "Assassin", "Knight", "Priest", "Wizard", "Archer", "Rogue"]

print(f"{Classes[randint(0, 20)]}")