from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('index.html')


@app.route('/hello/')
def hello_world():
	header = '<h1>Hello, creature!</h1>'
	p1 = '<p>One day it will be all clear, I promise.</p>'
	p2 = '<p>But definitely not today... And not tomorrow.</p>'
	page = header + p1 + p2
	return page


if __name__ == '__main__':
	app.run(host='0.0.0.0')
