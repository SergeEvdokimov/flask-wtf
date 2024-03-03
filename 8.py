from flask import *
import json

app = Flask(__name__)


@app.route('/')
def default():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    text = '''Человечество вырастает из детства.
    Человечеству мала одна планета.
    Мы сделаем обитаемыми безжизненные пока планеты.
    И начнем с Марса!
    Присоединяйся!'''
    return '</br>'.join(text.split('\n'))


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='mars.jpeg')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <h2>Вот она какая, красная планета</h2>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    topics = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    url_pic = url_for('static', filename='img/mars.jpeg')
    url_style = url_for('static', filename='css/style.css')
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         rel="stylesheet"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_style}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_pic}" alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert-dark" role="alert">
                          <br><h3>{topics[0]}</h3>
                        </div>
                        <div class="alert-success" role="alert">
                          <br><h3>{topics[1]}</h3>
                        </div>
                        <div class="alert-secondary" role="alert">
                          <br><h3>{topics[2]}</h3>
                        </div>
                        <div class="alert-warning" role="alert">
                          <br><h3>{topics[3]}</h3>
                        </div>
                        <div class="alert-danger" role="alert">
                          <br><h3>{topics[4]}</h3>
                        </div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">

                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h4 align="center">на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" 
                                    id="surname" aria-describedby="surnamelHelp" 
                                    placeholder="Введите фамилию" name="lastname">

                                    <input type="text" class="form-control" id="name" 
                                    placeholder="Введите имя" name="name">

                                    <br>
                                    <input type="email" class="form-control" id="email" 
                                    placeholder="Введите адрес почты" name="email">

                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu_lvl">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Имею несколько высших образований</option>
                                        </select>
                                     </div>
                                        <label for="eduSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="spec1" name="spec1">
                                        <label class="form-check-label" for="spec1">
                                        Инженер-исследователь</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec2" name="spec2">
                                        <label class="form-check-label" for="spec2">
                                        Пилот</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec3" name="spec3">
                                        <label class="form-check-label" for="spec3">
                                        Инженер-строитель</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec4" name="spec4">
                                        <label class="form-check-label" for="spec4">
                                        Строитель</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec5" name="spec5">
                                        <label class="form-check-label" for="spec5">
                                        Экзобиолог</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec6" name="spec6">
                                        <label class="form-check-label" for="spec6">
                                        Врач</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec7" name="spec7">
                                        <label class="form-check-label" for="spec7">
                                        Инженер по терраформированию</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec8" name="spec8">
                                        <label class="form-check-label" for="spec8">
                                        Климатолог</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec9" name="spec9">
                                        <label class="form-check-label" for="spec9">
                                        Специалист по радиационной защите</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec10" name="spec10">
                                        <label class="form-check-label" for="spec10">
                                        Астрогеолог</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec11" name="spec11">
                                        <label class="form-check-label" for="spec11">
                                        Гляциолог</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec12" name="spec12">
                                        <label class="form-check-label" for="spec12">
                                        Инженер жизнеобеспечения</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec13" name="spec13">
                                        <label class="form-check-label" for="spec13">
                                        Метеоролог</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec14" name="spec14">
                                        <label class="form-check-label" for="spec14">
                                        Оператор марсохода</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec15" name="spec15">
                                        <label class="form-check-label" for="spec15">
                                        Киберинженер</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec16" name="spec16">
                                        <label class="form-check-label" for="spec16">
                                        Штурман</label>
                                        <br><input type="checkbox" class="form-check-input" id="spec17" name="spec17">
                                        <label class="form-check-label" for="spec17">
                                        Пилот дронов</label>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">

                                          <input class="form-check-input" type="radio" name="sex" id="male" 
                                          value="male" checked>

                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">

                                          <input class="form-check-input" type="radio" name="sex" id="female"
                                           value="female">

                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="5" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">

                                        <label class="form-check-label" for="acceptRules">
                                        Готовы ли Вы остаться на Марсе?</label>

                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('lastname', "-"))
        print(request.form.get('name', "-"))
        print(request.form.get('email', "-"))
        print(request.form.get('edu_lvl', "-"))
        print(request.form.get('file', "-"))
        print(request.form.get('about', "-"))
        print(request.form.get('accept', "-"))
        print(request.form.get('sex', "-"))
        print(request.form.get('spec1', "-"))
        print(request.form.get('spec2', "-"))
        print(request.form.get('spec3', "-"))
        print(request.form.get('spec4', "-"))
        print(request.form.get('spec5', "-"))
        print(request.form.get('spec6', "-"))
        print(request.form.get('spec7', "-"))
        print(request.form.get('spec8', "-"))
        print(request.form.get('spec9', "-"))
        print(request.form.get('spec10', "-"))
        print(request.form.get('spec11', "-"))
        print(request.form.get('spec12', "-"))
        print(request.form.get('spec13', "-"))
        print(request.form.get('spec14', "-"))
        print(request.form.get('spec15', "-"))
        print(request.form.get('spec16', "-"))
        print(request.form.get('spec17', "-"))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choices(planet_name):
    topics = ['На ней много необходимых ресурсов;',
              'На ней есть вода и атмосфера;',
              'На ней есть небольшое магнитное поле;',
              'Наконец, она просто красива!']
    url_style = url_for('static', filename='css/style.css')
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         rel="stylesheet"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_style}" />
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <h3>Эта планета близка к Земле;</h3>
                        <div class="alert-success" role="alert">
                          <br><h3>{topics[0]}</h3>
                        </div>
                        <div class="alert-secondary" role="alert">
                          <br><h3>{topics[1]}</h3>
                        </div>
                        <div class="alert-warning" role="alert">
                          <br><h3>{topics[2]}</h3>
                        </div>
                        <div class="alert-danger" role="alert">
                          <br><h3>{topics[3]}</h3>
                        </div>
                      </body>
                    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    url_style = url_for('static', filename='css/style.css')
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         rel="stylesheet"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_style}" />
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h3>Претендента на участие в миссии {nickname}</h3>
                        <div class="alert-success" role="alert">
                          <br><h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                        </div>
                        <div class="alert-light" role="alert">
                          <br><h3>Составляет {rating}!</h3>
                        </div>
                        <div class="alert-warning" role="alert">
                          <br><h3>Желаем удачи!</h3>
                        </div>
                      </body>
                    </html>"""


@app.route('/carousel')
def carousel():
    url_style = url_for('static', filename='css/style.css')
    return f'''
    <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

            <link rel="stylesheet" type="text/css" href="{url_style}" />
            <title>Варианты выбора</title>
          </head>
          <body>
            <h1>Пейзажи Марса</h1>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
            <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="{url_for('static', filename='img/mars.jpg')}" class="d-block w-100" alt="1">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/mars.jpeg')}" class="d-block w-100" alt="2">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="2">
                </div>
                <div class="carousel-item">
                  <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-100" alt="3">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          <body>
        </html>'''


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return render_template("9.html")
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/member')
def show_member():
    with open('templates/members.json', encoding='utf-8') as file:
        js = json.load(file)
    return render_template("8.html", js=js['members'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
