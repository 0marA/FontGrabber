import time
from selenium import webdriver
from loginInfo import USERNAME, PASSWORD
import keyboard


DAILY_GIFTS_URL = "https://www.creativefabrica.com/daily-gifts/"
CLOSE_POPUP_TAG = "onesignal-slidedown-allow-button"
JOIN_PROMPT_DIV = "promo-upsell-popup-freebie-close"

driver = webdriver.Firefox()
driver.get(DAILY_GIFTS_URL)
driver.maximize_window()

time.sleep(3)
driver.find_element_by_id(CLOSE_POPUP_TAG).click()
driver.find_element_by_link_text("Close").click()

driver.execute_script("window.scrollTo(0, 300)") 
downloadButton = driver.find_element_by_css_selector("span[class='btn-text']").click()

usernameBox = driver.find_element_by_name('username')
usernameBox.click()
usernameBox.send_keys(USERNAME)

passwordBox = driver.find_element_by_name('password')
passwordBox.click()
passwordBox.send_keys(PASSWORD)
keyboard.press_and_release("enter")

time.sleep(4)
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(1)
downloadButton = driver.find_element_by_css_selector("span[class='btn-text']").click()
time.sleep(5)
driver.quit()
