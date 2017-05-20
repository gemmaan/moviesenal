import json
fo = open('hasilstreaming.json', 'r')
fw = open('tweet+location.txt', 'a')
for line in fo:
	try:
		tweet = json.loads(line)
		fw.write(tweet['text']+","+tweet['coordinates']+"\n")
	except:
		continue