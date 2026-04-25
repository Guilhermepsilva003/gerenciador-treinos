from models.treino import Treino

treinos = []

while True:
    print("\n=== GERENCIADOR DE TREINOS ===")
    print("1. Criar treino")
    print("2. Adicionar exercício")
    print("3. Listar treinos")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do treino: ")
        treino = Treino(nome)
        treinos.append(treino)
        print(f"✅ {nome} criado com sucesso!")

    elif opcao == "2":
        if len(treinos) == 0:
            print("⚠️ Nenhum treino cadastrado. Crie um treino primeiro!")
        else:
            print("\nTreinos disponíveis:")
            for i, treino in enumerate(treinos):
                print(f"{i + 1}. {treino.nome}")
        
            indice = int(input("\nEscolha o número do treino: ")) - 1
            nome = input("Nome do exercício: ")
            series = int(input("Séries: "))
            repeticoes = int(input("Repetições: "))
        
            treinos[indice].adicionar_exercicio(nome, series, repeticoes)
            print("✅ Exercício adicionado com sucesso!")

    elif opcao == "3":
        if len(treinos) == 0:
            print("⚠️ Nenhum treino cadastrado!")
        else:
            print("\n=== SEUS TREINOS ===")
            for treino in treinos:
                print(treino)

    elif opcao == "4":
        print("Até logo!")
        break

    else:
        print("Opção inválida!")