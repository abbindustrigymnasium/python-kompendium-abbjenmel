print("Vad heter du?")# ber användaren att mata in sitt namn
namn=input()#sparar det inmatade värdet i variabeln namn
print("Hur gammal är du?")#frågar användaren om dens namn
ålder=input()#sparar det inmatade värdet i variabeln ålder
if ålder=="1":
    print(namn+", enligt vårdguiden behöver du sova 14 timmar per natt")
elif ålder=="2":
    print(namn+", enligt vårdguiden behöver du sova 13 timmar per natt")
elif ålder=="3":
    print(namn+", enligt vårdguiden behöver du sova 12 timmar per natt")
elif ålder=="4":
    print(namn+", enligt vårdguiden behöver du sova 11,5 timmar per natt")
elif ålder=="5" or ålder=="6":
    print(namn+", enligt vårdguiden behöver du sova 11 timmar per natt")
elif ålder=="7":
    print(namn+", enligt vårdguiden behöver du sova 10,5 timmar per natt")
elif ålder=="8" or ålder=="9" or ålder=="10":
    print(namn+", enligt vårdguiden behöver du sova 10 timmar per natt")
elif ålder=="11":
    print(namn+", enligt vårdguiden behöver du sova 9,5 timmar per natt")
elif ålder=="12" or ålder=="13" or ålder=="14" or ålder=="15":
    print(namn+", enligt vårdguiden behöver du sova 9 timmar per natt")
elif ålder=="16":
    print(namn+", enligt vårdguiden behöver du sova 8,5 timmar per natt")
else:
    print(namn+", enligt vårdguiden behöver du sova 8 timmar per natt")

