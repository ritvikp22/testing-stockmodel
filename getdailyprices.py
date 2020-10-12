import sys
import csv
import yfinance as yf

stock = yf.Ticker("SWPPX")
csv.field_size_limit(sys.maxsize)
def monthToNum(shortMonth):
    return {
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9, 
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
    }[shortMonth]
dates = list()
times = list()
speeches = list()
phrases = list()
stock_open = list()
stock_close = list()
length = 0
with open("trumpspeeches5.csv", 'r') as csvfile:
    for row in csv.reader(csvfile):
        length += 1
        dates.append(row[0])
        times.append(row[1])
        speeches.append(row[2])
        phrases.append(row[4:])
for i in range(length):
    date = dates[i]
    year = date[date.find(", ") + 2:]
    month = monthToNum(date[:3])
    day = int(date[4:date.find(", ")])
    monthString = str(month)
    if(month < 10):
        monthString = "0" + monthString
    dayString = str(day)
    if(day < 10):
        dayString = "0" + dayString
    data = stock.history(start=year+"-"+monthString+"-"+dayString, end="2020-10-11")
    if(i == 0):
        print(year, monthString, dayString)
        print(data)
        print(str(data['Open']).split(" "))
        print(str(data['Open']).split(" ")[0][5:])
        print(year+"-"+monthString+"-"+dayString)
    openPrice = -1.0
    closePrice = -1.0
    if(str(data['Open']).split(" ")[0][5:] == year+"-"+monthString+"-"+dayString):
        openPrice = data['Open'][0]
        closePrice = data['Open'][1]
    stock_open.append(openPrice)
    stock_close.append(closePrice)
print(stock_open[0], stock_close[0])
with open("trumpspeecheswithstocks.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(length):
        temp_val = list()
        temp_val.append(dates[i])
        temp_val.append(times[i])
        temp_val.append(stock_open[i])
        temp_val.append(stock_close[i])
        temp_val.append(speeches[i])
        temp_val.append(phrases[i])
        csvwriter.writerow(temp_val)
