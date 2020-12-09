#Python harjutus 6
#richard markus tins it20
#02:12.20

#faili avamine
minu_fail = open('nimi.txt', 'r')
ref=0
ke=0
kokku=[]
#faili sisu kuvamine
faili_sisu = minu_fail.readlines()
for i in range(len(faili_sisu)):
    #print(faili_sisu[i],end="")
    enimi,pnimi,erakond,sopru=faili_sisu[i].split(" ")
    print(f"{enimi:11}{pnimi:11}{erakond:4}{sopru:5}",end="")
    if erakond== "RE":
        ref+=1
    if erakond=="KE":
        ke+=1
    #lisab erakonna loendisse kui teda seal pole
    if erakond not in kokku:
        kokku.append(erakond)
    text=enimi+" "+pnimi+"\n"
    with open('nimed.txt','a') as fail_kirjutamiseks:
        fail_kirjutamiseks.write(text)
    
print(f"\nReformikaid kokku: {ref}")
print(f"Keskikuid kokku: {ke}")
print(f"Erakondi kokku: {len(kokku)}")

#faili sulgemine
minu_fail.close()