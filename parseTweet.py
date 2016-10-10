#Parse a tweet with python 

import json
	

from collections import Counter


#var used to count pronouns
pronomen = {'den':0, 'hon':0, 'det':0, 'han':0, 'hen':0, 'denna':0, 'denne':0}

#json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

#parsed_json = json.loads(json_string) #loads is for string or unicode, load is for file or file-like object	

#print(parsed_json['first_name'])


#with open('inputJSONtest.json') as json_data:
#	data = json.load(json_data) 
#	print(data['text'])

	#for line in data:
#		print line.get('text')

	#for line in json_data:
	#	tweet =json.loads(line)
	#	print tweet['text']

#function to parse JSON document
def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
            yield json.dumps(chunk) #dumps loads json to string
            chunk = ""
        except ValueError:
            pass


#count pronouns with Counter
with open('inputJSONtest.json') as f:
   for parsed_json in load_json_multiple(f):
	count = Counter(parsed_json.split())
	for key in count:
		if key in pronomen:
			pronomen[key] += count[key]
			print key
			print pronomen[key]
		#	print parsed_json['text'] 
	#	nrden += 1
	#	print parsed_json['text']
	#	print nrden

#def count_many(needles, haystack):
 #   count = Counter(haystack.split())
  #  return {key: count[key] for key in count if key in needles}





