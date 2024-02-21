# ---------#1---------
import random
from string import punctuation, digits

lause = input("Sisesta oma sõna või lause: ").lower()
v = k = m = t = n = 0
vokaali = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
konsonanti = ["b", "p", "d", "t", "g", "k", "s", "h", "f", "š", "z", "ž"]
markid = punctuation
numberid = digits

lause_list = list(lause)
for sumbol in lause_list:
    if sumbol == vokaali:
        v += 1
    elif sumbol in konsonanti:
        k += 1
    elif sumbol in markid:
        m += 1
    elif sumbol in numberid:
        n += 1
    else:
        t += 1

print("Vokaali:", v)
print("Konsonanti:", k)
print("Kirjuvahemärgid:", m)
print("Tühikud:", t)
print("Numberid:", n)

# -----------#2 ----------

# Создаем пустой список для хранения имен
nimed = []
inimene_vanus = []

# Просим пользователя ввести пять имен
for i in range(5):
    while True:
        nimi = input("Palun, Sisesta nimi: ").capitalize()
        if nimi not in nimed:
            nimed.append(nimi)
            break
        else:
            print("Sisesta veel kord")





vimane = nimi

print("Loetelu:", nimed)

nimed.sort() # Сортируем имена в алфавитном порядке

print("Nimed tähestikulises järjekorras: ")
for nimi in range(len(nimed)):
    print(nimi + 1, ". ", nimed[nimi], sep="")


# Последнее добавленное имя
print("Viimati lisatud nimi:", vimane)

# Вывод возраст каждого человека

print("inimene vanus = ", inimene_vanus)


#   KESKMINE, MINIMUM, MAKSIMUM JA SUMMA

vanused = []
for i in range(5):
    vanus = int(input("Sisesta vanus: "))
    vanused.append(vanus)
maksimum = max(vanused)
minimum = min(vanused)
summa = sum(vanused)
keskmine = summa/len(vanused)
print("Maksimum vanus on", maksimum, "\nMinimum on", minimum, "\nSumma on", summa, "\nKeskmine on ", keskmine)

#   Выводим на экран и имя и возраст

for i in range(5):
    print(nimed[i], "on", vanused[i], "aastat vana")

# ------------- 3 -------------

from random import *

arvud = []

n = int(input("Mitu rida joonistame? "))
s = input("Sisestage, kui sümbol: ")
# loendi taitmine
for p in range(n):
    arvud.append(randint(1, 100))
# diagrammi loomine
for p in range(n):
    print(arvud[p]*s)


# ------------- 4 -------------

indeksid = ["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]


while True:
    while True:
        try:
            indeks = int(input("Sisesta oma indeks: "))
            indeks_elemendide_arv = len(str(indeks))
            if indeks_elemendide_arv == 5:
                print("5 numbriline indeks")
                break
            else:
                print("On vaja 5 numbriline arv(postiindeks)!")
        except:
            print("Vale andmetuup")
    arv1 = indeks//10000
    print(arv1)
    symbolid = list(str(indeks))
    sym1 = symbolid[0]
    print(sym1)
    if arv1 <= len(indeksid):
        print("Sa elad:", indeksid[arv1 - 1])
    else:
        print("Ei ole vastet sellele indeksile")


# ------------- 5 -------------

arvud = input("Sisesta numbrit (ruumiga eraldatud): ").split()
i, j = 0, len(arvud) - 1
while i < j:
    arvud[i], arvud[j] = arvud[j], arvud[i]
    i, j = i + 1, j - 1
print(arvud)

# ------------- 6 -------------

from random import *
from string import *

nimekirja1 = []
nimekirja = []
n = int(input("Nimekirja suurus: "))
for i in range(n):
    arv = randint(10, 100)
    nimekirja1.append(arv)
    nimekirja.append(arv)
maksimum = nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
vajavarv = maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i] = vajavarv
print(nimekirja1)
print(nimekirja)

numbers = []
numbers1 = int(input("Nimekirja suurus"))

if numbers1 == 0:
    print("Arv ei saa olla null")

numbers.append(numbers1)
# Находим самое большое число в списке
max_number = max(numbers)

# Делим самое большое число на длину списка
useless_number = max_number / len(str(numbers))

# Заменяем самое большое число в списке на "бесполезное" число
index_of_max = numbers.index(max_number)
numbers[index_of_max] = useless_number

print("Исходный список чисел:", numbers)


# ------------- 7 -------------

try:
    arvud = input("Sisestage arvud: ")


    sort_cba = sorted(arvud, reverse=True)
    print("Сортировка по убыванию абсолютных значений:", sort_cba)

    sort_abc = sorted(arvud)
    print("Сортировка по возрастанию абсолютных значений:", sort_abc)
except:
    print("ValueError")

# ------------- 8 -------------



# ------------- 9 -------------

import string

while True:
    inimene_nimi = input("Sisesta oma nimi: ").capitalize()
    if inimene_nimi.isalpha():
        break
    else:
        print("Nimi peab sisaldama ainult tähti!")

print("Tere, {}!".format(inimene_nimi.capitalize()))

nimi_length = len(inimene_nimi)
vowels = sum(1 for letter in inimene_nimi if letter.lower() in 'b, p, d, t, g, k, s, h, f, š, z, ž')
consonants = nimi_length - vowels

