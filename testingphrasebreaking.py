import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import csv
import os
import sys
#If not done on the device running this code already, run import nltk then nltk.download() in python shell to download necesary libraries
csv.field_size_limit(sys.maxsize)
rows = list()
donelist = list()
length = 0
f = open("trumpspeeches4.csv")
length = len(f.readlines())
#print(length)
with open("trumpspeeches4.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
index = 0
while(index < length):
    tokenized = sent_tokenize(rows[index][2])
    temp_counter = 0
    counter = 0
    sums = 0
    vals = list()
    for i in tokenized: 
        wordsList = nltk.word_tokenize(i) 
        tagged = nltk.pos_tag(wordsList)
        dotry = False
        temp_val = ""
        for i in range(len(tagged)):
            if(tagged[i][1] == "IN"):
                dotry = True
                temp_counter = i
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
    sums = 0
    counter = 0
    for val in vals:
        counter += 1
        sums += len(val.split())
    avg_word_list = [sums/counter]
    with open("trumpspeeches5.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(donelist)
        csvwriter.writerow(rows[index] + vals)
        donelist.append(rows[index] + avg_word_list + vals)
    print(index, ", :", avg_word_list)
    index += 1
print("Done")
