import random
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from server.aops_utils import *
from server.aops_utils.get_answers import verify_answer
from server.aops_utils.get_problems import get_problems, get_problem, random_problem
from server.aops_utils.get_solutions import get_solutions

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/problems/AIME/test', methods=['GET'])
def problems():
    year = int(request.args.get('year', None))
    contest = str(request.args.get('contest', None))
    return jsonify(problems=get_problems(year, contest))

@app.route('/api/problems/AIME/single', methods=['GET'])
def single():
    year = int(request.args.get('year', None))
    contest = str(request.args.get('contest', None))
    num = int(request.args.get('num', None))
    return get_problem(year, contest, num)

@app.route('/api/problems/AIME/solution', methods=['GET'])
def solution():
    year = int(request.args.get('year', None))
    contest = str(request.args.get('contest', None))
    num = int(request.args.get('num', None))
    return jsonify(solutions=get_solutions(year, contest, num))

@app.route('/api/problems/AIME/check', methods=['GET'])
def check_problem():
    year = int(request.args.get('year', None))
    contest = str(request.args.get('contest', None))
    num = int(request.args.get('num', None))
    answer = int(request.args.get('answer', None))
    return jsonify(verdict=verify_answer(year, contest, num, answer))

@app.route('/api/problems/AIME/random', methods=['GET'])
def random():
    num_min = int(request.args.get('min', None))
    num_max = int(request.args.get('max', None))
    ret = random_problem(num_min, num_max)
    if ret[1] == "invalid":
        abort(404)
    return jsonify(year=ret[0], contest=ret[1], num=ret[2])

if __name__ == '__main__':
    app.run()