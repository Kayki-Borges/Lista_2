s = float(input("Digite o salário por hora:"))
h = float(input("Digite a quantidade do horas trabalhadas:"))
sb = s*h
print("Salário bruto:{}".format(sb))
if sb >= 900 and sb <= 1500:
    print("Ir:{}:{}".format("5%", s*(5/100)+s))
elif sb > 1500 and sb <= 2500:
    print("Ir:{}:{}".format("10%",s*(10/100)+s))
else :
    print("Ir:{}:{}".format("20%",s*(20/100)+s))
print("FGTS:{}".format("10%"))
