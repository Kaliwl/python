a = input("Digite a operação desejada(soma, subtração, multiplicação ou divisão): ")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if a == "soma":
    print(num1 + num2)
elif a == "subtração":
    print(num1 - num2)
elif a == "multiplicação":
    print(num1 * num2)
elif a == "divisão":
    print(num1 / num2)
