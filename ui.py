import scrap
import os
os.system('cls||clear')
ui = '''
--------------------------------
Nacisnij przyciski (1-3), aby wybrac co ciebie interesuje

1. Wylosuj film
2. Wybierz losowy film na podstawie kryteriów(gatunek, rok, ranking)
3. Wyjscie
4. Znajdź film
8. Stwórz bazę danych ze strony filmweb.pl(top 500) 
0. Wyjście

'''
exit = True
while exit == True:
    decision = int(input(ui))
    os.system('cls||clear')
    if decision == 1:
        print(1)
        # exit = False
    elif decision == 2:
        print(2)
        # exit = False
    elif decision == 3:
        print(2)
        # exit = False
    elif decision == 8:
        scrap.scrap()
        # exit = False
    elif decision == 0:
        print("Do zobaczenia później")
        exit = False
    else:
        print("Coś poszło nie tak\n")
