valorprestacao = int(input("digite o valor da prestação: "))
diasatraso = int(input("digite o número de dias de atraso: "))
multa = valorprestacao*0.02
multa1 = int(input("digite o porcentagem da multa: "))
multapordia = valorprestacao*diasatraso*0.0003
prestacao = valorprestacao + multa + multapordia
print("O valor da prestação em atraso é %2.f" %(prestacao))

prestacao2 = valorprestacao+(valorprestacao*(multa1/100)*diasatraso)
print("O valor da prestação em atraso é %2.f" %(prestacao2))

