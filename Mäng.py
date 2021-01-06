#mäng
#Richard Markus Tins
import time

#saves faili loomine
save=open("saves.txt","a+")
#faili salvestamise funktsioon
def check_saves(n=""):
    save=open("saves.txt","r")
    saves=save.readlines()
    n=n.replace(" ","-")
    for i in range(len(saves)):
        sn,sd,ss,sm,sp=saves[i].split(",")
        if sn == n:
            n=n.replace("-"," ")
            pl = createPlayer(sn,sd,ss,sm,sp)
            return pl
    return 0

#salvestab tegelase
def save_player(n="",d=0,s=0,m=0,p=0):
    save=open("saves.txt","a+")
    print(n,d,s,m,p)
    nn=n.replace(" ","-")
    save.write(nn+","+str(d)+","+str(s)+","+str(m)+","+str(p))
    return


#kiire tõlke sõnastik
translate = {
    "defence":"Kaitses",
    "strength":"tugevuses",
    "magic":"maagias",
    "perception":"laskmises",
}

stats=["defence","strength","magic","perception"]
#tegelane
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
        print(f"\nTegelane: {self.name}")
        time.sleep(t)
        print(f"Kaitse: {self.defence}")
        time.sleep(t)
        print(f"Tugevus: {self.strength}")
        time.sleep(t)
        print(f"Maagia: {self.magic}")
        time.sleep(t)
        print(f"Täpsus: {self.perception} \n")
        
#lollikindel skilli saamise funktsioon
def find_skill():
    skill=""
    x=100
    print(f"Sul on {x} skillpointi jagada")
    for i in range(len(stats)-1):
        if x != 0:
            j=input(f"Ma olin vist {translate[stats[i]]} nii hea: ")
            if x < int(j):
                while x < int(j):
                    j=input("Peab olema väiksem kui olemasolevad punktid: ")
                    if i !=2:
                        s=int(j)+","
                    elif i ==2:
                        s=int(j)
                x=x-int(j)
                
            elif i != 2:
                x=x-int(j)
                s=int(j)
                s=str(s)+","
                
            elif i == 2:
                x=x-int(j)
                s=int(j)
                s=str(s)
            skill=skill+s
        else:
            if x == 0:
                print(f"Ma {translate[stats[i]]}t üldse ei osanud: 0")
                if i != 2:
                    s=0
                    s=str(s)+","
                elif i == 2:
                    s=0
                    s=str(s)
            skill=skill+s
        print(f"Sul on {x} skillpointi jagada")
        time.sleep(1)
    return skill

#tegelase loomise funktsioon      
def createCharacter():
    n=input("Mu nimi oli vist: ")
    if check_saves(n) != 0:
        print(f"Salvestatud karakteritest leiti {n}")
        return check_saves(n)
    else:
        
        d,s,m=find_skill().split(",")
        
        d=int(d)
        s=int(s)
        m=int(m)
        
        print(f"Ma olin {translate[stats[3]]} kindlasti nii hea: {100-d-s-m}")
        
        p=100-d-s-m
        
        sav=input("Kas soovite tegelase salvestada? (jah/ei)\n")
        if sav == "jah":
            save_player(n,d,s,m,p)
        p = createPlayer(n,d,s,m,p)
        return p

#proloogi lugemise funktsioon
def proloog():
    print("Sa ärkad alasti keset ristteed ning ei mäleta kes sa oled.")
    time.sleep(t)
    print("Põhja poole on mets kus on pimedam ja puud on kiduramad.")
    time.sleep(t)
    print("Ida poole on kanakuut, täiesti tavaline kanakuut...")
    time.sleep(t)
    print("Lõuna poole on mahajäetud saeveski.")
    time.sleep(t)
    print("Lääne poole on kõrts.")
    time.sleep(t)
    print("Aga ennem... kes sa oled?")
    time.sleep(t)
    
#mängu algus
y=input("Soovite mängida? (jah/ei) \n")
#mängu dialoogi kiiruse valik
speed=input("dialoogi kiirus: (kiire,keskmine,aeglane) \n")
if speed == "kiire":
    t=0.5
elif speed == "keskmine":
    t=1
elif speed == "aeglane":
    t=1.5

if y == "jah":
    hp=20
    proloog()
    player=createCharacter()
    print(player.showStats())
    
    
            




