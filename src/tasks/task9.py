import string
from curses.ascii import isupper, islower, isdigit

from unicodedata import digit

from to_do import TODO


def task9(username: str) -> bool:
    """
    lowercase_re = re.findall("[a-z]",username)
    uppercase_re = re.findall("[A-Z]",username)

    return {

    }
    """

    special = "_"
    number = [0-9]
    alphabet = string.ascii_lowercase
    alphabet1 = string.ascii_uppercase
    #number = digits

    if (len(username) < 5 or len(username) > 12):
        return False

    if username[0] != alphabet :
        return False

    if username[-1] == special:
        return False

    if username[0] == username.isdigit():
        return True

    has_upper = False
    has_lower = False
    has_digit =  False
    has_underscore = False

    for letter in username:
        if letter == isupper():
            has_upper = True
        elif letter == islower():
            has_lower = True
        elif letter == isdigit():
            has_digit = True
        elif letter == has_underscore:
            result = True
        else:
            result = True

    return result


if __name__ == "__main__":

    # username = "Alex_9"
    print(task9(username = "Alex_9"))

    # username = "9alexA"
    print(task9(username = "9alexA"))


