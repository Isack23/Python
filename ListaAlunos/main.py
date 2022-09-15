listaAluno = []
op = 1
id = 0
while (op != 4):
    print( "\nDIGITE A OPÇÃO QUE VOCÊ DESEJA? \n 1---> Cadastrar novo aluno\n 2---> Buscar por ID\n 3---> Pesquisar por nome\n 4---> Sair\n   Op:  ")
    op = int(input())
    if (op == 1):
        id = id + 1
        print("Digite o nome do aluno: ")
        nome = input()
        print("Digite o turma: ")
        turm = input()
        print("Digite o turno: ")
        turn = input()
        aluno = [id, nome, turm, turn]
        print(aluno)
        listaAluno.append(aluno)

    elif (op == 2):
        print("Digite um Id: ")
        n = int(input())
        tem = False
        for x in listaAluno:
            if n in x:
                print(x)
                tem = True
        if tem == False:
            print("não contem!")
    elif (op == 3):
        print("Digite um nome do aluno: ")
        n = input()
        tem = False
        for x in listaAluno:
            if n in x:
                print(x)
                tem = True
        if tem == False:
            print("não contem!")
    elif (op == 4):
        print("VOLTE SEMPRE")
    else:
        print("Digite uma opção válida!")
