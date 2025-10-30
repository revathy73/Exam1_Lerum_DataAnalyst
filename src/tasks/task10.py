from to_do import TODO


def task10(classroom: list[str], student: str) -> int:

    result = 0
    for index,string in enumerate(classroom):
        if string.lower() == student.lower():
                result += index

    return result


if __name__ == "__main__":

    # classroom = ["Anna", "Bob", "anna", "Eve", "Anna"] , student = "anna"
    print(task10(classroom = ["Anna", "Bob", "anna", "Eve", "Anna"] , student = "anna"))
