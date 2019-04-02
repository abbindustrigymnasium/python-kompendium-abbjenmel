mängd = range(500)#skapar arrayen mängd och ger den alla värden mellan 0 och 500
odd=[]#skapar arrayen odd
sumodd=0#skapar variabeln sumodd och sätter den lika med 0
for number in mängd:#för alla nummer i arrayen mänds sker följande kod
    if number%2==1:#om nummeret delat med två är ett sker följande kod
        odd=number#i arrayen odd adderas alla tal i nummer
        sumodd+=number#sumodd är lika med alla tal i nummer adderat med varandra
        
print(sumodd)#skriver ut värdet i variabeln sumodd
        
        