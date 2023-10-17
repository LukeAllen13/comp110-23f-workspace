"""for loops."""

xs: list[int] = [1, 2, 3]
idx: int = 0
while idx < len(xs):
    print(xs[idx])
    idx += 1

for elem in xs:
    print(elem)