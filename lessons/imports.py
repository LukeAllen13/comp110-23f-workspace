"""Practice importing from other modules"""

from lessons import my_function

if __name__ == "__main__":
    print("Howdy!")

print(my_function.addition(1,2))

print(my_function.my_variable)