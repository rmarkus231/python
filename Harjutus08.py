#ül8 klassid ja objektid
#richard markus tins it20
#9.12.20

class Auto:
    #atribuudid
    automark='teadmata'
    aasta=0
    hind=0
    värv='puudub'
    maks=0
    
    #meetodid
    def __init__(self,x,y,z,a,b):
        self.automark = x
        self.aasta = y
        self.hind = z
        self.varv = a
        self.maks = b
    
    def lisaMark(self,x):
        self.mark = x
        
    def lisaAasta(self,x):
        self.Aasta = x
        
    def lisaHind(self,x):
        self.Hind = x
        
    def lisaVarv(self,x):
        self.varv = x
    
    def lisaKiirus(self,x):
        self.maks = x
        
    def kuva(self):
        print(f"automark: {self.automark} \nAasta: {self.aasta} \nHind: {self.hind} \nVärv: {self.varv} \nMaksimum kiirus: {self.maks}")
    
minuAuto= Auto("opel",2000, 2500,"lilla","95")
minuAuto.kuva()