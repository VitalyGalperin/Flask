import datetime
import random
import re
from flask import Flask

app = Flask(__name__)


@app.route('/hello_word')
def hello_function():
    return "Привет, мир!"


@app.route('/cars')
def cars_function():
    return "Chevrolet, Renault, Ford, Lada"


@app.route('/cats')
def cats_function():
    cats = ['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мэйн-Кун', 'Манчкин']
    return random.choice(cats)


@app.route('/get_time/now')
def now_function():
    current_time = datetime.datetime.now()
    return f"Точное время {current_time}"


@app.route('/get_time/future')
def future_function():
    future_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет {future_time}"


@app.route('/get_random_word')
def word_function():

    while True:
        with open('war_and_peace.txt', 'r', encoding='cp1251') as file:
            random_line = random.choice(file.readlines())
            words = random_line.split(' ')
            if len(words) > 0:
                word = random.choice(words)
                format_word = re.sub(r"[,.!?;:-]", "", word)
                if format_word and len(format_word) > 1:
                    break
    return format_word


@app.route('/counter')
def count_func():
    if not hasattr(count_func, 'count'):
        count_func.count = 0
    count_func.count += 1
    return 'Страница открывалась/обновлялась ' + str(count_func.count) + ' раз(а)'
