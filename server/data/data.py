import json
import os
import random


def get_json(obj):
    return json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))


class Data:
    def __init__(self, problems: list[tuple[int, str, int]]):
        self.problems = problems


userdata: Data = Data([])


def write_file():
    print("Writing data")
    with open("data.json", "w") as f:
        f.write(get_json(userdata))


def read_file():
    print("Reading data")
    global userdata
    if not os.path.exists("data.json"):
        write_file()
    with open("data.json", "r") as f:
        userdata = json.loads(f.read(), object_hook=lambda d: Data(**d))


def get_all_problems():
    return userdata.problems


def successfully_solve(problem: tuple[int, str, int]):
    if problem not in userdata.problems:
        userdata.problems.append(problem)


def get_random_problem(num_min: int, num_max: int) -> tuple[int, str, int]:
    if num_min > num_max or num_min < 1 or num_max > 15:
        return 0, "invalid", 0
    unsolved_problems = [(year, contest, num) for year in range(2000, 2024) for contest in ["I", "II"] for num in
                         range(num_min, num_max) if (year, contest, num) not in userdata.problems]
    return random.choice(unsolved_problems) if unsolved_problems else (0, "invalid", 0)
