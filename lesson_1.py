print("Tere maailm!")

                            #1
# name = input("What's your name?: ")    #input name
# age = int(input("How old are you?: "))  # input age
# print("Hello, "+name+". You are"+str(age)+" years old")
# print("Hello!",name,". You are", age,"years old")
# print("Hello, {0}!\n You are {1} years old".format(name, age))

#print(type(age))
                        #2
# vanus = 18
# nimi = "Jaak"
# pikkus = 16.5
# kas_kaib_koolis = True
#
# print(f"Vanuse tuup: {type(vanus)}")
# print(f"Nimi tuup: {type(nimi)}")
# print(f"Pikkus tuup {type(pikkus)}")
# print(f"Kas kaib koolis tuup {type(kas_kaib_koolis)}")


                        #3

# import random
# from random import *
# kokku = randint(10, 100)
# print("Kokku: ", kokku)
# mitu = int(input("Mitu kommi tahad votta: "))
# kokku -= mitu
# print("Nuud laua peal on", kokku, "kommid: ")

        # №4

# import math
# dlina_okruzhnosti = float(input("Введите длину окружности дерева (в сантиметрах): "))
# diametr_dereva = dlina_okruzhnosti / math.pi
# print(f"Диаметр дерева: {diametr_dereva:.2f} см")

        # №6
# try:
#     aeg = float(input("Mitu tundi kulus sõiduks? "))
#     teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#     kiirus = teepikkus / aeg
#     print("Sinu kiirus oli " + str(kiirus) + " km/h")
# except:
#     print("Viga andmetuubiga")


        # №5

# import math
# N = float(input("Sisestage ristkülikukujulise maatüki pikkus (meetrites): "))
# M = float(input("Sisestage ristkülikukujulise maatüki laius (meetrites): "))
#
# diagonaal = math.sqrt(N**2 + M**2)
#
# print(f"Ristkülikukujulise maatüki diagonaal on {diagonaal:.2f} meetrit.")


        # №7




        # №8

# print("  @..@\n"
#       " (----)\n"
#       "( \__/ )\n"
#       " ^^ "" ^^")

        # №9

# a = int(input("Sisesta esimese külje pikkus: "))
# b = int(input("Sisesta teise külje pikkus: "))
# c = int(input("Sisesta kolmanda külje pikkus: "))
#
# umbermoot = a + b + c
# print(f"Kolmnurga ümbermõõt on: {umbermoot}")

        # №10

# def arvuta_maksumus(pitsa_hind, jootraha_protsent):
#     jootraha = pitsa_hind * (jootraha_protsent / 100)
#     igaühe_maksumus = (pitsa_hind + jootraha) / 2
#     return igaühe_maksumus
#
# pitsa_hind = 12.90
# jootraha_protsent = 10
#
# maksumus = arvuta_maksumus(pitsa_hind, jootraha_protsent)
# print(f"Igaüks peab maksma {maksumus:.2f} eurot.")

        #№10_2

# from random import *
#
# P = randint(1, 5)
# hind = 12.90
#
# hind *= 1.1
# osa = round(hind / P, 2)
# print("Iga sober maksab: ", osa)

