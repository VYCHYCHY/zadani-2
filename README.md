# Týden 01 – Úvod a základy

## Cíl lekce
- Nainstalovat si Python a VS Code a spustit první program.
- Naučit se pracovat s proměnnými a základními datovými typy (`int`, `float`, `str`, `bool`).
- Umět načíst vstup od uživatele pomocí `input()` a vypsat výstup pomocí `print()` a f-stringů.

## Výklad

### Instalace
1. Stáhni a nainstaluj Python z [python.org](https://www.python.org/downloads/) (při instalaci na Windows zaškrtni "Add python.exe to PATH").
2. Stáhni a nainstaluj [VS Code](https://code.visualstudio.com/) a v něm rozšíření **Python** (od Microsoftu).
3. Ověř instalaci v terminálu:
   ```bash
   python --version
   ```

### První program
```python
print("Ahoj, světe!")
```
Funkce `print()` vypíše text na obrazovku (do konzole).

### Proměnné a datové typy
Proměnná je pojmenované místo v paměti pro uloženou hodnotu. Python typ proměnné pozná sám podle přiřazené hodnoty:

```python
jmeno = "Petra"      # str   - text (v uvozovkách)
vek = 21              # int   - celé číslo
vyska = 172.5         # float - desetinné číslo
je_studentka = True    # bool  - True / False
```

Typ hodnoty zjistíš funkcí `type()`.

### Vstup a výstup
```python
jmeno = input("Jak se jmenuješ? ")   # input() vždy vrací str
vek = int(input("Kolik je ti let? ")) # převod textu na číslo pomocí int()
print(f"Ahoj, {jmeno}, za rok ti bude {vek + 1} let.")
```

f-string (řetězec s předponou `f`) umožňuje vkládat hodnoty proměnných přímo do textu pomocí `{}`.

Podrobné okomentované ukázky najdeš v souborech `priklady/priklad_1.py` a `priklady/priklad_2.py` - projdi si je a zkus si je spustit.

## Poznámky pro výklad (doporučený postup)

Poznámky pro učitele k vedení hodiny u jednotlivých cvičení. Bez časového rozpisu – jen doporučený postup, na co se zaměřit a časté chyby studentů.

### Úkol 1 – `pozdrav(jmeno)`
- Doporučený postup výkladu: nejprve zopakuj, že funkce v Pythonu vrací hodnotu pomocí `return`, ne `print()` – studenti si to často pletou z předchozí ukázky v `priklady/`. Ukaž rozdíl mezi vypsáním textu a jeho vrácením z funkce.
- Na co se zaměřit: skládání řetězců (spojování textu a proměnné) – f-string je nejpřirozenější volba, protože ji už viděli v `priklady/priklad_2.py`.
- Časté chyby studentů: zapomenutý `return` (funkce pak vrací `None` a test selže); použití `print()` místo `return`; špatně umístěná interpunkce v pozdravu (mezera, vykřičník).
- Tip: nech studenty nahlas popsat vstup a výstup funkce ještě předtím, než začnou psát kód – pomůže to ujasnit, co přesně má funkce vrátit.

### Úkol 2 – `secti(a, b)`
- Doporučený postup výkladu: krátce zopakuj aritmetické operátory a rozdíl mezi `int` a `float` u výsledku sčítání.
- Na co se zaměřit: že funkce nemusí vstupy nijak převádět – přijímá čísla tak, jak jsou (na rozdíl od `input()`, který vždy vrací text).
- Časté chyby studentů: pokus o převod parametrů pomocí `int()`/`str()`, i když to není potřeba; opět zapomenutý `return`.
- Tip: propoj s částí o `input()` z výkladu – uveď kontrast, kdy je převod typu potřeba (data z `input()`) a kdy ne (data už jsou čísla).

### Úkol 3 – `preved_na_text(cislo)`
- Doporučený postup výkladu: naváže přímo na sekci o f-stringech z výkladu – zdůrazni, že vstupem může být jak `int`, tak `float`, a f-string si s oběma poradí bez ručního přetypování.
- Na co se zaměřit: přesný formát výstupního textu (mezery, velikost písmen) – testy kontrolují přesné znění.
- Časté chyby studentů: použití `str(cislo)` a ruční spojování řetězců pomocí `+` místo f-stringu (funguje to, ale je dobré je nasměrovat k f-stringu, který si právě probrali); překlep ve statické části textu.
- Tip: ukaž na tabuli rozdíl mezi `"Hodnota je " + cislo` (chyba, TypeError) a f-stringem – dobře to ilustruje, proč je f-string praktický.

## Cvičení

Doplň funkce v souborech ve složce `cviceni/`:

- **`ukol_1.py` - `pozdrav(jmeno)`**: Vrať pozdrav ve tvaru `"Ahoj, <jmeno>!"`.
  - Příklad: `pozdrav("Petra")` -> `"Ahoj, Petra!"`
  - Pokud `jmeno` není `str`, vyhoď `TypeError` s výstižnou zprávou.
- **`ukol_2.py` - `secti(a, b)`**: Vrať součet dvou čísel `a` a `b`.
  - Příklad: `secti(2, 3)` -> `5`
  - Pokud `a` nebo `b` není `int`/`float`, vyhoď `TypeError` s výstižnou zprávou.
- **`ukol_3.py` - `preved_na_text(cislo)`**: Vrať řetězec ve tvaru `"Hodnota je <cislo>"` pomocí f-stringu.
  - Příklad: `preved_na_text(5)` -> `"Hodnota je 5"`
  - Pokud `cislo` není `int`/`float`, vyhoď `TypeError` s výstižnou zprávou.

## Jak si to sám zkontrolovat
```bash
pip install -r requirements.txt
pytest cviceni -v
```
Po nahrání na GitHub navíc automaticky poběží testy přes GitHub Actions – uvidíš zelenou/červenou fajfku u commitu.

## Hodnocení

Po nahrání do GitHub Classroom se úkoly hodnotí automaticky:

- **Základní testy** (`test_ukol_1.py`, `test_ukol_2.py`, `test_ukol_3.py`) se spouští ihned po každém pushi a výsledek uvidíš během pár minut přímo u commitu / v záložce Actions.
- Na **jedničku** je navíc potřeba projít přísnějšími **stress testy** – ty pomocí knihovny [Hypothesis](https://hypothesis.readthedocs.io/) generují tisíce náhodných a hraničních vstupů (včetně neplatných typů) a ověřují, že funkce fungují správně ve všech případech, ne jen na pár ukázkových vstupech. Tyto testy se zpřístupní až poté, co vyučující zveřejní oficiální řešení (branch `reseni`) – do té doby nejsou součástí hodnocení.

## Odevzdání
Vyplň soubory v `cviceni/`, commitni a pushni do svého repozitáře do stanoveného termínu. Řešení (branch `reseni`) zveřejní vyučující až po deadline.
