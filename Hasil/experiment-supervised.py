import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.linear_model import SGDClassifier
from sklearn import svm
import numpy as np
from sklearn import metrics
from nltk import FreqDist

csv.field_size_limit(500000)

#fungsi untuk load dataset
def load_data(dataset):
    sentences = []
    labels = []
    
    with open(dataset, 'rU') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
               text = row['text']
               type = row['type']

               sentences.append(text)
               labels.append(type)
            except:
                continue
    return sentences, labels


##how to load dataset

train_sentences, train_labels = load_data("dataset/data-train.csv")
test_ff = open('tweet-ff.tweets', 'r')
test_gotg = open('tweet-gotg.tweets', 'r')

#Tokenizing text
count_vect = CountVectorizer()

#transform ke bentuk vector pake tf-idf
X_train_counts = count_vect.fit_transform(train_sentences)
# tfidf_transformer = TfidfTransformer(smooth_idf=False) #pake tf
# tfidf_transformer = TfidfTransformer(smooth_idf=True) #pake idf
tfidf_transformer = TfidfTransformer() #pake tfidf
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
# print X_train_tfidf
print X_train_counts.shape
print count_vect.vocabulary_.get(u'algorithm')

#text classification algorithm
clf = SGDClassifier().fit(X_train_tfidf, train_labels)
# clf = svm.SVC().fit(X_train_tfidf, train_labels)
# clf = svm.SVC(kernel='linear', probability=True, class_weight='auto').fit(X_train_tfidf, train_labels)


#ubah data test ke bentuk vector tfidf
X_new_counts = count_vect.transform(test_gotg)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

#prediksi data test
predicted = clf.predict(X_new_tfidf)

#print label data test
score_arr=[]
for category in predicted:
   print category
   score_arr.append(category)

#cek akurasi
X_old_counts = count_vect.transform(train_sentences)
X_old_tfidf = tfidf_transformer.transform(X_old_counts)
predicted_train = clf.predict(X_old_tfidf)
# print 'Akurasi:'
# print np.mean(predicted == test_labels)
score_fd=FreqDist(score_arr)     
score_fd.plot(cumulative=False) 
# for doc, category in zip(docs_new, predicted):
#   print('%r,%s' % (doc, predicted))

