from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/signature/signatutest.html')
action = ActionChains(driver)

time.sleep(2)

# toClick = driver.find_element(By.CLASS_NAME,"sign-button" )
# action\
#     .move_to_element(toClick)\
#     .click()\
#     .perform()

canvas = driver.find_element(By.ID,'signature-pad')
def draw_on_canvas():
    action\
        .move_to_element(canvas)\
        .move_by_offset(-300, -200)\
        .move_by_offset(336, 111)\
        .click_and_hold()\
        .move_by_offset(25, 5)\
        .move_by_offset(5, 10)\
        .move_by_offset(-10, 5)\
        .move_by_offset(-75,15)\
        .move_by_offset(5,-5)\
        .move_by_offset(5,5)\
        .move_by_offset(-10,10)\
        .release()\
        .move_by_offset(40, -33)\
        .click_and_hold()\
        .move_by_offset(-5,5)\
        .move_by_offset(5,5)\
        .move_by_offset(-5,5)\
        .release()\
        .move_by_offset(12, -15)\
        .click_and_hold()\
        .move_by_offset(5,0)\
        .move_by_offset(3,3)\
        .move_by_offset(0,5)\
        .move_by_offset(-3,3)\
        .move_by_offset(-5,0)\
        .move_by_offset(-3,-3)\
        .move_by_offset(0,-5)\
        .move_by_offset(3,-3)\
        .release()\
        .move_by_offset(5,8)\
        .click_and_hold()\
        .move_by_offset(7,7)\
        .release()\
        .perform()

draw_on_canvas()
time.sleep(10)