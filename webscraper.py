from selenium import webdriver
import keyboard
import time

dailyGifts = "https://www.creativefabrica.com/daily-gifts/"
closePopup = "onesignal-slidedown-allow-button"

driver = webdriver.Firefox()
driver.get(dailyGifts)
driver.maximize_window()

driver.find_element_by_id(closePopup).click()
driver.find_element_by_link_text("Close").click()

driver.execute_script("window.scrollTo(0, 300)") 
downloadButton = driver.find_element_by_css_selector("span[class='btn-text']").click()

username = driver.find_element_by_name('username')
username.click()
username.clear
username.send_keys("engineermachine@outlook.com")

password = driver.find_element_by_name('password')
password.click()
password.clear
password.send_keys("bruhapple")
keyboard.press_and_release("enter")

time.sleep(4)
driver.execute_script("window.scrollTo(0, 300)") 
downloadButton = driver.find_element_by_css_selector("span[class='btn-text']").click()
