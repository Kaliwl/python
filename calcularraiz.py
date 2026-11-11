import math
num = int(input("Digite um número: "))
if num > 0:
    raiz = math.sqrt(num)
    print(f"a raioz quadrada de um número é:{raiz}")
else:
    print("Não é possível calcular a raiz de um número negativo.")