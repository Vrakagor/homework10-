import keyword
def is_valid_variable(name):
    if not name or name in keyword.kwlist or name.count("__") > 1 or name[0].isdigit():
        return False

    for char in name:
        if not (char.islower() or char.isdigit() or char == "_"):
            return False
    else:
        return True
user_input = input("Введіть ім'я змінної: ")
