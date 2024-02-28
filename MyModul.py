import math

def summa(arv1: int, arv2: int, arv3: int)->int:
    """ Funktsioon tagastab kolme arvu summa
        summa(arv1, arv2, arv3)

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Arv3 sisestab kasutaja
    :rtype: int
    """
    s = arv1 + arv2 + arv3
    return s


def TuubiKontroll() -> any:
    """ Funktsioon tagastab sissestatud õiges formaadis
        IntKontroll()

    :rtupe: any
    """

    x = input("Sisestage andmed: ")
    try:
        t = int(x)
        return x
    except:
        try:
            return float(x)
        except:
            return str(x)



# --------------- 2 --------------
def is_year_leap(year: int) -> bool:
    """ Funktsioon otsustab kas aasta on liiga voi ei ole
    Tagastab True on aasta on liigaasta ja False kui aasta on tavaline

    :param int year: Aasta sisestab kasutaja
    :rtype: bool
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# --------------- 1 --------------
def arithmetic(a: int, b: int, op: int) -> any:
    """ Funktsioon tagastab Lihtsamad aritmeetilised tehted

    :param a:
    :param b:
    :param op:
    :rtype: any
    """


    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Jagamine nulliga pole lubatud"
    else:
        return "Tundmatu operaator"

a = float(input("Sisestage esimene number: "))
b = float(input("Sisestage teine number: "))
op = input("Sisestage operaator (+, -, *, /): ")


# ------------ 3 ----------

def square(kulg: float) -> any:
    """ Funktsioon ruudu küljel ja tagastab 3 väärtust: ruudu ümbermõõt, ruudu pindala ja ruudu diagonaal.

    :param float kulg:
    :rtype: any
    """
    S = kulg**2
    P = 4*kulg
    d = kulg * math.sqrt(2)
    return S, P, d




# ------------ 4 -----------

def season(month:int) -> str:
    """ Funktsioon tagastab hooaja, millesse see kuu kuulub (talv, kevad, suvi või sügis)

    :param int month:
    :rtype: str
    """
    if month in [12, 1, 2]:
        return 'Talv'
    if month in [3, 4, 5]:
        return 'Kevad'
    if month in [6, 7, 8]:
        return 'Suvi'
    if month in [9, 10, 11]:
        return 'Sügis'
    else:
        return 'Tundmatu kuu number'

# ------------ 5 -----------

def bank(a: float, years:int) -> float:
    """ Funktsioon

    :param float a:
    :param int years:
    :rtype: float
    """

    protsenti_aastas = 0.1 # 10% годовых
    A = a * (1 + protsenti_aastas) ** years
    return A





# ------------ 6 -----------

def is_prime(number: int) -> bool:
    """ Funktsioon tagastab arv vahemikus 0 kuni 1000 ja tagastab tõene,
        kui see on algväärtus, ja Väär muul juhul

    :param int number:
    :rtype: bool
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# ------------ 7 -------------

def date(day: int, month: int, year: int) -> bool:
    """ Funktsioon tagastab True, kui selline kuupäev on meie kalendris, ja False muul juhul

    :param int day:
    :param int month:
    :param int year:
    :rtype: bool
    """
    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28



# -------------- PALGAD PRAKTILINE TOO -----------------
from praktiline_too_palgad import *

def lisa_inimene_ja_palgad(nimi: str, palga: int) -> str:
    for nimi in range(len(inimesed)):
        print(nimi + 1, ". ", inimesed[nimi], sep = "")

    for palga in range(len(palgad)):
        print(palga + 1, ". ", palgad[palga], sep = "")



