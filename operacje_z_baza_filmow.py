import sqlite3

def what_to_add():
    title = input("add name of the movie you want to add")
    genre = input("add genre of the movie you want to add")
    year = input("add year of the movie you want to add")
    rating = input("add rating of the movie you want to add")
    return title, genre, year, rating

def random_movie():
    command = "SELECT * FROM movies ORDER BY RANDOM() LIMIT 1;"
    c.execute(command)
    print(c.fetchall())

def choose_movie(genre, year, rating):
    command = "SELECT * FROM movies WHERE genre = " + genre
    command2 = "SELECT * FROM movies WHERE year = " + year
    command3 = "SELECT * FROM movies WHERE rating = " + rating
    c.execute(command)
    c.execute(command2)
    print(c.fetchall())
    


creating_table = "CREATE TABLE IF NOT EXISTS movies(title TEXT, genre TEXT, year INTEGER, rating REAL)"
insert_into = "INSERT INTO movies(title, genre, year, rating)VALUES (?, ?, ?, ?);"

conn = sqlite3.connect('movies.db')
c = conn.cursor()

# c.execute(creating_table)

# data_tuple = what_to_add()

# c.execute(insert_into, data_tuple)

# c.execute('SELECT * FROM movies')
# # c.execute('DELETE FROM movies WHERE rating = 7.31')
# print(c.fetchall())

genre = input("podaj gatunek")
year = input("podaj rok")
rating = input("podaj raing")

choose_movie(genre, year, rating)

# random_movie()

conn.commit()
conn.close()
