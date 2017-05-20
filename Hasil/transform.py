import json
fo = open('hasilstreaming.json', 'r')
fw = open('tweet.txt', 'a')
for line in fo:
	try:
		tweet = json.loads(line)
		fw.write(tweet['text']+"\n")
	except:
		continue