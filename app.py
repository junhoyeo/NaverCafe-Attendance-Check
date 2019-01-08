import json, time, random
import logging
import os.path
from selenium import webdriver

URL = '???'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(CURRENT_DIR, './secret.json'), 'r') as file:
    user = json.load(file)

driver_path = os.path.join(CURRENT_DIR, './chromedriver')
driver = webdriver.Chrome(driver_path)

# login
driver.get('https://nid.naver.com/nidlogin.login')
input('press enter after login') # 로그인 대기

driver.get(URL)
driver.find_element_by_css_selector('a#menuLink46').click()
# driver.implicitly_wait(5)

# driver.execute_script('''
#     var cafe = document.getElementById('cafe_main').contentWindow.document;
#     cafe.getElementById('cmtinput').value = '><';
#     cafe.querySelector('button#btn-submit-attendance').click();
# ''')
driver.switch_to.frame(driver.find_element_by_id('cafe_main'))
driver.find_element_by_css_selector('textarea#cmtinput').send_keys('><')
driver.find_element_by_css_selector('button#btn-submit-attendance').click()
driver.quit()
