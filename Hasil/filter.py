from nltk import word_tokenize

fo = open('tweet.txt', 'r')
fw = open('tweet-ff.txt', 'a')
fg = open('tweet-gotg.txt', 'a')
keyword_ff = ['fast furious','fast n furious','fast and furious','ff8','fast & furious','fast furious 8','fast n furious 8','fast and furious 8','fast & furious 8']
keyword_gotg = ['guardians of the galaxy','gotg','guardians of the galaxy vol. 2','gotg vol. 2','gotg 2','guardians of the galaxy 2']
for line in fo:
	if any(ext.lower() in line for ext in keyword_ff):
		fw.write(line)	 
	if any(ext.lower() in line for ext in keyword_gotg):
		fg.write(line)	


	