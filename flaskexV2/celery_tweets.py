from flask import Flask
from flask_celery import make_celery

import swiftclient
import os

container_name = 'tweets'


#config connection
conn = swiftclient.Connection(
        user=os.environ['OS_USERNAME'],
        key=os.environ['OS_PASSWORD'],
	tenant_name=os.environ['OS_TENANT_NAME'],
	authurl=os.environ['OS_AUTH_URL'],
        auth_version=3
)

app = Flask(__name__)
app.config['CELERY_BROKER_URL']='amqp://guest@localhost//'
app.config['CELERY_BACKEND']='rpc://'


celery = make_celery(app)


#OBS har inte testat denna del av koden!
@app.route('/getTweets', methods=['GET']) 
#tells Flask which URL should trigger the function
def enfunktion():
	getTweets.delay()
	return "Ett test!"

@celery.task(name= 'celery_tweets.getTweets')
def getTweets():
	#hamta en lista med alla filer i containern
	for data in conn.get_container(container_name)[1]:
        	print '{0}\t{1}\t{2}'.format(data['name'], data['bytes'], data['last_modified'])
	#hamta objek data['name']
		obj_tuple = conn.get_object(container_name, data['name'])
		#with open(data['name'], 'w') as tweets:
        	#	tweets.write(obj_tuple[1])
	return 'klar'



if __name__ == '__main__':
	app.run(debug=True)


