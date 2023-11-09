"""Creating dictionary functions."""

__author__ = "730704135"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    output_dict: dict[str, str] = {}
    if len(input_dict) == 0:
        return input_dict
    for key in input_dict:
        output_dict[input_dict[key]] = key
    if len(input_dict) != len(output_dict):
        raise KeyError("You can't have more than one of the same key!")
    return output_dict


def favorite_color(people_colors: dict[str, str]) -> str:
    """Find the most popuular color/s of the inputed people."""
    color_dict: dict[str, int] = {}
    if len(people_colors) == 0:
        return "Input is empty! Please enter a dictionary."
    for key in people_colors:
        if people_colors[key] in color_dict:
            color_dict[people_colors[key]] += 1
        else:
            color_dict[people_colors[key]] = 1
    num: int = 0
    for key_2 in color_dict:
        if color_dict[key_2] > num:
            num = color_dict[key_2]
    for elem in color_dict:
        if color_dict[elem] == num:
            return elem


def count(input_list: list[str]) -> dict[str, int]:
    """Count terms in inputed list."""
    ct_dict: dict[str, int] = {}
    if len(input_list) == 0:
        return ct_dict
    if len(input_list) == 0:
        return input_list
    for value in input_list:
        if value in ct_dict:
            ct_dict[value] += 1
        else:
            ct_dict[value] = 1
    return ct_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Produce a dictionary with keys equal to the first letter of the words in the value list."""
    output_dict: dict[str, list[str]] = {}
    for key in words:
        if key[0].lower() not in output_dict:
            output_dict[key[0].lower()] = [key]
        else:
            output_dict[key[0].lower()].append(key)
    return output_dict


def update_attendance(attendance_log: dict[str, list[str]], student: str, day: str) -> dict[str, list[str]]:
    """Update attendance."""
    if student not in attendance_log:
        attendance_log[student] = [day]
    elif day not in attendance_log[student]:
        attendance_log[student].append(day)
    return attendance_log


def main():
    e: dict[str, str] = invert({"Hello" : "Bye", "Bye" : "Hello"})
    print(e)
    p: dict[str, str] = favorite_color({"Luke": "Blue", "Manix": "Orange", "David": "Blue"})
    print(p)
    t: dict[str, str] = favorite_color({"Luke": "Orange", "David": "White", "Tyler": "Pink", "Jake": "Black", "Nathan": "Pink"})
    print(t)
    r: list[str] = count(["Hello", "Hello", "Hello", "See", "See", "See"])
    print(r)
    y: list[str] = count(["One_Very_Very_Very_Very_Very_Long_Term"])
    print(y)
    u: list[str] = alphabetizer(["Apple", "able", "Bell", "Car", "Door"])
    print(u)
    i: list[str] = alphabetizer(["AAA", "AAAA", "AAAAA"])
    print(i)
    o: list[str] = alphabetizer([])
    print(o)
    p: list[str] = count([])
    print(p)
    a: dict[str, str] = favorite_color({})
    print(a)
    s: dict[str, list[str]] = update_attendance({"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}, "Tuesday", "Vrinda")
    print(s)
    d: dict[str, list[str]] = update_attendance({"Tuesday": ["Luke", "David"], "Monday": ["Alyssa"]}, "Monday", "Manix")
    print(d)
    f: dict[str, list[str]] = {}
    print(update_attendance(f, "Luke", "Monday"))
    print(update_attendance({"Tuesday": ["Luke", "David"]}, "Manix", "Tuesday"))

if __name__ == "__main__":
    main()