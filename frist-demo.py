from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("http://www.bing.com")
driver.quit()