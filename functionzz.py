FILEPATH = "UdoTodo.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        Todoss = file_local.readlines()
    return Todoss


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """

    # Get the two values in a list
    parts = user_input.split(",")

    # Store the two values in variables
    lower_bound = float(parts[0])
    upper_bound = float(parts[1])

    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}


import zipfile
import pathlib

# zipfile and pathlib are standard libraries


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # pathlib.Path generates a "destination path" of the form: dest_dir/compressed.zip
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def feetinch_to_meter(ft, inch):
    meter = ft * 0.3048 + inch * 0.0254
    return meter


def strength(password):
    # The variable "password" contains an "input" request for password. For example: password = input("Enter your key")
    result = []
    if len(password) >= 8:
        result.append(True)
    else:
        result.append(False)

    uppercase = False
    for item in password:
        if item.isupper():
            uppercase = True
    result.append(uppercase)

    digit = False
    for item in password:
        if item.isdigit():
            digit = True
    result.append(digit)

    if all(result) == True:
        return "Strong Password"
    else:
        return "Weak Password"

def avg(scores):
    average = sum(scores)/len(scores)
    return average
    # 'scores' is a list of numbers

def get_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    return age

def get_nr_items(usr_ip):
    items = usr_ip.split(",")
    return len(items)
    # This fn calculates the no of items separated by comma as entered by the user.

def feeling(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <= 25:
        return "Warm"
    else:
        return "Cold"


freezing_point = 0
boiling_point = 100
def water_state(temp):
    if temp <= freezing_point:
        return "Solid"
    elif freezing_point < temp < boiling_point:
        return "Liquid"
    else:
        return "Gas"


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
    make_archive(filepaths=["bonus1.py", "bonus2.py"], dest_dir="dest")
