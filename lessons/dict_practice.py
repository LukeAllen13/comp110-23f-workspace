"""Practice with dictionaries."""

# Constructing a dictionary...
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary.")
print(ice_cream)


# Learning to add elements (a key value pair) to a dictionary...
ice_cream["mint"] = 3
print("After adding mint.")
print(ice_cream)


# Maybe you want to remove a key value pair from your dictionary...
ice_cream.pop("mint")
print("After removing mint.")
print(ice_cream)


# Accessing a value of a key...
print(f"I have {ice_cream['chocolate']} orders of chocolate ice cream.")


# Modifying a value...
ice_cream["vanilla"] = 10
# or ice_cream["vanilla"] += 2
# both modify in the same way. 
print("After modifying vanilla ice_cream.")
print(ice_cream)


# Getting the length
# When using len(dict), it returns the amount of key value pairs that you have in the dictionary.
print("Flavors available after removing mint.")
print(f"The number of flavors(key value pairs) available: {len(ice_cream)}")


# To check to see if a key is in your dictionary...
"chocolate" in ice_cream
"rainbow sherbert" in ice_cream
print("Is chocolate in ice cream?")
print("chocolate" in ice_cream)
print("Is mint in ice cream?")
print("mint" in ice_cream)
# returns a bool letting you know if the key was found in the dictionary...


# for loops with dict
for key in ice_cream:
    print(key)

for key in ice_cream:
    print(ice_cream[key])

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")

