import random
from random import *
import math

# print("tund on alanud")
# hilinemine = input("Kas õpilane on hilinenud?: ") #jah - a.lower(), JAH - a.upper(), Jah - a.capitalize(), jAH
# if hilinemine.upper() == "JAH":
#     print("Õpilane ootab 30 min")
# print("Õpilane astub klassi")



# arv = randint(0, 1000) # Juhuslik täisarv vahemikust 0-1000
# if arv %2 == 0:
#     print(arv, "on paaris arv")
# else:
#     print(arv, "on paaritu arv")
# print()



# protsent = randint(-100, 500) #0-100, 0-60 - "2", 61-75-"3", 76-89-"4", 90-100-"5"
# print(protsent,"% on testi tulemus")
# if protsent<0 or protsent>100:
#     tulemus = "valed andmed"
# elif 0<protsent<60:
#     tulemus = "hinne 2"
# elif 61<=protsent<75:
#     tulemus = "hinne 3"
# elif 75<=protsent<90:
#     tulemus = "hinne 4"
# else:
#     tulemus = "hinne 5"
# print(tulemus)



            #1
# nimi = input("Mis on sinu nimi: ").capitalize()
# print("Tere, ", nimi)
# if nimi == "Juku":
#     print("Lahe kinno")
# else:
#     print("Ei lahe kinno")
#
#
# juku_vanus = randint(0, 100)
# print("Juku on", juku_vanus)
# if juku_vanus<0 or juku_vanus>100:
#     print("Vale vanus")
# if juku_vanus<6:
#     print("Tasuta pilet Jukule")
# elif juku_vanus<=14:
#     print("Lastepilet Jukule")
# elif juku_vanus<=65:
#     print("Täispilet Jukule")
# elif juku_vanus<=100:
#     print("Sooduspilet Jukule")
# else:
#     print("Viga andmetega")


            #2

# import random
# nimed = choice(["Kirill", "Bogdan", "Vsevolod", "Gleb", "Martin", "Lev", "Sasha", "Elena", "Eva", "Mike"])
# valitud_nimed = random.sample(nimed, len(nimed))
#
#
#
# print(f"Täna sinu pinginaaber on {nimed}!")

            #2.1


    # def genereeri_nimed():
    #     nimed = ["Kirill", "Bogdan", "Vsevolod", "Gleb", "Martin", "Lev", "Sasha", "Elena", "Eva", "Mike"]
    #     valitud_nimed = random.sample(nimed, 2)
    #     return valitud_nimed
    #
    # pinginaabrid = genereeri_nimed()
    # nimed = f"{pinginaabrid[0]} ja {pinginaabrid[1]}"
    #
    # print(f"Täna on pinginaabriteks {nimed}!")



            #3
# arv1 = int(input("Введите первую длину стены комнаты (в сантиметрах): "))
# arv2 = int(input("Введите вторую длину стены комнаты (в сантиметрах): "))
#
# S = arv1 * arv2
# P = 2*(arv1 + arv2)
# print("Периметр комнаты =", round(S, 2),"\nА площадь комнаты =", round(P, 2))
#
# remont = input("Хотите сделать ремонт? ")
# if remont.capitalize() == "Да":
#     print(input("Тогда сколько стоит квадратный метр замены пола? "))



            #4

# alghind = randint(0, 1000)
# print(alghind)
# if alghind >= 700:
#     soodus_protsentides = 30
#     allahindlus = (soodus_protsentides/ 100) * 30
#     uus_hind = alghind - allahindlus
#     print(f"Uus hind pärast 30% allahindlust on: {uus_hind}", )
# else:
#     print("Tootesoodustus algab 700€-st, seega 30% allahindlust ei saa")


            #4.1

    # def arvuta_allahindlus(alghind):
    #     if alghind >= 700:
    #         soodustus_protsentides = 30
    #         allahindlus = (soodustus_protsentides / 100) * alghind
    #         uus_hind = alghind - allahindlus
    #         print(f"Uus hind pärast 30% allahindlust on: {uus_hind}")
    #     else:
    #         print("Tootesoodustus algab 700€-st, seega 30% allahindlust ei saa")
    #
    #
    # alghind = float(input("Sisestage alghind: "))
    # uus_hind = arvuta_allahindlus(alghind)

            #5

