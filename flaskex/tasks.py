from celery import Celery
import time

app = Celery('tasks', broker='amqp://guest@localhost//', backend='rpc://')

@app.task
def reverse(string):
	time.sleep(10)
	return string[::-1]
