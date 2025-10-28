from to_do import TODO


def task1(weather: str) -> str:


    """
    length_of_weather = len(weather)
    size_of_index = length_of_weather - 1
    """
    middle_index = len(weather) // 2
    middle_value = weather[middle_index]

    if middle_value == "S":
        result = "Sunny"
    elif middle_value == "C":
        result = "Cloudy"
    elif middle_value == "R":
        result = "Rainy"
    else:
        result = "Storm"


    return result


if __name__ == "__main__":

    # weather = "SCRTS"   ---> Rainy
    print(task1(weather = "SCRTS"))

    # weather = "RTSCS"   ---> Sunny
    print(task1(weather = "RTSCS"))


