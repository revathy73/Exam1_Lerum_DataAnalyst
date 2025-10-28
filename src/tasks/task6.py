from to_do import TODO


def task6(orders: list[str]) -> list[str]:

    result = []
    for order in orders:
        order_components = order.split("|")
        country = order_components[1]
        if country.lower() == "se":
            result.append(order_components[0])
    return result

if __name__ == "__main__":

    print(task6(orders =
        ["anna|se|ELEC-4932",
        "bo|no|HOME-118",
        "carl|SE|SPORT-77",
        "dina|dk|ELEC-200",
        "erik|se|HOME-555",
        "fred|se|ELEC-4932"]
        ))
