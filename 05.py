n1 = float(input("Digite a primeira nota parcial:"))
n2 = float(input("Digite a segunda nota parcial"))
m = (n1 + n2) / 2
if m == 10:
    print("Aprovado com Distinção!")
elif m >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")