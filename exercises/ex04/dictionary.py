"""Exercise to gain familiarity with dictionaries and common fuctions."""

__author__ = "730736689"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Function to reverse dictionary keys and values."""
    output: dict[str, str] = {}
    for key in input:
        new_key: str = str(input[key])
        new_value: str = str(key)
        output[str(new_key)] = str(new_value)
        # new list, no confusion with keys and values
    if len(input) != len(output):
        # if there are two same values, the lists will be diff lengths - use this
        raise KeyError("output may not contain two identical keys")
    else:
        return output


def favorite_color(input: dict[str, str]) -> str:
    """Returns most popular color in a group."""
    colors: dict[str, int] = {}
    for people in input:
        if input[people] in colors:
            colors[str(input[people])] += 1
            # works similar to count function. create another dict to then use
        else:
            colors[str(input[people])] = 1
    fav_count: int = 0
    # define these as empty/0 outside of loop so they don't reset each time
    favorite: str = ""
    for color in colors:
        if colors[color] > fav_count:
            # if value is higher, they'll change, if equal, they won't
            fav_count = colors[color]
            favorite = color
    return str(favorite)


def count(input: list[str]) -> dict[str, int]:
    """Returns the count of times each value appears in a list."""
    counts: dict[str, int] = {}
    for value in input:
        if value in counts:  # will skip this until else completed
            counts[value] += 1
        else:
            counts[value] = 1  # will complete first
    return counts


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Categorizes a list of words into the letter they start with."""
    dictionary: dict[str, list[str]] = {}
    # create empty dictionary first to return later
    for item in input:
        if item[0].lower() in dictionary:
            letter_list: list[str] = dictionary[item[0].lower()]
            # use .lower() function to ensure P and p would be same
            letter_list.append(item)
            dictionary[item[0].lower()] = letter_list
        else:
            dictionary[item[0].lower()] = [item]
    return dictionary


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates a list to include names of students and days they were present."""
    if day in input:
        if student not in input[day]:  # ensures no repeated names
            student_list: list[str] = input[day]
            student_list.append(student)
            input[day] = student_list
        # use more simple version of code used for alphabetizer
    else:
        input[str(day)] = [student]
