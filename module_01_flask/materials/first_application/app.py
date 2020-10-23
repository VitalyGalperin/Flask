import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/test')
def test_function():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


@app.route('/hello/world')
def hello_func():
    return "Hello, world!"


@app.route('/counter')
def count_func():
    if not hasattr(count_func, 'count'):
        count_func.count = 0
    count_func.count += 1
    return 'Страница открывалась/обновлялась ' + str(count_func.count) + ' раз(а)'
