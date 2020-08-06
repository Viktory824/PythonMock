from faker import Faker
from flask import Flask
from flask import jsonify

app = Flask(__name__)


# @app.route('/hello')
@app.route('/')
def hello_world():
    return 'Hello there!'


@app.route('/text')
def get_text():
    fake = Faker('ru_RU')
    return fake.text()


# '/post/<int:post_id>'
@app.route('/<int:num>')
def get_num(num):
    return jsonify({'num': num})


@app.route('/books')
def get_dct():
    dct = {'Eddins': 'Image Processing with MATLAB',
           'Dickens': 'Christmas Carol',
           'Foreman': 'Data Smart',
           'Archer': 'False Impressions',
           'Hemingway': 'Farewell to Arms'
           }
    return jsonify(dct)


app.run(host='0.0.0.0', port=8080, debug=True)
