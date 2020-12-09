#harjutus 4
#richard markus tins it20
#25:11.20
import random
import math

#ruutude ja kuupide tabel

print("nr\troot\tkuup")
for i in range(1,5):
    print(f"{i}\t{i*i}\t{i*i*i}")

input()
#pank
intress=0.05
algsumma=10000
aasta=5
loop=1
konto=algsumma
print(f"Aasta\tAlgsumma\tIntress\tAasta lõppuks")
while loop <= aasta:
    print(f"{loop}\t{algsumma:.2f}\t{algsumma*intress:.2f}\t{algsumma+algsumma*intress:.2f}")
    algsumma=algsumma+algsumma*intress
    loop=loop+1

print(f"Summa kokku: {algsumma:.2f}")
print(f"Kasum: {algsumma-konto:.2f}")
input()
#arvude arvamine

print("*********************")
print("*****ARVAMISMÄNG*****")
print("*********************")

arv=int(random.randint(1,3))
arvamised=0
status="L"
while arvamised < 3 or vastus=="jah" or arvamised==0:
    if arvamised<3 and status == "L":
        quess=int(input("Arva ära vahemikkus 1-3: "))
        if quess == arv:
            print("Võitsite","\n")
            status="W"
        else:
            print("proovige uuesti")
            arvamised=arvamised+1
    else:
        vastus=input("kas soovite uuesti mängida? (jah,ei) ")
        if vastus == "jah":
            arvamised=arvamised*0
            arv=int(random.randint(1,4))
            status = "L"
        else:
            arvamised=10
#prindib aint 5ga jaguvad arvud
input()
print("5ga jaguvad arvud 0-100 on")
for i in range(1,101):
    if i%5==0:
        print(i)
print("")
#pisike korrutus tabel
input()
y=5
for i in range(1,11):
    print(f"{y} * {i} = {y*i}", end="\n")
    
#paaris ja paaritu
input()
print("")
arv=int(random.randint(0,100))
if arv%2==0:
    print(f"{arv} on paaris arv")
else:
    print(f"{arv} on paaritu")
    
print("")
#loto
input()
for a in range(5):
    print(random.randint(0,9))

print("")

#tärnid
input()
for i in range(0,5):           #read
    for j in range(0,5):       #veerud
        print('* ', end='')
    print()
    
print("")

for i in range(1,6):
    print('*'*i)

print("")

x=6
for i in range(1,x):
    print('*'*(x-i))
    
#jalgpalli meeskond
input()
sugu=input("mis soost olete (mees,naine): ")
if sugu == "naine":
    print("te ei sobi antud meeskonda")
else:
    vanus=int(input("Kui vana te olete: "))
    if 16 <= vanus <= 18 and sugu == "mees":
        print("sobite antud meeskonda")
    else:
        print("te ei sobi antud meeskonda")

#müük
input()
hind=float(input("toote hind eurodes: "))
if hind <= 10:
    print(f"lõpplik hind on {hind-hind*0.1}")
elif hind>=10:
    print(f"lõpplik hind on {hind-hind*0.2}")

#ruut
#== on võrdne
#= võrdub
input()
sides=input("sisesta ruudu küljed: (1,2)")
k1,k2,k3,k4=sides.split(",")
if k1==k2 :
    print("tegemist on ruuduga")
else:
    print("tegemist ei ole ruuduga")
    
#matemaatika
input()
num1=int(input("sistage 1. arv: "))
num2=int(input("sistage 2. arv: "))
tehe=input("sisesta tehe: (+-*/)")
if tehe=="+":
    print(f"{num1}+{num2}={num1+num2}")
elif tehe=="-":
    print(f"{num1}-{num2}={num1-num2}")
elif tehe=="/":
    print(f"{num1}/{num2}={num1/num2}")
elif tehe=="*":
    print(f"{num1}*{num2}={num1*num2}")

#juubel
input()
aasta=int(input("mis aastal sündusite?: "))
vanus=2020-aasta
if vanus%5==0:
    print("tegemist on juubeliga")
else:
    print("tegemist ei ole juubeliga")

