n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))
if n1>n2 and n1>n3 and n2<n1:
    print("O maior numero é {} e o menor é {}".format(n1,n2))
elif n2>n1 and n2>n3 and n3<n2:
    print("O maior número é {} e o menor é {}".format(n2,n3))
else:
    print("O maior número é {} e o menor é {}".format(n3,n1))