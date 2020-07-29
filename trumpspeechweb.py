from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
import time
import csv

d = DesiredCapabilities.CHROME

d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
action = webdriver.common.action_chains.ActionChains(driver)
driver.get("https://www.rev.com/blog/transcript-category/donald-trump-transcripts/page/3?view=all")
i = 11
val = driver.find_element_by_xpath("//*[@id=\"fl-main-content\"]/div[1]/div/div/div/div[4]/div/div/div/div/div[1]/div[" + str(i) + "]/div")
time.sleep(3)
action.move_to_element_with_offset(val, 0, 0)
time.sleep(3)
action.click()
action.perform()
print("Done")
action.move_to_element_with_offset(val, 10, 10)
time.sleep(2)
action.click()
action.perform()
print("Done")

temp_list = ['Date', 'Text']
temp_list[0] = driver.find_element_by_xpath("//*[@id=\"fl-main-content\"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/p").text
temp_list[1] = driver.find_element_by_xpath("//*[@id=\"transcription\"]/div/div/div/div/div").text

print(temp_list[0])
print(temp_list[1])


filename = "trumpspeeches.csv"
# writing to csv file
rows = list()
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
    csvwriter.writerow(temp_list)

driver.close()
#//*[@id="fl-main-content"]/div[1]/div/div/div/div[4]/div/div/div/div/div[1]/div[5]/div
#//*[@id="fl-main-content"]/div[1]/div/div/div/div[4]/div/div/div/div/div[1]/div[4]/div
#//*[@id="fl-main-content"]/div[1]/div/div/div/div[4]/div/div/div/div/div[1]/div[3]/div
#//*[@id="fl-main-content"]/div[1]/div/div/div/div[4]/div/div/div/div/div[1]/div[1]/div
