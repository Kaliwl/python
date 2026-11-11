idade = int(input("Digite a idade: "))
if idade <= 16:
    print("Não eleitor")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
else:
    print("Eleitor facultativo")