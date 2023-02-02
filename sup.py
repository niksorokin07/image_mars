from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def printt():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """<h1>Человечество вырастает из детства.</h1>
            <h1>Человечеству мала одна планета.</h1>
            <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
            <h1>И начнем с Марса!</h1>
            <h1>Присоединяйся!</h1>"""


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='mars.png')} alt="no img">
                    <div class="alert alert-primary" role="alert">
                      Вот она какая, красная планета!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
