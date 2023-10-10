"""Practice with lists."""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1]: str = "cereal"
grocery_list.pop(2)
print(grocery_list)

x: list[str] = ["Comp", "110"]
x[1] = "210"
y: str = x
print(y)

a: str = "24"
b: str = a 
a += "6"
print(b)