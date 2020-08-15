import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import csv
import sys

#TF-IDF Test

# documentA = 'the man went out for a walk'
# documentB = 'the children sat around the fire'

# bagOfWordsA = documentA.split(' ')
# bagOfWordsB = documentB.split(' ')

# uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

# numOfWordsA = dict.fromkeys(uniqueWords, 0)
# for word in bagOfWordsA:
#     numOfWordsA[word] += 1
# numOfWordsB = dict.fromkeys(uniqueWords, 0)
# for word in bagOfWordsB:
#     numOfWordsB[word] += 1

# stopwords.words('english')

# def computeTF(wordDict, bagOfWords):
#     tfDict = {}
#     bagOfWordsCount = len(bagOfWords)
#     for word, count in wordDict.items():
#         tfDict[word] = count / float(bagOfWordsCount)
#     return tfDict

# tfA = computeTF(numOfWordsA, bagOfWordsA)
# tfB = computeTF(numOfWordsB, bagOfWordsB)

# def computeIDF(documents):
#     import math
#     N = len(documents)
    
#     idfDict = dict.fromkeys(documents[0].keys(), 0)
#     for document in documents:
#         for word, val in document.items():
#             if val > 0:
#                 idfDict[word] += 1
    
#     for word, val in idfDict.items():
#         idfDict[word] = math.log(N / float(val))
#     return idfDict

# idfs = computeIDF([numOfWordsA, numOfWordsB])

# def computeTFIDF(tfBagOfWords, idfs):
#     tfidf = {}
#     for word, val in tfBagOfWords.items():
#         tfidf[word] = val * idfs[word]
#     return tfidf

# tfidfA = computeTFIDF(tfA, idfs)
# tfidfB = computeTFIDF(tfB, idfs)
# df = pd.DataFrame([tfidfA, tfidfB])

# vectorizer = TfidfVectorizer()
# vectors = vectorizer.fit_transform([documentA, documentB])
# feature_names = vectorizer.get_feature_names()
# dense = vectors.todense()
# denselist = dense.tolist()
# df = pd.DataFrame(denselist, columns=feature_names)
# df.to_csv('pd_idf_test.csv')


#PF-IDF Test

docs = dict()
csv.field_size_limit(sys.maxsize)

count = 0
transcripts = dict()
with open("trumpspeeches2.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        transcripts[count] = row[1]
        docs[count] = []
        for i in range(3, len(row)):
            docs[count].append(row[i])
        count += 1



for i in range(len(docs)):
    for element in docs[i]:
        element = element.lower()
        string = 'Inaudible'
        if string in element:
            element = element.replace(string, '')

docA = docs[0]
docB = docs[1]

totalA = transcripts[0]
totalB = transcripts[1]

unique_phrases = set(docA).union(set(docB))

numOfWordsA = dict.fromkeys(unique_phrases, 0)
for word in docA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(unique_phrases, 0)
for word in docB:
    numOfWordsB[word] += 1


def computeTF(phraseDict, bag_phrase):
    tfDict = {}
    bag_phrase_count = len(bag_phrase)
    for phrase, count in phraseDict.items():
        tfDict[phrase] = count / float(bag_phrase_count)
    return tfDict

tfA = computeTF(numOfWordsA, docA)
tfB = computeTF(numOfWordsB, docB)

print(tfA, tfB)

def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for phrase, val in document.items():
            if val > 0:
                idfDict[phrase] += 1
    
    for phrase, val in idfDict.items():
        idfDict[phrase] = math.log(N / float(val))
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB])


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for phrase, val in tfBagOfWords.items():
        tfidf[phrase] = val * idfs[phrase]
    return tfidf

tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
df = pd.DataFrame([tfidfA, tfidfB])

df.to_csv('pd_idf_test.csv')