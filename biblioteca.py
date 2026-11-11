print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
livros = []

while True:
    print("\nEscolha uma opção\n 1. Cadastrar livro\n 2. Consultar livro\n 3. Emprestar livro\n 4. Sair ")
    opçao = int(input("Digite o número da opção: "))
    
    if opçao == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livros.append((titulo, autor))
        print("Livro cadastrado com sucesso!")
    
    elif opçao == 2:
        titulo = input("Digite o título do livro para buscar: ")
        encontrado = False
        for livro in livros:
            if livro[0] == titulo:
                print(f"Livro encontrado: {livro[0]} por {livro[1]}")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")
    
    elif opçao == 3:
        titulo = input("Digite o título do livro para empréstimo: ")
        encontrado = False
        for livro in livros:
            if livro[0] == titulo:
                print(f"Livro emprestado {livro[0]} por {livro[1]} com sucesso")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")
    
    elif opçao == 4:
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida! Digite um número entre 1 e 4.")