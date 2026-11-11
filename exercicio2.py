a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
delta = b**2 - 4*a*c
if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("As raízes são: ", x1, "e", x2)
elif delta == 0:
        x1 = -b / (2*a)
        print("A raiz é: ", x1)
else:
        print("Não é possível fazer a raiz de um número negativo")