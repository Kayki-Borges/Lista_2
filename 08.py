p1 = float(input("Digite o primeiro preço:"))
p2 = float(input("Digite o segundo preço:"))
p3 = float(input("Digite o terceiro preço:"))
if p1 < p2 < p3:
    print("Você deve comprar  o produto de {}R$".format(p1))
elif p2 < p1:
    print("Você deve comprar o produto de {}R$".format(p2))
else:
    print("Voce deve comprar o produto de {}R$".format(p3))