# temperatuur = randint(1, 20)
# print(temperatuur)
# if temperatuur >= 18:
#     print("Temperatuur on üle 18 kraadi, mis on soovitav toasoojus talvel.")
# else:
#     print("Temperatuur on 18 kraadi või madalam, soovitav on hoida soojem temperatuur talvel.")


            #5.2

    # def kontrolli_temperatuuri(temperatuur):
    #     if temperatuur >= 18:
    #         print("Temperatuur on üle 18 kraadi, mis on soovitav toasoojus talvel.")
    #     else:
    #         print("Temperatuur on 18 kraadi või madalam, soovitav on hoida soojem temperatuur talvel.")
    #
    # temperatuur = float(input("Mis temperatuur täna väljas on?: "))
    # kontrolli_temperatuuri(temperatuur)



            #6


# pikkus= int(input("Mis on sinu pikkus?: "))
# print("Sa oled", pikkus)
# if 150 <= pikkus < 168:
#     pikkasvu = "lühike"
# elif 169 <= pikkus < 177:
#     pikkavu = "keskmine"
# else:
#     pikkasvu = "pikk"
# print(f'Sa oled {pikkasvu}')

            #7

# pikkus = randint(140, 210)
# print(pikkus)
# sugu = choice(['mees', 'näine'])
# print(sugu)
# if sugu.lower() == 'mees':
#     if pikkus < 165:
#         print("Sa oled lühike mees.")
#     elif 165 <= pikkus < 180:
#         print("Sa oled keskmise pikkusega mees.")
#     else:
#         print("Sa oled pikk mees.")
# elif sugu.lower() == 'naine':
#     if pikkus < 155:
#         print("Sa oled lühike naine.")
#     elif 155 <= pikkus < 170:
#         print("Sa oled keskmise pikkusega naine.")
#     else:
#         print("Sa oled pikk naine.")
# else:
#     print("Palun sisestage kehtiv sugu.")

            #7.2

    # def pikkus_ja_sugu(pikkus, sugu):
    #     if sugu.lower() == 'mees':
    #         if pikkus < 165:
    #             print("Sa oled lühike mees.")
    #         elif 165 <= pikkus < 180:
    #             print("Sa oled keskmise pikkusega mees.")
    #         else:
    #             print("Sa oled pikk mees.")
    #     elif sugu.lower() == 'naine':
    #         if pikkus < 155:
    #             print("Sa oled lühike naine.")
    #         elif 155 <= pikkus < 170:
    #             print("Sa oled keskmise pikkusega naine.")
    #         else:
    #             print("Sa oled pikk naine.")
    #     else:
    #         print("Palun sisestage kehtiv sugu.")

    # pikkus = float(input("Mis on sinu pikkus? (cm): "))
    # sugu = input("Mis on sinu sugu? ('mees' või 'naine'): ")
    #print()
    # pikkus_ja_sugu(pikkus, sugu)


            #8        ????????????


# milk = input("Kas sa tahad piima osta?: ")
# milk_cost = 1.65
# bread_cost = 2
# apples_cost = 3.45
# if milk.capitalize() == "Jah":
#     milk_int = int(input("kui palju sa tahad?: "))              #milk
#     milk1 = milk_cost * milk_int
#     print(f"See läheb maksma {milk1}")
# elif milk.capitalize() == "Ei":
#     bread = input("Kas sa tahad leiba osta?: ")
#     if bread.capitalize() == "Jah":
#         bread_int = int(input("Kui palju sa tahad osta?: "))    #bread
#         bread1 = bread_cost * bread_int
#         print(f"See läheb maksma {bread1}")
#     elif bread.capitalize() == "Ei":
#         apples = input("Kas sa tahad õuna osta?: ")             #apples
#         apples_int = int(input("Kui palju sa tahad osta?: "))
#         apples1 = apples_cost * apples_int
#         print(f"See läheb maksma {apples1}")
#
# total_amount = apples1 + bread1 + milk1
#
# all = input("Kas see on kõik? ")
# if all.capitalize() == "Jah":
#     print(f"Sinult {total_amount}€")







            #9


# kylg1 = int(input("Sisestage kujundi esimene külg (cm): "))
# kylg2 = int(input("sisestage kujundi teine külg (cm): "))
# if kylg1 == kylg2:
#     print("See on ruut!")
# else:
#     print("See ei ole ruut")





            #10

