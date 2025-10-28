from to_do import TODO


def task3(temperatures: list[int]) -> str:

    month = ["January","February","March","April","May","June","July","August","September",
             "October","November","December"]


    lowest_value = temperatures[0]
    result = 0

    for index,temperature in enumerate(temperatures):
        if temperature < lowest_value:
            lowest_value = temperature
            result = index

    return month[result]

if __name__ == "__main__":

    # temperatures = [-2, 0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1]
    print(task3(temperatures = [-2, 0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1]))

    # temperatures = [-2, 0, 5, 9, 15, 20, 22, 21, 16, 10, 4, -1]
    print(task3(temperatures=[5, 3, 10, 9, 15, 20, 22, 21, 16, 10, 4, 25]))
