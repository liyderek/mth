import random
import requests
from bs4 import BeautifulSoup
import functools


@functools.lru_cache(maxsize=None)
def get_problems(year: int, contest: str) -> list[str]:
    if year < 2000 or year > 2024:
        return []
    if contest != "I" and contest != "II":
        return []

    URL = f"https://artofproblemsolving.com/wiki/index.php/{year}_AIME_{contest}_Problems"
    PARAMS = {}
    R = requests.get(url=URL, params=PARAMS)
    if R.status_code != 200:
        return []
    html = BeautifulSoup(R.content, 'html.parser')

    ret = []
    for h2 in html.findAll('h2'):
        if not h2.text.startswith("Problem"):
            continue
        prob_string = ""
        p = h2
        while p.find_next_sibling().name == "p":
            p = p.find_next_sibling()
            for a in p.findChildren("a", recursive=False):
                if str(a.text).strip() == "Solution":
                    break
            else:
                prob_string += str(p) + "\n"
                continue
            break

        ret.append(prob_string)

    return ret


def get_problem(year: int, contest: str, problem_num: int) -> str:
    if year < 2000 or year > 2024:
        return ""
    if contest != "I" and contest != "II":
        return ""
    return get_problems(year, contest)[problem_num - 1]


def random_problem(num_min: int, num_max: int) -> tuple[int, str, int]:
    if num_min > num_max or num_min < 1 or num_max > 15:
        return 0, "invalid", 0
    year = random.randint(2000, 2024)
    contest = random.choice(['I', 'II'])
    problem_num = random.randint(num_min, num_max)
    return year, contest, problem_num
