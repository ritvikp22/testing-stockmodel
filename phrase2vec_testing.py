from gensim.models.phrases import Phrases, Phraser 
import csv

with open("trumpspeeches.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
