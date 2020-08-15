#Import packages
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import csv
import sys
from nltk.corpus import stopwords
def remove_stopwords(string):
    new_string = ""
    for word in string.split():
        if word not in stopwords.words("english"):
            new_string += word + " "
    return new_string[:len(new_string)-1]
'''
## Exapmple document (list of sentences)
doc = list()
csv.field_size_limit(sys.maxsize)
with open("trumpspeeches2.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in range(3, len(row)):
            doc.append(row[i])
# Tokenization of each document
tokenized_doc = []
for d in doc:
    if d.lower() not in stopwords.words("english"):
        tokenized_doc.append(word_tokenize(d.lower()))
print("TOKENIZED")
tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_doc)]
print("TAGGED")
model = Doc2Vec(tagged_data, vector_size=20, window=2, min_count=1, workers=4, epochs = 100)
model.save("test_doc2vec2.model")
print("SAVED")
'''
model= Doc2Vec.load("test_doc2vec2.model")
print(model.n_similarity(remove_stopwords("thanks everyone").split(), remove_stopwords("thanks all").split()))
