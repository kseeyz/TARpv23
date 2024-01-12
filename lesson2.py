import random
from random import *

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

# def arvuta_allahindlus(alghind):
#     if alghind >= 700:
#         soodustus_protsentides = 30
#         allahindlus = (soodustus_protsentides / 100) * alghind
#         uus_hind = alghind - allahindlus
#         print(f"Uus hind pärast 30% allahindlust on: {uus_hind}")
#     else:
#         print("Tootesoodustus algab 700€-st, seega 30% allahindlust ei saa")
#
# alghind = float(input("Sisestage alghind: "))
# uus_hind = arvuta_allahindlus(alghind)



            #5

# def kontrolli_temperatuuri(temperatuur):
#     if temperatuur >= 18:
#         print("Temperatuur on üle 18 kraadi, mis on soovitav toasoojus talvel.")
#     else:
#         print("Temperatuur on 18 kraadi või madalam, soovitav on hoida soojem temperatuur talvel.")
#
# temperatuur = float(input("Mis temperatuur täna väljas on?: "))
# kontrolli_temperatuuri(temperatuur)



            #6


pikkus = int(input("Mis on sinu pikkus?: "))
print("Sa oled", pikkus)
if pikkus < 150 >= 168:
    pikk = "lühike"
elif pikkus < 169 >= 177:
    pikk = "keskmine"
else:
    pikk = "pikk"
print()
print("Sa oled", pikk)



