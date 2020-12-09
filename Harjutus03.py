#Harjutus 03
#Richard Markus Tins
import datetime

#palindroom
sona=input("sisetsa sõna : ")
print(sona.lower() == sona.lower()[::-1])

#korralik nimi
name=input("mis on sinu nimi: ")
name=name.lower()
name=name.capitalize()
print("Tere,",name,"!")

#vandumine
tekst=input("sisestage midagi mis sisaldab \"kurat\": ")
print(tekst.replace('kurat', '***'))

#email
email=input("sisestage oma email: ")
print('@' in email)

#tundide ajad
algus=input("millal algavad tunnid? (hh:mm)")
lopp=input("millal lõppevad tunnid? (hh:mm)")
hh1,mm1=algus.split(":")
hh2,mm2=lopp.split(":")
aeg1=int(hh1)*60+int(mm1)
aeg2=int(hh2)*60+int(mm2)
vahe=aeg2-aeg1
h=vahe//60
m=vahe % 60
print(f"Päeva pikkus on {h}:{m}")

