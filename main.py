from flask import Flask, url_for, request

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


@app.route('/promotion_image')
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
                  <link rel="stylesheet" 
                    href="{url_for('static', filename='style/style.css')}">
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.png')} alt="no img">
                    <div class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style/style2.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Форма для регистрации в суперсекретной системе</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                        <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                        <input type="password" class="form-control" id="password" placeholder="Введите адрес почты" name="password">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас обраование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>нет</option>
                                              <option>среднее</option>
                                              <option>высшее</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="about">почему вы хотите полететь?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                         <label for="form-group form-check">Укажите работу</label>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">врач</label>
                                        </div>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                        </div>
                                          <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                         <div class="туц">
                                            <input type="checkbox" class="ready?" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">готовы ли вы остаться на марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planetname>')
def choice(planetname):
    if request.method == 'GET':
        return f'''
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Реклама {planetname}!</title>
                      </head>
                      <body>
                       <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style/style.css')}" />
                    <h1>Моё предложение: {planetname}</h1>
                        <div class="alert alert-primary" role="alert">
                         {planetname} ближе к Земле;
                        </div>
                        <div class="alert alert-success" role="alert">
                          На этой планете много необходимых ресурсов;
                        </div>
                        <div class="alert alert-danger" role="alert">
                          На ней есть вода и атмосфера;
                        </div>
                        <div class="alert alert-info" role="alert">
                          На ней есть большое магнитное поле;
                        </div>
                        <div class="alert alert-dark" role="alert">
                          Наконец, она просто красива!
                        </div>
                      </body>
                    </html>
                   '''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    if request.method == 'GET':
        return f'''
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Результаты отбора</title>
                      </head>
                      <body>
                       <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style/style2.css')}" />
                    <h1>Результаты отбора</h1>
                        <div class="alert alert-primary" role="alert">
                        Претиндент на участие в миссии {nickname}
                        </div>
                        <div class="alert alert-success" role="alert">
                         Поздравляем! Ваш рейтинг после {level} этапа отбора
                        </div>
                        <div class="alert alert-danger" role="alert">
                          составляет {rating}!
                        </div>
                        <div class="alert alert-dark" role="light">
                          Желаем удачи!
                        </div>
                        </div>
                      </body>
                    </html>
                   '''


@app.route('/load_photo', methods=['GET'])
def load_photo():
    if request.method == 'GET':
        f = request.files['file']
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style/style1.css')}" />
                            <title>Пример загрузки файла</title>
                            <script type="text/javascript" src="{url_for('static', filename='js/js.js')}"></script>
                          </head>
                          <body>
                            <h1>Загрузка файла</h1>
                            <br>
                            <h2>для участия в миссии</h2>
                            <form class="login_form" method="post">
                                 <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <br>
                                            <img id="frame" src="" class="img-fluid" />
                                            <br>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/style/style.css')}" />
                    <title>Пейзажи Марса</title>
                </head>
                <body>
                <h1>Пейзажи Марса</h1>
                <div class="container">
                  <br>
                  <br>
                  <div id="C" class="carousel slide" data-ride="carousel">
                    <ol class="carousel-indicators">
                      <li data-target="#C" data-slide-to="1" class="active"></li>
                      <li data-target="#C" data-slide-to="2"></li>
                      <li data-target="#C" data-slide-to="3"></li>
                      <li data-target="#C" data-slide-to="4"></li>
                    </ol>
                    <div class="carousel-inner" role="listbox">
                      <div class="item active">
                        <img src="{url_for('static', filename='img/mars1.jpg')}" alt="First Slide">
                            <div class="carousel-caption d-none d-md-block">
                                <h4>Железный пейзаж</h4>
                                <p>Сверхчеткие снимки показывают нам сухой, скалистый рельеф,
                                 покрытый мелкой красной пылью.
                                    Красная пыль, на самом деле, - это оксид железа. Все, начиная от
                                 земли до маленьких камней и скал, покрыто этой пылью.
                                </p>
                            </div>
                      </div>
                      <div class="item">
                        <img src="{url_for('static', filename='img/mars2.jpg')}" alt="Second Slide">
                            <div class="carousel-caption d-none d-md-block">
                                <h4>Геологическая стабильность</h4>
                                <p>Так как на Марсе нет ни воды, ни подтвержденной тектонической
                                 активности, его геологические особенности остаются практически
                                 неизменными. По сравнению с поверхностью Земли, которая
                                 испытывает постоянные изменения, связанные с водной эрозией и
                                 тектонической активностью.
                                </p>
                            </div>
                      </div>
                      <div class="item">
                        <img class="d-block w-100" src="{url_for('static', filename='img/mars3.jpg')}" alt="Third Slide">
                        <div class="carousel-caption d-none d-md-block">
                            <h4>Скалистые ландшафты</h4>
                            <p>Ландшафт Марса состоит из разнообразных геологических структур.
                             Он является домом для самых высоких гор, известных во всей Солнечной системе.
                            </p>
                        </div>
                      </div>
                      <div class="item">
                        <img class="d-block w-100" src="{url_for('static', filename='img/mars4.jpg')}" alt="Fourth Slide">
                        <div class="carousel-caption d-none d-md-block">
                            <h4>Карьеры</h4>
                            <p>По мимо гор, на Марсе также много карьеров. Наиболее известный каньон
                             в Солнечной системе, это Долина Маринера, также находящаяся на
                             поверхности Красной планеты.
                            </p>
                        </div>
                      </div>
                    </div>
                    <a class="left carousel-control" href="#C" role="button" data-slide="prev">
                      <span class="glyphicon glyphicon-chevron-left" aria-hidden="false"></span>
                      <span class="sr-only">Previous</span>
                    </a>
                    <a class="right carousel-control" href="#C" role="button" data-slide="next">
                      <span class="glyphicon glyphicon-chevron-right" aria-hidden="false"></span>
                      <span class="sr-only">Next</span>
                    </a>
                  </div>
                </div>
                </body>
                </html>
                '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
