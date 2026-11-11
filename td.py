TD = (input("DIgite o tipo de diaria: "))
dias = int(input("Digite a quantidade de dias: "))
simples = 255
duplo = 305.50
triplo = 360.50
if TD == "simples":
    print("Valor total: R$ ", simples * dias)
elif TD == "duplo":
    print("Valor total: R$", duplo * dias)
elif TD == "triplo":
    print("Valor total: R$", triplo * dias)
else:
    print("Nenhuma diária é válida")