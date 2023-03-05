from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
import time

def cookies():
    trust_consent = driver.find_element(By.ID, "buttons")
    reject_consent = trust_consent.find_element(By.ID, "didomi-notice-agree-button").click()

def scrolling_page():
    for i in range(150):
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.PAGE_DOWN)
    
def scraping():
    main = driver.find_element(By.CLASS_NAME, 'page__container.rankingTypeSection__container')
    ranking = main.find_elements(By.CLASS_NAME, 'rankingType__card')
    return ranking

PATH = "/home/szczepi/glupoty/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.filmweb.pl/ranking/film")

driver.implicitly_wait(3)
cookies()
driver.implicitly_wait(3)
scrolling_page()
ranking = scraping()

title = []
year = []
genres = []
star_rating = []

for r in range(0,len(ranking)):
    title.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__title').text)
    year.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__year').text)
    genres.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__genres').text[7:])
    star_rating.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__rate--value').text)
    
    time.sleep(3)
    driver.quit()
    