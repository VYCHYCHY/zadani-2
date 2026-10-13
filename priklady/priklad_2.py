"""
Příklad 2: Vstup od uživatele (input) a práce s f-stringy.

Spusť tento soubor v terminálu příkazem:
    python priklady/priklad_2.py
"""

# Funkce input() vypíše zadaný text a počká, až uživatel něco napíše
# a stiskne Enter. Vrácená hodnota je VŽDY typu str (řetězec)!
jmeno = input("Jak se jmenuješ? ")
print(f"Ahoj, {jmeno}!")

# Pokud chceme od uživatele číslo, musíme text (str) převést pomocí
# funkce int() nebo float()
vek_text = input("Kolik je ti let? ")
vek = int(vek_text)  # převod textu na celé číslo

# Stejnou věc můžeme zapsat i na jeden řádek:
# vek = int(input("Kolik je ti let? "))

za_deset_let = vek + 10
print(f"Za deset let ti bude {za_deset_let} let.")

# f-stringy umí i formátování čísel, například zaokrouhlení na
# 2 desetinná místa pomocí ":.2f"
vaha = float(input("Kolik vážíš (kg)? "))
print(f"Tvoje váha je {vaha:.2f} kg.")
