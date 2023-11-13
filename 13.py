n1 = float(input("Digite a primeira nota parcial:"))
n2 = float(input("Digite a segunda nota parcial:"))
nt = (n1 + n2)/2
if nt >= 9 and nt <= 10:
    print("Aprovado!")
elif nt >= 7.5 and nt <= 9:
    print("Aprovado!")
elif nt >= 6 and nt <= 7.5:
    print("Aprovado!")
elif nt > 4 and nt < 6:
    print("Reprovado!")
else:
    print("Reprovado!")