print("Tähtede arv nimes:", nimi_length)
print("Täishäälikute arv:", vowels)
print("Konsonantide arv:", consonants)

unique_letters = sorted(set(inimene_nimi.lower()))
print("Nimetage tähed tähestiku järjekorras:", ", ".join(unique_letters))



# -------------- 13 --------------
import random


sõnad = ["Arvuti", "Buss", "Raamat", "Kodu", "Kass", "Koer", "Leht", "Maailm"]

sõna = random.choice(sõnad).lower()


arvamatu_kiri = []
arvatud_kiri = []
katsed = 0

display = "_" * len(sõna)

while True:
    print("Arvatud sõna:", display)
    print("Arvamatu kiri", arvamatu_kiri,)
    kiri = input("Sisesta kiri: ").lower()
    if kiri in sõna:
        arvatud_kiri.append(kiri)
        display = ''.join([char if char in arvamatu_kiri else '_' for char in sõna])
        if '_' not in display:
            print("Palju õnne! Sa arvasid sõna: ", sõna)
            print("Katsete arv: ", katsed)
            break
        else:
            arvamatu_kiri.append(kiri)


        katsed += 1




# -------------- 18 ------------

import random

choices = ["kivi", "käärid", "paber"]

while True:
    try:
        player_choice = input("Valige kivi, käärid või paber (sisestage väljumiseks exit): ").lower()
        if player_choice == "exit":
            print("Head Aega!")
            break

        if player_choice not in choices:
            raise ValueError("Vigane sisestus. Valige kivi, käärid või paber.")

        computer_choice = random.choice(choices)

        print("Arvuti on valitud:", computer_choice)

        if player_choice == computer_choice:
            print("Viit!")
        elif player_choice.index(player_choice) > computer_choice.index(computer_choice) or \
            player_choice.index(player_choice) > computer_choice.index(computer_choice) or \
            player_choice.index(player_choice) > computer_choice.index(computer_choice):
            print("Sina võitsid!")
        else:
            print("Sa kaotasid.")

    except ValueError as ve:
        print(ve)

#
# (player_choice == "kivi" and computer_choice == "käärid") or \
#                 (player_choice == "käärid" and computer_choice == "paber") or \
#                 (player_choice == "paber" and computer_choice == "kivi"):





# BlackJack
import random

# # Создание колоды карт
suits = ['Ussid', 'Teemandid', 'Klubid', 'Tipud']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Daam', 'Kuningas', 'Äss']
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# # Перемешивание колоды
random.shuffle(deck)

# # Начальные карты для дилера и игрока
dealer_hand = [deck.pop(), deck.pop()]
player_hand = [deck.pop(), deck.pop()]

# # Показываем карты
print("Edasimüüja kaardid:")
print(f"{dealer_hand[0]['rank']} {dealer_hand[0]['suit']}")
print("Üks kaart peidetud")
print()
print("Teie kaardid:")
print(f"{player_hand[0]['rank']} {player_hand[0]['suit']}")
print(f"{player_hand[1]['rank']} {player_hand[1]['suit']}")
print()

# # Игрок
player_score = sum([10 if card['rank'] in ['Jack', 'Daam', 'Kuningas'] else 11 if card['rank'] == 'Äss' else int(card['rank']) for card in player_hand])

while player_score < 21:
    action = input("Kas soovite võtta teise kaardi? (jah/ei): ").lower()
    if action == 'jah':
        new_card = deck.pop()
        player_hand.append(new_card)
        print("Sa võtsid kaardi:", new_card['rank'], new_card['suit'])
        player_score += 10 if new_card['rank'] in ['Jack', 'Daam', 'Kuningas'] else 11 if new_card['rank'] == 'Äss' else int(new_card['rank'])
        print("Teie punktide summa:", player_score)
        print()
    else:
        break


dealer_score = sum([10 if card['rank'] in ['Jack', 'Daam', 'Kuningas'] else 11 if card['rank'] == 'Äss' else int(card['rank']) for card in dealer_hand])

while dealer_score < 17:
    new_card = deck.pop()
    dealer_hand.append(new_card)
    dealer_score += 10 if new_card['rank'] in ['Jack', 'Daam', 'Kuningas'] else 11 if new_card['rank'] == 'Äss' else int(new_card['rank'])

# # Вывод результатов
print("Edasimüüja kaardid:")
for card in dealer_hand:
    print(f"{card['rank']} {card['suit']}")
print("Edasimüüja punktid kokku:", dealer_score)
print()
print("Teie kaardid:")
for card in player_hand:
    print(f"{card['rank']} {card['suit']}")
print("Сумма ваших очков:", player_score)

# # Проверка результатов
if player_score > 21:
    print("Sa kaotasid, kui läksid üle parda.")
elif dealer_score > 21:
    print("Edasimüüja kaotas üle minnes.")
elif player_score > dealer_score:
    print("Sina võitsid!")
elif player_score < dealer_score:
    print("Sa kaotasid!")
else:
    print("Viit!")




# ------------- sleep + tqdm --------------
from time import sleep
from os import replace
cl = 0

for i in range(50):
    sym = i*"-"
    cl += 1
    print(replace(sym, ))
    sleep(0.6)

print()

import time
from tqdm import tqdm

mylist = [1,2,3,4,5,6,7,8]

for i in tqdm(mylist):
    time.sleep(1)





