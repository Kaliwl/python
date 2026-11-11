import math
sombra = float(input("Digite o comprimento da sombra em metros: "))
angulo = math.radians(float(input("Digite o ângulo em graus: ")))
altura = math.tan(angulo) * sombra
print("A altura do prédio é de %.2f metros" % (altura))
