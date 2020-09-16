import csv
import sys
import jellyfish

csv.field_size_limit(sys.maxsize)

source1list = list()
with open("trumptest.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        source1list.append(row)

source2list = list()
with open("trumpspeeches3.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        source2list.append(row)

rows = list()
index = 0
for i in range(len(source2list)):
    str1 = source2list[i][1]
    str2 = source1list[index][1]
    val = jellyfish.jaro_distance(str1, str2)
    if(val > 0.8):
        print(val)
        temp = list()
        temp.append(source1list[index][0])
        temp.append(source2list[i][0])
        temp.append(source1list[index][1])
        index += 1
        rows.append(temp)
    print(i)
    if(index >= len(source1list)):
        break
with open("trumpspeeches4.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
