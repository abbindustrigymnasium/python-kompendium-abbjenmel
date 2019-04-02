print("Välj ett land")#skriver ut en uppgift till användaren
land=input()#sparar värdet som användaren skrivit i variabeln land
land=land.title()#ändrar värdet i land så att första bokstaven är stor men alla andra bokstäver i ordet är små
skandinavien=["Sverige", "Norge", "Finland", "Island", "Danmark"]#skapar arrayen skandinavien som håller alla land i skandinavien
storbrittannien=["England", "Nordirland", "Scottland", "Wales"]#skapar arrayen storbrittanien som håller alla land i storbrittanien
if land in skandinavien:#om användarens land finns med i arrayen skandinavien sker följande rad kod
    print(land+ " ligger i skandinavien")#skriver ut ett meddelande i terminalen
elif land in storbrittannien:#om användarens land finns med i arrayen strobrittanien sker följande rad kod
    print(land+ " ligger i storbrittanien")#skriver ut ett meddelande i terminalen
else:#om ingen av de två förjande möjligheterna var sanna sker följande raden kod
    print(land+ " ligger inte i skandinavien eller storbrittanien")#skriver ut ett meddelande i terminalen