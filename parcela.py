total = float(input("Digite o total da sua compra: "))
parcelas = int(input("Digite o número de parcelas: "))
if parcelas == 2:
   v =  (total*0.03)+total
   print(v)
elif parcelas == 4:
    v = (total*0.07)+total
    print(v)
elif parcelas == 6:
    v = (total*0.09)+total 
    print(v)   
elif parcelas == 8:
   v = (total*0.12)+total
   print(v)
else:
    print("O número de parcelas é inválido")
print("O valor das suas parcelas é:", v/parcelas)
