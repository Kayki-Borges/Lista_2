l1 = float(input("Digite o primeiro lado:"))
l2= float(input("Digite o segundo lado:"))
l3 = float(input("Digite o terceiro lado:"))

if ((l1 + l2 > l3) and (l1 + l3 > l2)and (l2 + l3 > l1)):
    if (l1 == l2) and (l2 == l3):
        print("Seu triângulo é equilátero!")
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print("Seu triângulo é isósceles!")
    else:
        print("Seu triângulo é escaleno!")
else:
    print("Isto NÃO é triângulo!")