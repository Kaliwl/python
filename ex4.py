agua = int(input("Digite o valor d a conta de agua: "))
luz = int(input("Digite o valor da conta de luz: "))
telefone = int(input("Digite o valor da conta de telefone: "))
salário = int(input("Digite o valor do seu salário: "))
if agua + luz + telefone > salário: 
    print("Você não tem dinheiro suficiente para pagar as contas")  
else:
    resto = salário - (agua + luz + telefone)
    print("Voce tem dinheiro suficiente para pagar as contas. o que sobra é", resto)
    