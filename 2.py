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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
