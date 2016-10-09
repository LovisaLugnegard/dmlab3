from flask import Flask
from flask_celery import make_celery
import os

app = Flask(__name__)
app.config['CELERY_BROKER_URL']='amqp://guest@localhost//'
app.config['CELERY_BACKEND']='rpc://'


celery = make_celery(app)


#flask app part	
@app.route('/process/<name>')
def process(name):

	reverse.delay(name)
	return 'I sent an async request:)'

@celery.task(name='celery_example.reverse')
def reverse(string):
	return string[::-1]

if __name__ == '__main__':
	app.run(debug=True)

