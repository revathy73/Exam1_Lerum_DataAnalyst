from to_do import TODO


def task2(votes: str) -> str:

    #high_votes = votes[0]
    result = 0
    value = 0
    for vote in votes:
        value = votes.count(vote)
        if value > len(votes):
            result = value


    if value == "A":
        result = "Alice"
    elif value == "B":
        result = "Bob"
    elif value == "C":
        result = "Carol"
    elif value == "D":
        result = "David"

    return result

if __name__ == "__main__":

    # votes = "CBBDAAB"
    print(task2(votes = "CBBDAAB"))

    # votes = "CCDCAAB"
    print(task2(votes="CBBDAAB"))
