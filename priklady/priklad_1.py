"""
Příklad 1: První program, proměnné a datové typy.

Spusť tento soubor v terminálu příkazem:
    python priklady/priklad_1.py
"""

# Nejjednodušší program v Pythonu - vypíše text na obrazovku
print("Ahoj, světe!")

# Proměnná je pojmenované "místo v paměti", kam si ukládáme hodnotu.
# Python u proměnných nemusíme (a nemůžeme) předem určovat typ - pozná ho sám.
jmeno = "Petra"        # str  - textový řetězec (string)
vek = 21                # int  - celé číslo
vyska = 172.5           # float - desetinné číslo
je_studentka = True      # bool - pravda/nepravda (True/False)

# Funkce type() nám řekne, jakého typu proměnná je
print(jmeno, type(jmeno))
print(vek, type(vek))
print(vyska, type(vyska))
print(je_studentka, type(je_studentka))

# Jednoduché sečtení dvou čísel (aritmetickým operátorům se budeme
# podrobně věnovat až příští týden, tady jen ukázka)
soucet = vek + 5
print("Za pět let bude mít Petra", soucet, "let.")

# f-string (formátovaný řetězec) - nejpohodlnější způsob, jak vkládat
# hodnoty proměnných do textu. Před uvozovky se píše písmeno f
# a proměnná se vloží do složených závorek {}
print(f"Jmenuji se {jmeno}, je mi {vek} let a měřím {vyska} cm.")
