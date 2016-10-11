#Parse a tweet with python 

import json
	

from collections import Counter


#var used to count pronouns
pronomen = {'den':0, 'hon':0, 'det':0, 'han':0, 'hen':0, 'denna':0, 'denne':0}



#function to parse JSON document
def load_json_multiple(segments):
    chunk = ""
    for line in segments:
        chunk += line
        try:
            yield json.loads(chunk) #loads json to dict object
            chunk = ""
        except ValueError:
            pass


#count pronouns with Counter
with open('jsonTEST') as f:
   for parsed_json in load_json_multiple(f):
	count = Counter(parsed_json['text'].lower().split())
	for key in count:
		if key in pronomen:
			pronomen[key] += count[key]
#print key och print pronomen ar endast för att se vad som hander under tiden, ta bort sen
			print key
			print pronomen[key]


#save result in json-filen result.json
with open('result.json', 'w') as fp:
    json.dump(pronomen, fp)
print pronomen

#def count_many(needles, haystack):
 #   count = Counter(haystack.split())
  #  return {key: count[key] for key in count if key in needles}





