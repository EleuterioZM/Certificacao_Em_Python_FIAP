import json

usuarios = {}

while True:
    opcao = input(
        "O que deseja realizar?\n"
        "1 - Cadastrar Usuario\n"
        "2 - Buscar um Usuario\n"
        "3 - Excluir um Usuario\n"
        "4 - Listar Usuarios\n"
        "5 - Salvar Usuario\n"
        "0 - Sair\n"

    ).upper()

    if opcao == "1":
        chaves = input("Digite o Login: ").upper()
        nome = input("Digite o nome do usuario: ").upper()
        data = input("Digite a ultima data de acesso: ").upper()
        estacao = input("Qual foi a ultima estacao acessada: ").upper()

        usuarios[chaves] = [nome, data, estacao]
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        chaves = input("Digite o Login do usuário que deseja buscar: ").upper()
        if chaves in usuarios:
            print(f"Usuário encontrado: {usuarios[chaves]}")
        else:
            print("Usuário não encontrado.")

    elif opcao == "3":
        chaves = input("Digite o Login do usuário que deseja excluir: ").upper()
        if chaves in usuarios:
            del usuarios[chaves]
            print("Usuário excluído com sucesso!")

        else:
            print("Usuário não encontrado.")


    elif opcao == "4":
        # Reading from the file
        with open("Savalvar_Usuario.json", "r") as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)

    elif opcao == "5":
        with open ("Savalvar_Usuario.json", "a") as arquivo :
            json.dump(usuarios, arquivo)
            print("Usuários salvos com sucesso!")


    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    # Pergunta se o usuário deseja continuar
    resposta = input("Digite \"Y\" para continuar ou qualquer outra tecla para sair: ").upper()
    if resposta != "Y":
        print("Saindo do sistema...")
        break