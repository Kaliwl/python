turno = int(input("Digite o turno que você trabalha com os números: 1 (matutino), 2 (vespertino) ou 3 (noturno): "))
horas = int(input("Digite quantas horas você trabalhou hoje: "))
if turno == 3:
    dinheiro = horas * 45
    print("Você ganhou R$ ", dinheiro)
else:
    dinheiro1 = horas * 37.50
    print("Você ganhou R$ ", dinheiro1)
    