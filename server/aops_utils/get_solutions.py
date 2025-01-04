import random
import requests
from bs4 import BeautifulSoup
import functools


@functools.lru_cache(maxsize=None)
def get_solutions(year: int, contest: str, num: int) -> list[dict[str, str]]:
    if year < 2000 or year > 2024:
        return []
    if contest != "I" and contest != "II":
        return []

    URL = f"https://artofproblemsolving.com/wiki/index.php/{year}_AIME_{contest}_Problems/Problem_{num}"
    PARAMS = {}
    R = requests.get(url=URL, params=PARAMS)
    if R.status_code != 200:
        return []
    html = BeautifulSoup(R.content, 'html.parser')
    print(html)

    ret = []
    for h2 in html.findAll('h2') + html.findAll('h3'):
        if not (h2.text.startswith("Solution") or h2.text.startswith("Video")):
            continue
        if h2.text.startswith("Solutions"):
            continue
        solution = {}
        solution_str = ""
        solution["title"] = h2.text
        solution["author"] = "AOPS"
        p = h2
        while p.find_next_sibling().name == "p" or p.find_next_sibling().name == "center":
            p = p.find_next_sibling()
            if p.text.startswith("~"):
                solution["author"] = p.text.strip(" \n")
                break
            solution_str += str(p) + "\n"
        solution["content"] = solution_str
        ret.append(solution)

    return ret
