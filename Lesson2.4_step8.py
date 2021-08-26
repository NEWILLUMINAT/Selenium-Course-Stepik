from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)


def calc(num):
    return str(math.log(abs(12*math.sin(num))))


try:
    browser.implicitly_wait(12)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element_by_id("book")
    book_button.click()

    button = browser.find_element_by_id("solve")

    x = int(browser.find_element_by_id("input_value").text)
    answer_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    answer_field.send_keys(str(calc(x)))
    button.click()
finally:
    time.sleep(10)
    browser.quit()




