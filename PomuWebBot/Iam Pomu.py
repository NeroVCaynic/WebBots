import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://impomu.com/")
button = driver.find_element_by_id("im-pomu")
action = ActionChains(driver)
action.click(button)
#for x in range(500):
while True:
	action.perform()
	


