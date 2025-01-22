import keyword


def is_valid_variable(name):

    if not name or name in keyword.kwlist:
        return False

    if name.strip("_") == "":
        return False

    if name[0].isdigit():
        return False

    if not all(c.islower() or c.isdigit() or c == "_" for c in name):
        return False

    return True

user_input = input("Введіть ім'я змінної: ")