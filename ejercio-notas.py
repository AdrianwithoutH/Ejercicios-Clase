nota=float(input("Dime tu nota:\n\n"))
if nota <0:
    print("Incorrecto\n")
elif nota <5:
    print("Insuficiente\n")
elif nota <6:
    print("Sufiente\n")
elif nota <7:
    print("Bien\n")
elif nota <9:
    print("Notable\n")
elif nota <=10:
    print("Sobresaliente\n")
else:
    print("Incorrecto")