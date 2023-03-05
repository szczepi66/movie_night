# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.wait import WebDriverWait
# import time

# PATH = "/home/szczepi/glupoty/chromedriver"
# driver = webdriver.Chrome(PATH)

# driver.get("https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular?page=4")

# driver.implicitly_wait(3)

# trust_consent = driver.find_element(By.ID, "onetrust-consent-sdk")
# reject_consent = trust_consent.find_element(By.ID, "onetrust-reject-all-handler").click()
# main = driver.find_element(By.ID, 'main_container')
# titles = main.find_elements(By.CLASS_NAME, 'p--small')
# for t in titles:
#     print(t.text)
    
# time.sleep(3)

# driver.quit()

# element = driver.find_element(By.TAG_NAME, 'div')

# elements = element.find_elements(By.CLASS_NAME, 'p--small')
# for e in elements:
#     print(e.text)

# search = driver.find_element(By.NAME, "s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# time.sleep(10)

# header = driver.find_element(By.CLASS_NAME, "entry-title")
# print(header.text)

# time.sleep(10)

# driver.quit()