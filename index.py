print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis on sinu nimi?: ")
print(nimi.capitalize(), ", oi kui ilus nimi!!!")

index1 = int(input('kas leian Sinu keha indeksi? 0-ei, 1-jah => '))
if index1 == 1:
    try:
        pikkus = int(input("Mis on sinu pikkus?: "))
        if 0 < pikkus <= 210:
            mass = int(input("Kui palju sa kaalud?: "))
            if 30 < mass <= 160:
                index = mass / (0.01 * pikkus)**2
                print("Sinu keha indeks on:", round(index, 1))
                if index <= 16:
                    index2 = "tervisele ohtlik alakaal"
                    #print("Sinu keha indeks on tervisele ohtlik alakaal!")
                elif 17 <= index < 19:
                    index2 = "alakaal"
                    #print("Sinu keha indeks on Alakaal!")
                elif 19 <= index < 25:
                   index2 = "normaalkaal"
                    #print("Sinu keha indeks on normaalkaal!")
                elif 25 <= index < 30:
                    index2 = "ülekaal"
                    #print("Sinu keha indeks on Ülekaal!")
                elif 30 <= index < 35:
                    index2 = "rasvumine"
                    #print("Sinu keha indeks on rasvumine!")
                elif 35 <= index < 40:
                    #print("Sinu keha indeks on tugev rasvumine!")
                    index2 = "tugev rasvumine"
                elif index >= 41:
                    index2 = "Tervisele ohtlik rasvumine"

                print("Sinu keha indeks on", index2)
                    #print("Sinu keha indeks on Tervisele ohtlik rasvumine!")
    except:
        print(ValueError)



elif index1 == 0:
    print("Okey, head aega!")

print("Kohtumiseni, " + nimi.capitalize() + " Igavesti Sinu, Python!")
