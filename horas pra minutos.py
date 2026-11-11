import math
horas = int(input("Digite quantas horas: "))
minutos = math.fma(horas, 60, 0)
print("o total de minutos é %2.f:"%(minutos))