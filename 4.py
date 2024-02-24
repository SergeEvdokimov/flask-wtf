from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        text = 'Инженерные тренажеры'
        pic = url_for('static', filename='img/ship.jpg')
    else:
        text = 'Научные симуляторы'
        pic = url_for('static', filename='img/ship.png')
    return render_template('2.html', text=text, pic=pic)


@app.route('/list_prof/<tp>')
def show_list(tp):
    if tp not in ['ol', 'ul']:
        return render_template('base.html', title='НЕВЕРНЫЙ ПАРАМЕТР')
    return render_template('3.html', tp=tp)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    url_style = url_for('static', filename='css/style.css')
    params = {'url_style': url_style, 'title': 'Анкета', 'surname': 'Wanty', 'name': 'Mark',
              'education': 'выше среднего', 'profession': 'штурман марсохода', 'sex': 'male',
              'motivation': 'Всегда мечтал застрять на Марсе!', 'ready': True}
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
