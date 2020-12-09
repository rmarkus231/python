#Python töö 1 ja 2
#richard markus tins it20
#30:11.20
import random

#õunad
poisid=int(input("Mitu pöialpoissi õunu tahtis (0-7)? "))
oun=14
while poisid > 0:
    ran=random.randint(1,2)
    print(ran)
    oun=oun-ran
    poisid=poisid-1

print(f"Lumivalgekesele jäi õunu {oun}")
input()
#male
h=int(input("ruudu arv: "))
print(f"Nisuteri {h}. ruudu eest: {pow(2,h-1)}")

input()
#täringud
t=int(input("mitu täringut soovite veeretada? "))
while t >0:
    print(random.randint(1,6))
    t=t-1

input()
#murelikkud lapsevanemad
ring=int(float(input("Ringide arv: ")))
porgand=0
if ring % 2 == 0:
    ring=ring
else:
    ring=ring-1

while ring > 0:
    porgand=porgand+ring
    ring=ring-2

print(f"Porgandite koguarv on {porgand}.")

input()
#tervitus
print("Tere,maailm!")

input()
#Aasta liblikas
aasta=2020
liblikas="teelehe-mosaiikliblikas"
lause_keskosa=". aasta liblikas on"
lause=f"{aasta}{lause_keskosa}{liblikas}"
print(lause)

input()
#pilved
pilv=7
pilv=float(input("Kui kõrgel on pilv (km): "))

if pilv > 6:
    print("Need on ülemise kihi pilved")
else:
    print("Need ei ole ülemise kihi pilved")
    
input()
#bussid
inimesed=int(input("Reisijaid on: "))
kohti=int(input("Kohti on bussis: "))
busse=inimesed//kohti
viimases=inimesed%kohti
if kohti >= inimesed:
    print("Vaja on 1 buss")
    print(f"Viimases bussis inimesi: {inimesed}")
else:
    print(f"Busse vaja: {busse}")
    print(f"Viimases bussis inimesi: {viimases}")

input()
#äratus
n=int(input("Mitu korda tahate äratust? "))
while n > 0:
    print("Tõuse ja sära!")
    n=n-1
    
input()

    