# print("Подсказка:")
# print("+  сложение")
# print("—  вычитание")
# print("*  умножение")
# print("/  деление")
# print("%  остаток от деления")
# print("** возведение в степень")
# print("// целочисленное деление")
# what = input('Что делаем? (+, -, *, /, **, %, //): ')
#
# #   +   добавление
# #   —   вычитание
# #   *   умножение
# #   /   деление
# #   %   остаток от деления
# #   **  возведение в степень
# #   //  целочисленное деление
#
# a = float(input('Введи первое число: '))
# b = float(input('Введи второе число: '))
#
# if what == '+':
#     c = a + b
#     print('Результат: ' + str(c))
# elif what == '-':
#     c = a - b
#     print('Результат: ' + str(c))
# elif what == '*':
#     c = a * b
#     print('Результат: ' + str(c))
# elif what == '%':
#     c = a % b
#     print('Результат: ' + str(c))
# elif what == '/':
#     c = a / b
#     print('Результат: ' + str(c))
# elif what == '**':
#     c = a ** b
#     print('Результат: ' + str(c))
# elif what == '//':
#     c = a // b
#     print('Результат: ' + str(c))
# else:
#     print('Я не знаю такой команды')
#
# input()


            #11

# import datetime
#
# birthday = input("Sisestage oma sünnipäev (YYYY-MM-DD): ")
#
# birthday = datetime.datetime.strptime(birthday, "%Y.%m.%d")
# current_date = datetime.datetime.now()
# age = current_date.year - birthday.year
#
# if age % 10 == 0:
#     print("teie sünnipäev on tähtpäev")
# else:
#     print("teie sünnipäev ei ole tähtpäev")



            #12


# def toote_allahindlus(alghind):
#     if alghind == 10:
#         soodustusprotsent = 10
#         allahindlus = (soodustusprotsent / 100) * alghind
#         uus_hind = alghind - allahindlus
#         print(f"Uus hind pärast 10% allahindlust on: {uus_hind}")
#     elif alghind > 10:
#         soodusprotsent2 = 20
#         allahindlus2 = (soodusprotsent2 / 100) * alghind
#         uus_hind2 = alghind - allahindlus2
#         print(f'Uus hind pärast 20% allahindlust on: {uus_hind2}')
#
# alghind = float(input("Sisestage alghind: "))
# uus_hind = toote_allahindlus(alghind)



            #13

# sugu = input("Mis on sinu sugu ('Mees' või 'Näine')?: ")
# if sugu.capitalize() == "Näine":
#     print("sa ei sobi meile!")
# elif sugu.capitalize() == "Mees":
#     vanus = int(input("Kui vana sa oled?: "))
#     if 16 <= vanus <= 18:
#         print("Sa sobid meile!")
#     else:
#         print("Sa ei sobi meile!")


            #14


# inimeste_arv = int(input("Sisestage, kui palju inimesi bussis sõida:"))
# print()
# bussi_maht = int(input("Valige siini helitugevus \n"
#                        "1) eriti väike (kuni 10 istekohta)\n"
#                        "2) väike (kuni 25)\n"
#                        "3) keskmine (40–50)\n"
#                        "4) suur (60-80)\n"
#                        "5) eriti suur mahutavus (100-120 istekohta): "))
# print()
# if inimeste_arv <= 10 and bussi_maht == 1:
#     print("Люди поместяться в автобус")
# else:
#     print("Люди не вместяться")
# if 11 < inimeste_arv <= 30 and bussi_maht == 2:
#     print("Люди поместяться")
# else:
#     print("Люди не поместяться")
# if 40 <= inimeste_arv <= 50 and bussi_maht == 3:
#     print("Люди поместяться в автобус")
# else:
#     print("Люди не вместяться")
# if 60 <= inimeste_arv <= 80 and bussi_maht == 4:
#     print("Люди поместяться")
# else:
#     print("Люди не вместяться")
# if 100 < inimeste_arv <= 120 and bussi_maht == 5:
#     print("Люди поместяться")
# else:
#     print("Люди не вместяться")

# inimeste_arv = int(input("Sisestage, kui palju inimesi bussis sõida:"))
# print()
# bussi_maht = int(input("Valige siini helitugevus \n"
#                        "1) eriti väike (kuni 10 istekohta)\n"
#                        "2) väike (kuni 25)\n"
#                        "3) keskmine (40–50)\n"
#                        "4) suur (60-80)\n"
#                        "5) eriti suur mahutavus (100-120 istekohta): "))
# print()
# if inimeste_arv <= 10 and bussi_maht == 1:
#     print("Люди поместяться в автобус 1")
#
# elif inimeste_arv <= 30 and bussi_maht == 2:
#     print("Люди поместяться 2")
#
# elif inimeste_arv <= 50 and bussi_maht == 3:
#     print("Люди поместяться в автобус 3")
#
# elif inimeste_arv <= 80 and bussi_maht == 4:
#     print("Люди поместяться 4")
#
# elif inimeste_arv <= 120 and bussi_maht == 5:
#     print("Люди поместяться 5")
# else:
#     print("Люди не вместяться")



