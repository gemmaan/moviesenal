from nltk import word_tokenize, pos_tag, FreqDist, tag

fw = open('tweet-ff.txt', 'r')
fn = open('negative-ff.txt', 'a')
fp = open('positive-ff.txt', 'a')

fg = open('tweet-gotg.txt', 'r')
fng = open('negative-gotg.txt', 'a')
fpg = open('positive-gotg.txt', 'a')

def loadWordset(filestp):
    wordSet = []
    file = open(filestp, 'r')
    for line in file:
        line = line.strip().lower()
        wordSet.append(line)
    return wordSet
# sebelum masuk ke pos tagger harus di tokenize dulu
# tokenize tidak hanya dengan spasi. kalau ada "saya makan mie, nasi goreng, ..." kalo hanya dnegan spasi jadinya "mie,"
# tokenize menggunakan machine learning
####Sentence Tokenizer####
posWordSet = loadWordset('positive-words.txt')
negWordSet = loadWordset('negative-words.txt')

for tweet in fw:
	tokens = word_tokenize(tweet)	
	tagged_tweet = pos_tag(tokens)

	for (word,tag) in tagged_tweet:
		if tag=='JJ':
			# kalau dia ada di file negative, tulis ke negative txt
			if word in posWordSet:
				fp.write(word+'\n')	
			# kalau dia ada di file positive, tulis ke positive txt
			if word in negWordSet:
				fn.write(word+'\n')	

for tweet in fg:
	tokens = word_tokenize(tweet)	
	tagged_tweet = pos_tag(tokens)

	for (word,tag) in tagged_tweet:
		if tag=='JJ':
			# kalau dia ada di file negative, tulis ke negative txt
			if word in posWordSet:
				fpg.write(word+'\n')	
			# kalau dia ada di file positive, tulis ke positive txt
			if word in negWordSet:
				fng.write(word+'\n')	
# print tagged_all
# tag_fd = FreqDist(tag for (word, tag) in tagged_all)

#plot frequency distribution
# tag_fd.plot(cumulative=False) 

# # mencari kata-kata sifat
# # keuarannya list of word, untuk semua pasang word,tag di tagged yang tagnya 'jj'
# adjectives = [word for (word,tag) in tagged if tag == 'JJ']
# print adjectives 



