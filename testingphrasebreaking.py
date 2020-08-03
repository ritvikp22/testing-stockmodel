import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import csv
import os
#If not done on the device running this code already, run import nltk then nltk.download() in python shell to download necesary libraries
txt = ""
with open("trumpspeeches.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        txt = row[1]
        break

tokenized = sent_tokenize(txt)
vals = list()
for i in tokenized: 
    wordsList = nltk.word_tokenize(i) 
    tagged = nltk.pos_tag(wordsList)
    dotry = False
    temp_val = ""
    for i in range(len(tagged)):
        if(tagged[i][1] == "IN"):
            dotry = True
        if(dotry):
            temp_val += tagged[i][0] + " "
        if(tagged[i][1] == "CC"):
            dotry = False
            temp_val = ""
        if(tagged[i][1] == "NN" or tagged[i][1] == "NNS"):
            dotry = False
            vals.append(temp_val[0: len(temp_val)-1])
            temp_val = ""
i = 0
while(i < len(vals)):
    if(vals[i] == '' or vals[i] == ' '):
        vals.remove(vals[i])
        i -= 1
    i += 1
print(vals)
