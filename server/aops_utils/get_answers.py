import requests
from bs4 import BeautifulSoup
import functools


@functools.lru_cache(maxsize=None)
def get_answers(year: int, contest: str) -> list[list[int]]:
    URL = "https://artofproblemsolving.com/wiki/api.php"
    PARAMS = {
        "action": "parse",
        "page": f"{year}_AIME_{contest}_Answer_Key",
        "format": "json"
    }

    R = requests.get(url=URL, params=PARAMS)
    DATA = R.json()

    html = BeautifulSoup(DATA["parse"]["text"]["*"], 'html.parser')
    ol = html.find("ol")
    ret = []
    if year == 2024 and contest == "I":
        ls = [[i] for i in [204, 25, 809, 116, 104, 294, 540, 197, 480, 113, 371, 385, 110, 104, 721]]
        ls[11] = [384, 385]
        return ls
    if len(ol.findAll("li")) != 15:
        print(f"WARNING: NOT VALID NUMBER OF PROBLEMS FOR {year}")
    for i, li in enumerate(ol.findAll("li")):
        if year == 2022 and contest == "II" and i == 7:
            ret.append([80, 81])
            continue
        try:
            ans = int(li.text)
            if ans < 0 or ans > 999:
                raise ValueError
            ret.append([ans])
        except ValueError:
            print(f"IS NOT VALID FOR {year} PROBLEM {i + 1}: ", li.text)
            ret.append([0])
    return ret


def verify_answer(year: int, contest: str, problem_num: int, answer: int) -> bool:
    if year < 2000 or year > 2024:
        return False
    if contest != "I" and contest != "II":
        return False
    if problem_num < 1 or problem_num > 15:
        return False
    print(get_answers(year, contest)[problem_num - 1])
    return answer in get_answers(year, contest)[problem_num - 1]


def test():
    for year in range(2000, 2025):
        for contest in ["I", "II"]:
            try:
                l = get_answers(year, contest)
                print(f"SUCCEEDED {year} {contest}: {l}")
            except Exception as e:
                print(f"FAILED {year} {contest}: {e}")
