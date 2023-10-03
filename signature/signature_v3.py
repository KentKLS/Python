from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

driver = webdriver.Chrome()
driver.get('https://app.sowesign.com/sign/home/recovery/1012/5c0e7a5d-81d7-4c41-8fb4-78b32adbfc98')
action = ActionChains(driver)






with open("test.csv") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    coordinates = [ [round(float(row[0])), round(float(row[1]))]  for row in reader]
    

starting_point = [coordinates[0][0], coordinates[0][1]]




offsets = []
for i in range(0, len(coordinates)-1):
    offset = [ coordinates[i+1][0] - coordinates[i][0], coordinates[i+1][1] - coordinates[i][1]  ]
    offsets.append(offset)


time.sleep(3)


toClick = driver.find_element(By.CLASS_NAME,"sign-button" )
action\
    .move_to_element(toClick)\
    .click()\
    .perform()
canvas = driver.find_element(By.ID,'signature-pad')

def drawMain():
    action\
        .move_to_element(canvas)
    for offset in offsets[:55] :
        action.click_and_hold().move_by_offset(offset[0], offset[1]).release().perform()
    action.move_by_offset(offsets[55][0],offsets[55][1])
    for offset in offsets[56:67]:
        action.click_and_hold().move_by_offset(offset[0], offset[1]).release().perform()
    action.move_by_offset(50,-32)
    for offset in offsets[103:]:
        action.click_and_hold().move_by_offset(offset[0], offset[1]).release().perform()

drawMain()
toClick = driver.find_element(By.CLASS_NAME,"validate-button" )
action\
     .move_to_element(toClick)\
     .click()\
     .perform()
time.sleep(30)
