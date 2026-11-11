compra = int(input("Digite o valor da compra: "))
if compra >=200:
    desconto = compra *0.20
    print("o valor da compra é", compra)
    print("O valor do desconto é: ", desconto)
else:
    print("Não possui desconto sua compra é de: ", compra )