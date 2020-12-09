#Python töö 1 ja 2 ja 3
#richard markus tins it20
#30:11.20-8.12.20
import random
from datetime import date

#kuupäev
def kuu_nimi(a=1):
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","septempber","oktoober","november","detsember"]
    return kuud[a-1]

def kuupäev_sõnadega(a):
    paev,kuu,aasta=kuup.split(".")
    kuu=int(kuu)
    x=f"{paev}. {kuu_nimi(kuu)} {aasta}. a"
    return x

kuup=input("Sisesta kuupäev formaadis DD.MM.YYYY: ")
print(kuupäev_sõnadega(kuup))

input()
#mündid
def pronksikarva_summa(a):
    f=0
    for i in range(len(a)):
        if int(a[i]) < 10 :
            f=f+int(a[i])
    return f

m=input("fail (mündid.txt): ")
#m="mündid.txt"
fail = open(m , encoding="UTF-8")
faili_sisu = fail.readlines()

print(f"Hoiupõrsase läheb {pronksikarva_summa(faili_sisu)} senti")

input()
#tervitused mõtisklusega
def tervitus(a=0):
    a=a+1
    return a
k=int(input("Sisestage külaliste arv: "))
for a in range(k):
    print(f"Võõrustaja: \" Tere!\"\nTäna {tervitus(a)}. kord tervitada, mõtiskleb võõrustaja.\nKülaline: \"Tere, suur tänu kutse eest!\"")

input()
#peo eelarve
def eelarve(arv=0):
    arv=arv*10+55
    return arv
inim=int(input("Kutsutud inimeste arv: "))
kindel=int(input("Tulevate inimste arv: "))
print(f"Maksimaalne eelarve: {eelarve(inim)} eurot")
print(f"Minimaalne eelarve: {eelarve(kindel)} eurot")

input()
#õunamahla tegemine
def mahlapakkide_arv(ountekogus=0):
    a=round(ountekogus * 0.4/3,0)
    return a
arv=int(input("õunte kogus (kg): "))
print(f"mahlapakkide arv: {mahlapakkide_arv(arv)}")

input()
#banner
def banner(reklaamlause="sinu reklaamlause!!"):
    reklaamlause=reklaamlause.upper()
    return reklaamlause

    
lause=input("Reklaamlauseks on: ")
kordi=int(input("kordi kuvada: "))
for i in range(kordi):
    print(banner(lause))
    kordi-1

input()
#lk4

#tahvli juurde
nimi=input("Sisestage failinimi (nimekiri.txt): ")
fail = open(nimi , encoding="UTF-8")
faili_sisu = fail.readlines()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
d,m,y=d1.split("/")
for i, line in enumerate(faili_sisu):
    if i== int(d)-1:
        print(f"vastama tuleb: {faili_sisu[i]}")

input()
#jukebox
nimi=input("mis faili soovite avada (jukebox.txt, 80ndad.txt, eesti_muusika.txt, edm.txt): ")
fail = open(nimi , encoding="UTF-8")
faili_sisu = fail.readlines()
for i in range(len(faili_sisu)):
    print(f"{i+1}. {faili_sisu[i]}")
play=int(input("Mis laulu tahate mängida: "))-1
for i, line in enumerate(faili_sisu):
    if i== play:
        print(f"Mängitakse: {faili_sisu[i]}")

input()
#sissetulekud
fail = open("txt/konto.txt", encoding="UTF-8")
faili_sisu = fail.readlines()
for i in range(len(faili_sisu)):
    if float(faili_sisu[i]) > 0:
        print(faili_sisu[i])

fail.close()
input()
#ülikoooli vastuvõetud
fail = open("txt/rebased.txt", encoding="UTF-8")
vastuvõetud = []

aasta=int(input("Mis aastat tahad (2011-2019): "))
aasta=aasta-2011
for i, line in enumerate(fail):
    if i== aasta:
        vastuvõetud.append(int(line))

print(vastuvõetud)
fail.close()


input()
#Jänesevanemate mure ver.3
lap=int(input("Ringide arv: "))
porgand=0
for i in range(lap):
    if lap%2==0:
        porgand=porgand+2
    else:
        lap=lap-1

print(f"porgandite arv on: {porgand}")

input()

#lk 3

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

    