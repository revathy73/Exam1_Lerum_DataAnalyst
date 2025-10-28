from to_do import TODO


def task7(deliveries: list[int]) -> str:


    day = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    highest_value = deliveries[0]
    value = 0
    result = 0

    for index,delivery in enumerate(deliveries):
        if delivery > highest_value:
            if deliveries[index] == 4:
                break
            else:
                highest_value = delivery
                result = index

    return day[result]

if __name__ == "__main__":

    # deliveries = [5, 16, 9, 14, 13, 20, 25]
    print(task7(deliveries = [5, 16, 9, 14, 13, 20, 25]))

    # deliveries = [35, 16, 50, 14, 100, 20, 25]
    print(task7(deliveries=[35, 16, 50, 14, 100, 20, 25]))


