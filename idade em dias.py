import math
idade = int(input("Digite sua idade em anos:"))
meses = int(input("Digite o número de meses adicionais:"))
dias = int(input("Digite o número de dias adicionais:"))
totalemdias = math.fma(idade, 365, math.fma(meses, 30, dias))
print("sua idade total em dias é %2.f" % (totalemdias))

