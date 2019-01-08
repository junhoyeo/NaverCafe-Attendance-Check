import time
import json
import os.path
import schedule
from selenium import webdriver

# message to write in attendance list
MSG = '><'
with open('./secret.json') as f:
    DATA = json.load(f)
    URL = DATA['url']
    ELEMENT = DATA['element']


def check(driver):
    try:
        driver.get(URL)
        driver.find_element_by_css_selector(ELEMENT).click()
        for i in range(3):
            start_time = time.time()
            driver.implicitly_wait(2)  # 대기
            driver.switch_to.frame(driver.find_element_by_id('cafe_main'))
            driver.find_element_by_css_selector(
                'textarea#cmtinput').send_keys(MSG)
            driver.find_element_by_css_selector(
                'button#btn-submit-attendance').click()
            print((time.time() - start_time), 'success')
    except:
        check(driver)


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, './chromedriver')
    driver = webdriver.Chrome(driver_path)

    # login
    driver.get('https://nid.naver.com/nidlogin.login')
    input('🔓 Press ENTER after login')  # 로그인 대기

    schedule.every().day.at('00:00').do(check, driver)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
