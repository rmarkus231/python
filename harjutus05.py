#harjutus 5, massiivid
#richard markus tins it20
#26:11.20

#lintdiagramm
vanused = [15,14,68,10,5,32,12,54]
for i in vanused:
    print("*"*i)

input()
#vanused
vanused = [15,14,68,10,5,32,12,54]
print(f"Suurim arv: {max(vanused)}")
print(f"Väiksemine: {min(vanused)}")
print(f"Summa: {sum(vanused)}")
print(f"Keskmine: {sum(vanused)/len(vanused)}")

input()
#duplikaadid
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus_nimekiri=[]

#lisab õpilased uute nimekirja kui teda seal pole
for x in range(len(opilased)):
    if opilased[x] not in uus_nimekiri:
        uus_nimekiri.append(opilased[x])

for i in uus_nimekiri:
    print(i)

input()
#massiivi osa muutmine
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
print("vbana nimekiri")
for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
    
replace=int(input("mitmendat soovite muuta? "))-1
new=input("milleks soovite muuta? ")
print(f"\n Valisid: {opilased[replace]}")
opilased[replace]=new
print("\n uus nimekiri")

for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
    
input()
#Nimede lisamine loendisse
nimed=[]
for i in range(5):
    nimi=input("sisesta nimi: ")
    nimed.append(nimi)
    
nimed.sort()
print(nimed)
print(f"Viimati lisatud: {nimi}")
