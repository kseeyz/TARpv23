from MyModul import * #summa as s
# summa_3 = summa(int(input("Esimese arv: ")),int(input("Teise arv: ")),int(input("Kolmas arv: ")))
# summa_31 = summa(100,100, 0)



# print(summa_3)
# print(summa_31)



# while True:
#     x = TuubiKontroll()
#     print(type(x))


# ------------- 2 ------------
while True:
    try:
        year= int(input("Sisesta aasta number: "))
        break
    except:
        print('Viga')
a = is_year_leap(year)
print(a)
#___________ 2.1___________

print(is_year_leap(int(input("Sisesta aasta (Tõeline kõrgaasta, vale ei kõrgaasta): "))))

# -------------- 1 -----------

print(arithmetic(a, b, op))

# ------------ 3 -----------

while True:
    try:
        a = float(input("Sisesta külg: "))
        break
    except:
        print('viga')
S, P, d = square(a)
print(f'S = {S}, P = {P}, d = {d}')

# ------------ 4 -----------

month_number = int(input("Sisestage kuu number: "))
print(f"Kuu {month_number} vastab aastaajale: {season(month_number)}")

# ------------ 5 ----------

while True:
    try:
        esialgne_deposiit = float(input("Sisestage esialgne sissemakse summa: "))
        hoiuse_aastad = int(input("Sisestage aastate arv: "))
        break
    except:
        print('viga')

A = bank(esialgne_deposiit, hoiuse_aastad)
print(f"Konto summa läbi {esialgne_deposiit} aasta: {bank(esialgne_deposiit, hoiuse_aastad)} euro")

# ------------ 6 ----------

while True:
    try:
        a = int(input("Sisestage number: "))
        break
    except:
        print('viga')

number = is_prime(a)
print(a)


