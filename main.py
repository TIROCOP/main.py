from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return '''<title> Привет, Марс! </title>
    <body> Миссия Колонизация Марса <body/>'''


@app.route('/index')
def index():
    return '''<title> Привет, Марс! </title>И на Марсе будут яблони цвести!'''


@app.route('/promotion')
def promotion():
    return '''<title> Привет, Марс! </title>
    Человечество вырастает из детства.</br>Человечеству мала одна планета.</br> 
           Мы сделаем обитаемыми безжизненные пока планеты.</br>И начнем с Марса!Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title> Привет, Марс! </title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{}" alt=""></br>
    Человечество вырастает из детства.</br>
    Человечеству мала одна планета.</br> 
    Мы сделаем обитаемыми безжизненные пока планеты.</br>
    И начнем с Марса!Присоединяйся!
</body>
</html>'''.format(url_for('static', filename='img/image_mars.png'))


@app.route('/promotion_image')
def promotion_image():
    with open('file_mars.html', 'r', encoding='utf-8') as CODE:
        return CODE.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
