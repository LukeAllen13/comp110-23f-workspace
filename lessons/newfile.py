"""Storymode"""
from random import randint

people: list[str] = ["David", "Luke", "Manix"]

num = randint(0,2)

david_pts = 0
luke_pts = 0
manix_pts = 0

t = 0
while t < 5:
    print(f"{people[num]}" gets a bonus point.)
    if people[num] == str("David"):
        david_pts += 1
    if people[num] == str("Luke"):
        luke_pts += 1
    if people[num] == str("Manix"):
        manix_pts += 1

print(f"David has {david_pts} pts. Luke has {luke_pts} pts. Manix has {manix_pts} pts.")

