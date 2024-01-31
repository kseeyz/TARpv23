#             #1
# try:
#     n = int(input("Sisestage jäneste arv (1 kuni 9):"))
#
#     if 1 <= n <= 9:
#         for i in range(n):
#             print("   (\\_/)")
#             print("   (o o)")
#             print("   / | \\" if i < n - 1 else "   / | ")
#             print()
# except:
#     print("Kirjutage arv vahemikus 1 kuni 9")


            #2
# try:
#     L = int(input("Sisestage L väärtus: "))
#     sum_tulemus = 0
#     kalkulaator = " "
#     for i in range(L + 1):
#         sum_tulemus += 1
#         kalkulaator += f'{i} + '
#
#     kalkulaator = kalkulaator[:-2]
#     result_täisarv = f"{kalkulaator}= {sum_tulemus}"
#     print(result_täisarv)
#
# except:
#             print("Sisestage oma arv, palun")


            #3

# import random
# try:
#     salajane_number = random.randint(0, 100)
#     katsete_piirang = 10
#
#     print("Arva ära arv vahemikus 0 kuni 100. Sul on 10 katset.")
#
#     for katsete in range(1, katsete_piirang + 1):
#         kasutaja_arvamine = int(input(f"Katse {katsete}: sisestage oma valik: "))
#
#         if kasutaja_arvamine == salajane_number:
#             print(f"Palju õnne! Arvasite arvu {salajane_number} pärast {katsete} katset ära.")
#             break
#         elif kasutaja_arvamine < salajane_number:
#             print("Rohkem. Proovi uuesti.")
#         else:
#             print("Vähem. Proovi uuesti.")
#     else:
#         print(f"Olete kõik katsed ammendanud. Peidetud number oli {salajane_number}")
# except:
#     print("Valeteade")

            #4

# try:
#     arv1 = int(input("Sisestage täisarv: "))
#     arv2 = arv1[::-1]
#     print('"Pööratut arv:', arv2)
# except:
#     print("Kirjutage täisarv")


# a = int(input("Sisestage täisarv: "))
# b = 0
# while a > 0:
#     number = a % 10
#     a = a // 10
#     b = b * 10
#     b += number
# print("*Ümberpööratud* number", str(b))

            #5

# try:
#     arv = int(input('Sisestage arv: '))
#     sum = 0
#     arvu_korrutis = 1
#     while arv > 0:
#         sum += arv % 10
#         arvu_korrutis *= arv % 10
#         arv = arv//10
#
#
#     print(f'Sum =')
#     print("Summa:", sum)
#     print("Korrutis:", arvu_korrutis)
# except:
#     print("Vaja numbrit")



