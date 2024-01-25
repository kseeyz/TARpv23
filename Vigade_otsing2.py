print("*** NUMBRIDEGA MÄNGUD ***")
print()
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) # надо было добавить две скобки в конце
        break
    except ValueError:
        print("See ei ole täisarv")
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga pole mõtet midagi ette võtta")
else:
    # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c = b = a # if убираем и убираем двойной знак ==
    paaris = 0 # только один знак =
    paaritu = 0 # только один знак =  так же
    while b > 0:
        if b % 2 == 0:
            paaris += 1 # не =+, а +=
        else:
            paaritu += 1 # не =+, а +=
        b = b // 10

print("Paarisarvud:", str(paaris))
print("Paaritud arvud:", str(paaritu))
print()
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*Tagurda* sisestatud number")
print()
b = 0
while a > 0:
    number = a % 10
    a = a // 10
    b = b * 10
    b += number # пишется не =+, а +=
print("*Ümberpööratud* number", str(b))
print()
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Siracuse hüpoteesi testimine") # была добавлена лишняя скобка
print()
if c % 2 == 0: #   if c % 2 = 0: Два знака ==
    print("c - paarisarv. Jagage 2-ga.")
else:
    print("c - paaritu arv. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
        if c % 2 == 0:
            c = c // 2 # c == c / 2 делиться всегда //
        else:
            c = (3 * c + 1) // 2 # c == c / 2 делиться всегда //
    print(str(c), end=' ') # print(c, end= ") не добавлена "
    print()
    print("Hüpotees on õige")