"""for loops."""

xs: list[int] = [1, 2, 3]
idx: int = 0
while idx < len(xs):
    print(xs[idx])
    idx += 1

for elem in xs:
    print(elem)

for number in xs:
    print(number)

pets: str = ["Louie", "Bo", "Bear"]

for pet_name in pets:
    print(f"Good boy, {pet_name}!")

names: list[str] = ["ALyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    elem: str = names[idx]
    print(f"{idx}:{elem}")