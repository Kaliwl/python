frequencia = int(input("Digite a frequencia :"))
media = int(input("Digite a media :"))
if frequencia < 75:
 print("Reprovado por falta")
elif frequencia >=75 and media < 6:
 print("reprovado por nota")
elif frequencia>=75 and media >= 6:
    print("aprovado")