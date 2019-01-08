import time
import os.path
import schedule
from selenium import webdriver

URL = '???'

def check(driver):
    try:
        start_time = time.time()
        driver.get(URL)
        driver.find_element_by_css_selector('a#menuLink46').click()
        driver.implicitly_wait(2)  # 대기
        driver.switch_to.frame(driver.find_element_by_id('cafe_main'))
        driver.find_element_by_css_selector(
            'textarea#cmtinput').send_keys('><')
        driver.find_element_by_css_selector(
            'button#btn-submit-attendance').click()
        driver.quit()
        print((time.time() - start_time), 'success')
    except BaseException:
        check(driver)


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, './chromedriver')
    driver = webdriver.Chrome(driver_path)

    # login
    driver.get('https://nid.naver.com/nidlogin.login')
    input('press enter after login')  # 로그인 대기

    schedule.every().day.at('00:00').do(check, driver)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
