#ül9 moodulid
#richard markus tins it20
#9.12.20

#Eralda iskukoodist sünnikuupäev ja leia isiku vanus
from datetime import datetime, timedelta

kood=input("Isikukood: ")
if len(kood)==11:
    print(f"{kood[5:7]},{kood[3:5]},{kood[1:3]}")

#ma ei tea kuidas teha seda kuupäevaks mida saab lahutada