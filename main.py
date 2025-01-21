import keyword

def is_valid_variable(name):
    if not name or name in keyword.kwlist or name[0].isdigit():
        return False

    if name.strip("_") == "":
        return False

    if "__" in name and not name.lstrip("_").isalnum():
        return False

    for char in name:
        if not (char.islower() or char.isdigit() or char == "_"):
            return False

    return True


user_input = input("Введіть ім'я змінної: ")
print(is_valid_variable(user_input))