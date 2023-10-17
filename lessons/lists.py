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

"""Half life problem."""
i = 0
drug_mg: int = 0
while i < 50:
    drug_mg: int = (drug_mg * .5) + 60
    i += 1
print("The answer to the Half Life problem: ")
print(drug_mg)

m = 0
balance: int = 0
while m < 43:
    balance: int = (balance * 1.0025) + 90
    m += 1
print("The balance is: ")
print(balance)

def interest(balance: int, num_months: int) -> int:
    n = 0
    new_balance: int = 0
    interest_rate: int = input(f"Input your interest rate for {num_months} here: ")
    while n < num_months:
        new_balance: int = new_balance + (balance * interest_rate)
        n += 1
    return new_balance