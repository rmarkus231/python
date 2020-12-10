#mäng
#Richard Markus Tins
import time

translate = {
    "defence":"Kaitses",
    "strength":"Tugevuses",
    "magic":"maagias",
    "perception":"täpsuses",
}

stats=["defence","strength","magic","perception"]
class createPlayer:
    #atribuudid
    name='teadmata'
    defence=0
    strength=0
    magic=0
    perception=0
    
    def __init__(self,n,d,s,m,p):
        self.name=n
        self.defence=d
        self.strength=s
        self.magic=m
        self.perception=p
    
    def showStats(self):
        print("\n\n\n\n"+"*"*20+"\n\n\n\n")
        print(f"Tegelane: {self.name}")
        time.sleep(1)
        print(f"Kaitse: {self.defence}")
        time.sleep(1)
        print(f"Tugevus: {self.strength}")
        time.sleep(1)
        print(f"Maagia: {self.magic}")
        time.sleep(1)
        print(f"Täpsus: {self.perception}")

        
def createCharacter():
    n=input("Mu nimi vist oli: ")
    d=0
    s=0
    m=0
    p=0
    x=100
    print(f"Sul on {x} skillpointi jagada")
    for i in range(len(stats)-1):
        j=input(f"Ma olin vist nii hea {translate[stats[i]]}: ")
        if i == 0:
            d=int(j)
        if i == 1:
            s=int(j)
        if i == 2:
            m=int(j)
        print(f"Sul on {x-d-s-m-p} skillpointi jagada")
        time.sleep(1)
    print(f"Ma olin {translate[stats[3]]} kindlasti nii hea: {x-d-s-m}")
    p=x-d-s-m
    p = createPlayer(n,d,s,m,p)
    return p

def proloog():
    for i in range(5):
        print("Sa ärkad alasti keset talu ning ei mäleta kes sa oled.")
        time.sleep(1)
        print("Sa ei mäleta oma nime ega midagi, eile pidi olema vist päris kõva pidu")
        time.sleep(1)

y=input("Soovite mängida? (jah/ei) ")
if y == "jah":
    proloog()
    #player=createCharacter()
    #print(player.showStats())
    
            




