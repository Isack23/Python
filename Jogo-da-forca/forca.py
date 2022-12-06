import os
import random
op = 1
while op == 1:
    print('\nJOGO DA FORCA')
    nome = input("Digite o nome do jogador: ").upper()
    print(f'Ola {nome}! Vamos começar a jogar?')
    input('\nPressione ENTER para começar')
    os.system('cls')


    lista_de_palavras = ['rebeca', 'maquinas', 'exatual', 'tiuria, jogademais']
    palavra_selecionada = random.choice(lista_de_palavras).upper()
    tamanho_palavra = len(palavra_selecionada)
    palavra_codificada = ['_'] * tamanho_palavra
    quantidade_de_erros = 0


    while '_' in palavra_codificada and quantidade_de_erros < 6:
        print(f'\nO tema é Expressões mais usadas na Turma S4 - Informatica, A palavra tem {tamanho_palavra} letras')
        print(f'Contagem de Erros: {quantidade_de_erros} de 6\n')
        for letra in palavra_codificada:
            print(letra, end='  ')  # _ _ _ _
        print()

        letra_escolhida = input('\nDigite uma letra: ').upper()
        acertou = False
        for i in range(len(palavra_selecionada)):
            if letra_escolhida == palavra_selecionada[i]:
                palavra_codificada[i] = letra_escolhida
                acertou = True


        if acertou == True:
            print('\nAcertou... tem essa letra na palavra !')

        else:
            print('\nErrou... Não tem essa letra na palavra. Escolha outra !')
            quantidade_de_erros = quantidade_de_erros + 1


    if quantidade_de_erros == 6:
        print('\nInfelismente você perdeu o jogo da forca.')
    else:
        print('\nParabéns! Você ganhou o jogo da forca ! ')

    print(f'A palavra era: {palavra_selecionada}\n')
    
    # condiçoes para recomeçar ou finalizar o jogo.
    print('Jogar Novamente ? \n'
          '1-Sim \n'
          '2-Não ')
    
    op2 = int(input("Digite a Opção: "))
    if op2 == 1:
        op = 1
    elif op2 == 2:
        op = 2
        print("\nJogo Encerrado... Até a próxima.")