s = float(input("Digite o salário:"))
if s <= 280:
    print("Você teve um aumento de 20%, seu slário agora é {}R$".format((20*s)/100))
elif s > 280 and s < 700:
    print("Você teve um aumento de 15%, seu salário agora é {}R$".format((15*s)/100))
elif s > 700 and s < 1500:
    print("Você teve um aumento de 10%, seu salário agora é {}R$".format((10*s)/100))
else :
    print("Seu salário é de {}R$".format(s))
    print("O percentual de aumento aplicado é de {}".format("10%"))
    print("Seu salário vai aumentar no valor de {}R$".format("100"))
    print("O npvp salário é {}".format((5*s)/100))

