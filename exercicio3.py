produto = input("Digite o nome do seu produto: ")
vc = float(input("Digite o valor de compra: "))
if vc <10:
    vv = vc*1.70
    print(f"O produto é {produto} e o valor de venda é {vv}")
elif 10<= vc < 30:
    vv = vc*1.50
    print(f"O produto é {produto} e o valor de venda é {vv}")
elif 30<= vc < 50:
  vv = vc*1.40
  print(f"O produto é {produto} e o valor de venda é {vv}")
elif vc >= 50:
  vv = vc*1.30
  print(f"O produto é {produto} e o valor de venda é {vv}")
    