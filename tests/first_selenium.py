from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://pythonexamples.org/tmp/selenium/index-12.html')

driver.save_screenshot("screenshot.png")

time.sleep(5)
driver.quit()