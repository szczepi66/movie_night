from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
import time

#------------------------------------------------------------------------------------------------------

# def full_scrap():

#     driver.get("https://www.filmweb.pl/ranking/film")

#     driver.implicitly_wait(3)
#     cookies()
#     driver.implicitly_wait(3)
#     scrolling_page()
#     ranking = scraping()

#     title = []
#     year = []
#     genres = []
#     star_rating = []

#     for r in range(0,len(ranking)):
#         title.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__title').text)
#         year.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__year').text)
#         genres.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__genres').text[7:])
#         star_rating.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__rate--value').text)
        
#         time.sleep(3)
#         driver.quit()

# def cookies():
#     trust_consent = driver.find_element(By.ID, "buttons")
#     reject_consent = trust_consent.find_element(By.ID, "didomi-notice-agree-button").click()

# def scrolling_page():
#     for i in range(150):
#         html = driver.find_element(By.TAG_NAME, 'html')
#         html.send_keys(Keys.PAGE_DOWN)
    
# def scraping():
#     main = driver.find_element(By.CLASS_NAME, 'page__container.rankingTypeSection__container')
#     ranking = main.find_elements(By.CLASS_NAME, 'rankingType__card')
#     return ranking

# PATH = "/home/szczepi/glupoty/chromedriver"
# driver = webdriver.Chrome(PATH)
# full_scrap()

#------------------------------------------------------------------------------------------------------
    
# print(genres)
  
# title = ranking[1].find_element(By.CLASS_NAME , 'rankingType__title')
# year = ranking[1].find_element(By.CLASS_NAME, 'rankingType__year')
# genres = ranking[1].find_element(By.CLASS_NAME, 'rankingType__genres')
# star_raiting = ranking[1].find_element(By.CLASS_NAME, 'rankingType__rate--value')
    
# def choose_film():
#     print(23)

# def main():
#     exit = True
#     while exit == True:
#         decision = int(input("What do you want to do\n1. Choose a film\n2. aka\n3. exit\n"))
#         if decision == 1:
#             choose_film()
#         elif decision == 2:
#             print("aka")
#         elif decision == 3:
#             print("Bye bye, see you soon")
#             exit = False
#         else:
#             print("There is something wrong with your input try again\n")
                  

# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------------------------------

# import os
# os.system('cls||clear')
# ui = '''
# --------------------------------
# Nacisnij przyciski (1-3), aby wybrac co ciebie interesuje

# 1. Wybor filmu
# 2. Nieznana opcja
# 3. Wyjscie

# '''
# exit = True
# while exit == True:
#     decision = int(input(ui))
#     os.system('cls||clear')
#     if decision == 1:
#         print(1)
#         exit = False
#     elif decision == 2:
#         print(2)
#         exit = False
#     elif decision == 3:
#         print("Bye bye, see you soon")
#         exit = False
#     else:
#         print("There is something wrong with your input try again\n")