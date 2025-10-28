from idlelib.debugger_r import restart_subprocess_debugger

from to_do import TODO


def task5(scores: list[int]) -> list[int]:

    if not  scores:
        return [-1]

    result = []

    for index,score in enumerate(scores):
        if index != scores[-1]:
            result.append(score + scores[index + 1])
        elif index == scores[-1]:
            result.append(score * score)


    return result

if __name__ == "__main__":

    # scores = [3, 5, 7, 2] ---> [8, 12, 9, 4]
    print(task5(scores = [3, 5, 7, 2]))
