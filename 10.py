s = float(input("Digite o salário:"))
print("-"*20)
if s <= 280:
    print("Você teve um aumento de 20%, seu salário agora é {}R$".format(s*(20/100)+s))
elif s > 280 and s < 700:
    print("Você teve um aumento de 15%, seu salário agora é {}R$".format(s*(15/100)+s))
elif s > 700 and s < 1500:
    print("Você teve um aumento de 10%, seu salário agora é {}R$".format(s*(10/100)+s))
else :
    print("Seu salário é de {}R$".format(s))
    print("-"*20)
    print("O percentual de aumento aplicado é de 5%")
    print("-"*20)
    print("Seu salário vai aumentar no valor de {}R$".format((s*(5/100)+s)-s))
    print("-"*20)
    print("O novo salário é {}".format(s*(5/100)+s))

