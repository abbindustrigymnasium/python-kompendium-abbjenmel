import math
print("Hur många vill ha 2 vanliga korvar?")#skriver ut en fras
van_2=input()#sparar värden från användaren i variabeln van_2
van_2=int(van_2)#omvandlar inehållet i variabeln van_2 till en integer från en string
print("Hur många vill ha 3 vanliga korvar?")#skriver ut en fras
van_3=input()#sparar värden från användaren i variabeln van_3
van_3=int(van_3)#omvandlar inehållet i variabeln van_3 till en integer från en string
print("Hur många vill ha 2 veganska korvar?")#skriver ut en fras
veg_2=input()#sparar värden från användaren i variabeln veg_2
veg_2=int(veg_2)#omvandlar inehållet i variabeln veg_2 till en integer från en string
print("Hur många vill ha 3 veganska korvar?")#skriver ut en fras
veg_3=input()#sparar värden från användaren i variabeln veg_3
veg_3=int(veg_3)#omvandlar inehållet i variabeln veg_3 till en integer från en string
dryck=van_2+ van_3+ veg_2 + veg_3#adderar flertalet värden i variabeln dryck
van_2korv= van_2*2#multiplicerar variabeln van_2 med två och sparar det nya värdet i van_2
van_3korv= van_3*3#multiplicerar variabeln van_3 med tre och sparar det nya värdet i van_3
veg_2korv= veg_2*2#multiplicerar variabeln veg_2 med två och sparar det nya värdet i veg_2
veg_3korv= veg_3*3#multiplicerar variabeln veg_3 med tre och sparar det nya värdet i veg_3
veganska= veg_2korv + veg_3korv#ger variabeln veganska värdet av två tidigare variabler adderade med varandra
vanliga= van_2korv + van_3korv#ger variabeln vanliga värdet av två tidigare variabler adderade med varandra
print(str(dryck) + " " + " " + str(veganska) + " " + str(vanliga))#skriver ut värdet av dryck, veganska och vanliga i string format
veganskapkt= veganska/4#delar variabeln veganska med fyra och sparar det nya värdet i veganskapkt
veganskapkt=math.ceil(veganskapkt)
vanligapkt = vanliga/8#delar variabeln vanliga med åtta och sparar det nya värdet i vanligapkt
vanligapkt=math.ceil(vanligapkt)
dryck=van_2+veg_2+van_3+veg_3
print(str(vanligapkt) + " " + str(veganskapkt) + " " +str(dryck))#skriver ut värdet av vanligapkt och veganskapkt i string format
print("Inköpslista: Vanlig korv " + str(vanligapkt)+ " Vegansk korv "+str(veganskapkt)+" Dryck "+str(dryck))#skriver ut inköpslistan
dryckkostnad=dryck*13.95#beräknar kostnaden för drycken
vegkostnad=veganskapkt*34.95#beräknar kostnaden för veganska korvar
vankostnad=vanligapkt*20.95#beräknar kostnaden för vanliga korvar
tot=vegkostnad+dryckkostnad+vankostnad#beräknar den totala kostnaden
print(str(tot)+" SEK")#skriver ut den totala kostnaden i terminalen