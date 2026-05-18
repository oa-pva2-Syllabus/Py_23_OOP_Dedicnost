# PVA2 - Programování a vývoj aplikací
## Lekce 23: OOP - Dědičnost

## Obsah

### 1 Streaming

Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů – filmy a seriály.

Vytvoř třídy `Porad`, `Film` a `Serial` dle níže uvedené specifikace.

**Třída `Porad`**
- Konstruktor: `__init__(self, nazev, zanr)`
- Atributy `nazev` a `zanr` jsou soukromé.
- Metoda `get_info()` vrátí řetězec:
  ```
  Název: Inception, Žánr: Sci-fi
  ```

**Třída `Film`** — potomek třídy `Porad`
- Konstruktor: `__init__(self, nazev, zanr, delka, rok_vydani)` — `delka` je v minutách
- Metoda `get_info()` vrátí řetězec:
  ```
  Název: Inception, Žánr: Sci-fi, Délka: 148 min, Rok vydání: 2010
  ```
- Metoda `celkova_delka()` vrátí celkovou délku filmu v minutách jako `int`.

**Třída `Serial`** — potomek třídy `Porad`
- Konstruktor: `__init__(self, nazev, zanr, pocet_epizod, delka_epizody)` — `delka_epizody` je v minutách
- Metoda `get_info()` vrátí řetězec:
  ```
  Název: Breaking Bad, Žánr: Drama, Počet epizod: 62, Délka epizody: 47 min
  ```
- Metoda `celkova_delka()` vrátí celkovou délku seriálu v minutách jako `int`.

Po naprogramování vytvoř alespoň jeden objekt `Film` a jeden objekt `Serial`, zavolej `get_info()` a ověř správnost výstupů.

---

### 2 Zhlédnutí

**Třída `Uzivatel`**
- Konstruktor: `__init__(self, uzivatelske_jmeno)`
- Celková délka sledování začíná na `0`.
- Metoda `pridej_zhlednuti(delka)` připočítá délku (v minutách) k celkové délce sledování.
- Metoda `get_sledovani()` vrátí celkovou délku sledování jako naformátovaný řetězec:

  | Délka sledování | Výstup |
  |---|---|
  | ≥ 1 den | `"2 dní, 3 hodin, 15 minut"` |
  | ≥ 1 hodina, < 1 den | `"3 hodin, 15 minut"` |
  | < 1 hodina | `"45 minut"` |

  Je-li počet minut nebo hodin nula, zobrazí se nula, např. `"3 hodin, 0 minut"`.

Vytvoř uživatele a simuluj zhlédnutí filmu a seriálu z předchozí části. Výsledek zobraz pomocí `get_sledovani()`.
