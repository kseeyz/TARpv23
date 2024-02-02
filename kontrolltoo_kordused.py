from random import *
import random

while True:
    try:
        K = int(input("Mitu kotleti sul on?: "))
        if K > 0:
            break
    except ValueError:
        print("Vale tuup")
while True:
    try:
        M = int(input("Mitu kotleti uhel pannil?: "))
        if M > 0:
            break
    except ValueError:
        print("Vale tuup")
pann = 0
while K > 0:
    K -= M
    pann += 1
    print(f'praetud: {pann} tk')
    if K<M:
        pann += 1
        print(f'praetud: {pann} tk')
print(f'Kokku oli praetid: {pann} pannid')
print()


            #1

# while True:
#     try:
#         n = int(input("Sisestage jäneste arv (1 kuni 9):"))
#         if 1 <= n <= 9:
#             break
#    except:
#         print("Valju tuup")
#
#
# for i in range(n):
#     print(' /V\ '.center(10, ' '), end = "")
# print()
# for i in range(n):
#     print(" (o o) ".center(10, ' '), end = "")
# print()
#
# for i in range(n):
#     print("   / | \\" if i < n - 1 else "   / | ")



            #2

L = int(input("Sisestage L väärtus: "))
sum_tulemus = 0
kalkulaator = " "
for i in range(L + 1):
    try:
        sum_tulemus += 1
        kalkulaator += f'{i} + '

        kalkulaator = kalkulaator[:-2]
        result_taisarv = f"{kalkulaator}= {sum_tulemus}"
        print(result_taisarv)
    except:
        print("Sisestage oma arv, palun")


            #3


salajane_number = random.randint(0, 100)
katsete_piirang = 10

print("Arva ära arv vahemikus 0 kuni 100. Sul on 10 katset.")

for katsete in range(1, katsete_piirang + 1):

    kasutaja_arvamine = int(input(f"Katse {katsete}: sisestage oma valik: "))

    if kasutaja_arvamine == salajane_number:
        print(f"Palju õnne! Arvasite arvu {salajane_number} pärast {katsete} katset ära.")
        break
    elif kasutaja_arvamine < salajane_number:
        print("Rohkem. Proovi uuesti.")
    else:
        print("Vähem. Proovi uuesti.")
else:
    print(f"Olete kõik katsed ammendanud. Peidetud number oli {salajane_number}")



            #4

try:
    arv1 = int(input("Sisestage täisarv: "))
    arv2 = arv1[::-1]
    print('"Pööratut arv:', arv2)
except:
    print("Kirjutage täisarv")


a = int(input("Sisestage täisarv: "))
b = 0
while a > 0:
    try:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
        print("*Ümberpööratud* number", str(b))
    except TypeError:
        print("Vale tuup")
            #5


arv = int(input('Sisestage arv: '))
sum = 0
arvu_korrutis = 1

while arv > 0:
    try:
        sum += arv % 10
        arvu_korrutis *= arv % 10
        arv = arv//10


        print(f'Sum =')
        print("Summa:", sum)
        print("Korrutis:", arvu_korrutis)
    except:
        print("Vaja numbrit")



