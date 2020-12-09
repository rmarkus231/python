#Python harjutus 7, funktsioonid
#richard markus tins it20
#02:12.20
import math

#ruumalade leidmis programm
def kuup():
    a=input("Valisid kuubi. Sisesta kuubi külje pikkus: ")
    v=pow(float(a),3)
    v=f"Kuubi ruumala on: {round(v,2)}"
    return v

def kera():
    r=input("Valisid kera. Sisesta kera raadius: ")
    v=4/3*math.pi*pow(float(r),3)
    v=f"Kera ruumala on: {round(v,2)}"
    return v

def koonus():
    r,h=(input("Valisid koonuse. Sisesta koonuse raadius ja kõrgus (r,h): ")).split(",")
    v=1/3*(math.pi*pow(float(r),2))*float(h)
    v=f"Koonuse ruumala on: {round(v,2)}"
    return v

def silinder():
    r,h=(input("Valisid silindri. Sisesta silindri raadius ja kõrgus (r,h): ")).split(",")
    v=math.pi*pow(float(r),2)*float(h)
    v=f"Silindri ruumala on: {round(v,2)}"
    return v

loop=1
while loop==1:
    print("*"*10+"LEIAME RUUMALA"+"*"*10)
    print(f"1 Kuup\n2 Kera\n3 Koonus\n4 Silinder")
    valik=input("Soovitud kujundi number: ")
    if int(valik) ==1:
        print(kuup())
    if int(valik) ==2:
        print(kera())
    if int(valik) ==3:
        print(koonus())
    if int(valik) ==4:
        print(silinder())
    kordus=input("Kas soovite veel arvutada? jah/ei: ")
    if kordus == "jah":
        print("\n"*50)
        loop=1
    else:
        loop=0

input()
#tervitus
def tervita(keel='ger'):
    ge="ger"
    ee="est"
    en="ing"
    if keel == ge or keel == 0:
        nimi=input("Dein Name: ")
        return "Hallo "+nimi
    if keel == ee:
        nimi=input("Teie nimi: ")
        return "Tere "+nimi
    if keel == en:
        nimi=input("Your name: ")
        return "Hello "+nimi

print(tervita(ing))

input()