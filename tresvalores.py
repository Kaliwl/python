a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite outro numero: "))
if a>b and b<c:
    print("O menor valor é o B")
elif a<b and a<c:
    print("O menor valor é o A")
else:
    print("O menor valor é o C")