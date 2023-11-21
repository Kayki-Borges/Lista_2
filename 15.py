a = float(input("Digite o valor de a: "))
if a == 0:
    print("isto não é uma equação do segundo grau!")
else:
    b = float(input("Digite o valor de b:"))
    c = float(input("Digite o valor de c:"))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Resultado de delta é menor que 0. Não há raízes reais.")
    elif delta == 0:
        raiz1 = (-b) / (2 * a)
        print("Delta é zero. A raíz é {}".format(raiz1))
    else:
        raiz2 = (-b + (delta ** (1 / 2))) / (2 * a)
        raiz3 = (-b - (delta ** (1 / 2))) / (2 * a)
        print(
            f"Delta maior que zero. A raíz 1 é {raiz2}, e a raiz 2 é {raiz3}")