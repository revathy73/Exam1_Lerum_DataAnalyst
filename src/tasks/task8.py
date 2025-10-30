from to_do import TODO


def task8(text: str) -> str:

    if not text:
        result = ""

    result = ""
    text_new  = ""
    for letter in reversed(text):
        text_new += letter

    for index,letter_new in enumerate(text_new):
        if index % 2 == 0:
            result += letter_new.upper()
        else:
            result += letter_new

    return result


if __name__ == "__main__":

    # text = "abcd"
    print(task8(text = "abcd"))

    # text =
