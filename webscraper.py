from selenium import webdriver

dailyGifts = "https://www.creativefabrica.com/daily-gifts/"
closePopup = "onesignal-slidedown-allow-button"

usernameStr = 'putYourUsernameHere'
passwordStr = 'putYourPasswordHere'
driver = webdriver.Firefox()
driver.get(dailyGifts)
driver.maximize_window()
# username = driver.find_element_by_id(i)
# username.send_keys(usernameStr)
nextButton = driver.find_element_by_id(closePopup).click()

popup = driver.find_element_by_link_text("Close").click()
driver.execute_script("window.scrollTo(0, 300)") 

downloadButton = driver.find_element_by_css_selector("span[class='btn-text']").click()

