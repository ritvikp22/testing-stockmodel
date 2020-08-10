#Import packages
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import csv
## Exapmple document (list of sentences)
doc = list()
with open("trumpspeeches2.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in range(3, len(rows)):
            doc.append(row[i])
        break
# Tokenization of each document
tokenized_doc = []
for d in doc:
    tokenized_doc.append(word_tokenize(d.lower()))
print(tokenized_doc)
tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_doc)]
print(tagged_data)
model = Doc2Vec(tagged_data, vector_size=20, window=2, min_count=1, workers=4, epochs = 100)
model.save("test_doc2vec.model")
model= Doc2Vec.load("test_doc2vec.model")
print(model.wv.vocab)
test_doc = word_tokenize("That is a good device".lower())
print(model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=5))