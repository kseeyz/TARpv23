import math
from math import *



print("Ruudu karakteristikud")
a = input("Sisesta ruudu külje pikkus => ")
S = float(a) ** 2
print("Ruudu pindala", round(S, 2))
P = 4 * float(a)
print("Ruudu ümbermõõt", round(P, 2))
di = float(a) * math.sqrt(2)
print("Ruudu diagonaal ", round(di, 2))

print()

print("Ristküliku karakteristikud")
b = input("Sisesta ristküliku 1. külje pikkus => ")
c = input("Sisesta ristküliku 2. külje pikkus => ")
S = float(b) * float(c)
print("Ristküliku pindala", round(S, 2))
P = 2*(float(b)+float(c))
print("Ristküliku ümbermõõt", round(P, 2))
di = math.sqrt(float(b)**2+float(c)**2)
print("Ristküliku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
r = input("Sisesta ringi raadiusi pikkus => ")
d = 2 * float(r)
print("Ringi läbimõõt", round(d, 2))
S = math.pi * float(r) ** 2
print("Ringi pindala", round(S, 2))
C = 2 * math.pi * float(r)
print("Ringjoone pikkus", round(C, 2))

