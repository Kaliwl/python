email = input("Entre com seu email: ")
if "@" in email:
    dominio = email.split("@")[1]
    print("O domínio do email é https://", dominio)
    
else:
    print("email inválido")
    
