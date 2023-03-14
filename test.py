import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

def insertVaribleIntoTable(title, genre, year, rating):
    try:
        sqliteConnection = sqlite3.connect('movies.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO movies
                          (title, genre, year, rating) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (title, genre, year, rating)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        # print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

conn = sqlite3.connect('movies.db')
c = conn.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
movies(title TEXT, genre TEXT, year INTEGER, rating REAL)"""

c.execute(command1)

conn.commit()
# conn.close()

def cookies():
    trust_consent = driver.find_element(By.ID, "buttons")
    reject_consent = trust_consent.find_element(By.ID, "didomi-notice-agree-button").click()
    driver.implicitly_wait(1)
    reklama = driver.find_element(By.CLASS_NAME, "ws")
    skip_reklama = reklama.find_element(By.CLASS_NAME, "ws__skipButton").click()

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
time.sleep(25)
scrolling_page()
ranking = scraping()

for r in range(0,len(ranking)):
    insertVaribleIntoTable(ranking[r].find_element(By.CLASS_NAME , 'rankingType__title').text,
                        ranking[r].find_element(By.CLASS_NAME , 'rankingType__genres').text[7:],
                        ranking[r].find_element(By.CLASS_NAME , 'rankingType__year').text,
                        ranking[r].find_element(By.CLASS_NAME , 'rankingType__rate--value').text)


time.sleep(3)
driver.quit()

# c.execute('''
#                   CREATE TABLE IF NOT EXISTS movies
#                   ([title] TEXT,[genre] TEXT, [year] INTEGER, [rating] REAL)
#                   ''')
# conn = sqlite3.connect('movies')
# c = conn.cursor()

# c.execute('SELECT * FROM movies')

# c.close()

# c.execute('''
#                   CREATE TABLE IF NOT EXISTS movies
#                   ([title] TEXT,[genre] TEXT, [year] INTEGER, [rating] REAL)
#                   ''')

# c.execute('''
#                   INSERT INTO movies (title, genre, year, rating)
                  
#                     VALUES
#                     ('szybcy i wsciekli', 'akcja', 2012, 3.8),
#                     ('szybcy i smutni', 'dramat', 2005, 3.8)
                    
#                   ''')

# c.execute('''
#                   SELECT
#                   a.title,
#                   b.genre,
#                   c.year,
#                   d.rating
#                   ''')

# for r in range(0,len(ranking)):
#     c.execute('INSERT INTO movies VALUES(?,?,?,?)', r)

# for r in range(0,len(ranking)):
#     title.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__title').text)
#     year.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__year').text)
#     genres.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__genres').text[7:])
#     star_rating.append(ranking[r].find_element(By.CLASS_NAME , 'rankingType__rate--value').text)
    
#     time.sleep(3)
#     driver.quit()

# for row in c.execute('SELECT * FROM movies;'):
#     print(row)

# # df = pd.DataFrame(c.fetchall(), columns=['title','genre','year','rating'])
# # print(df)

# conn.commit()

# conn.close()