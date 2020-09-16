from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
import time
import csv

d = DesiredCapabilities.CHROME
x = 1
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
action = webdriver.common.action_chains.ActionChains(driver)
links = list()
dates = list()
for i in range(1, 260):
    driver.get("https://www.whitehouse.gov/briefings-statements/page/" + str(x))
    s = driver.page_source
    while(s.find("<article class=\"briefing") != -1):
        s = s[s.find("<a href=\""):]
        index1 = s.find("<a href=\"") + 9
        index2 = s.find("\">")
        links.append(s[index1:index2])
        index1 = s.find("<time>") + 6
        index2 = s.find("</time>")
        dates.append(s[index1:index2])
        s = s[s.find("<article class=\"briefing") + 1:]
    links.remove("https://www.whitehouse.gov")
    x += 1
times = list()
pages = list()
dates2 = list()
for i in range(len(links)):
    link = links[i]
    driver.get(link)
    page = driver.page_source
    element = driver.find_element_by_xpath("//*[@id=\"main-content\"]/div[1]/div/h1")
    if (element.text.lower().find("trump") != -1):
        try:
            element = driver.find_element_by_xpath("//*[@id=\"main-content\"]/div[2]/div/div/p[2]")
            times.append(element.text)
            #print("Success")
        except:
            times.append("Uknown")
            #print("Fail")
        try:
            element = driver.find_element_by_xpath("//*[@id=\"main-content\"]/div[2]/div/div")
            pages.append(element.text)
        except:
            pass
            #print("Fail")
        dates2.append(dates[i])
    time.sleep(1)
print("Sorting")
filename = "trumpspeeches3.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(len(times)):
        temp = list()
        temp.append(dates2[i])
        temp.append(times[i])
        temp.append(pages[i])
        csvwriter.writerow(temp)
print("Done")
