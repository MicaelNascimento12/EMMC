# Autor: Micael Nascimento de Sousa
# Data: 06/05/2025

import os
import funcoes as F

aluno = F.carregarDados()

F.criarTabela()
F.carregarDados()

while True:
    os.system("cls")

    print("----------- Escola de música de Mogi das Cruzes -----------")

    opcao = input('''
    [1] Criar novo registro de aluno 
    [2] Exibir lista de alunos
    [3] Buscar registro por nome de aluno          
    [4] Alterar registro de aluno
    [5] Excluir registro de aluno
    [6] Encerrar programa                            
                                                                
    ===>  ''')

    if opcao == '1':
        F.cadastrarAluno()

    elif opcao == '2':
         F.exibirLista()

    elif opcao == '3':
        F.buscarNome(aluno)

    elif opcao == '4':
        F.alterar_Cadastro(aluno)
        
    elif opcao == '5':
        F.excluir_Cadastro(aluno)

    elif opcao == '6': 
        print('Programa encerrado!')
        break
    else:
            print("Opção inválida! Escolha um número entre 1 e 6.")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        print('Programa encerrado!')
        break
