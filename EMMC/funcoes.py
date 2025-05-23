import re
import sqlite3

from rich.console import Console
from rich.table import Table

def conectar():
    return sqlite3.connect("escola_musica.db")

def criarTabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            instrumento TEXT,
            curso TEXT
        )
    ''')
    conexao.commit()
    conexao.close()

def salvarDados(nome, instrumento, curso):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO alunos (nome, instrumento, curso)
        VALUES (?, ?, ?)
    ''', (nome, instrumento, curso))
    conexao.commit()
    conexao.close()


def carregarDados():
    aluno = {}
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        Matricula, Nome, Instrumento, Curso = linha
        aluno[Matricula] = [Nome, Instrumento, Curso]
    conexao.close()
    return aluno

def validar_Matricula(mensagem):
   while True:
        try:
           return int(input(mensagem))
        except ValueError:
           print("Erro! Digite um número válido.")

def cadastrarAluno():
    nome = input("Nome: ")
    instrumento = input('Instrumento: ')
    curso = input('Período de curso: ')
    
    salvarDados(nome, instrumento, curso)
    print("\nAluno cadastrado com sucesso!")

def alterar_Cadastro(aluno):
    matriculaAlteracao = int(input("Insira o número de matrícula: "))
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM alunos WHERE matricula = ?", (matriculaAlteracao,))
    aluno_encontrado = cursor.fetchone()
    
    if aluno_encontrado:
        print('Registro encontrado:')
        print(f'{" Matricula ":=^30} {" Nome ":=^30} {" Instrumento ":=^30} {" Curso ":=^30}')
        print(f'{aluno_encontrado[0]:^30} {aluno_encontrado[1]:^30} {aluno_encontrado[2]:^30} {aluno_encontrado[3]:^30}')

        opt = input('Digite (s) para alterar registro ou (n) para cancelar: ')
        if opt.lower() == 's':
            print("\nDigite os novos dados:")
            nome = input("Nome: ")
            instrumento = input("Instrumento: ")
            curso = input("Período de curso: ")

            cursor.execute('''
                UPDATE alunos
                SET nome = ?, instrumento = ?, curso = ?
                WHERE matricula = ?
            ''', (nome, instrumento, curso, matriculaAlteracao))
            
            conexao.commit()
            print("Registro atualizado com sucesso!")

    else: 
        print('Matrícula não encontrada!')
    
    conexao.close()


def excluir_Cadastro(aluno):
    matriculaExclusao = int(input("Insira o número de matrícula: "))
    if matriculaExclusao in aluno:
        print('Registro encontrado: ')
        print(f'{" Matricula ":=^30} {" Nome ":=^30} {" Instrumento ":=^30} {" Curso ":=^30}')
        print(f'{matriculaExclusao:^30} {aluno[matriculaExclusao][0]:^30} {aluno[matriculaExclusao][1]:^30} {aluno[matriculaExclusao][2]:^30}')

        opt = input('Digite (s) para alterar registro ou (n) para cancelar: ')
        if opt.lower() == 's':
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM alunos WHERE matricula = ?", (matriculaExclusao,))
            conexao.commit()
            conexao.close()
            del aluno[matriculaExclusao]
            print("Registro excluído com sucesso!\n")


def buscarNome(aluno):
    nomeBusca = input('Insira o nome do aluno: ')
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM alunos WHERE LOWER(nome) LIKE ?", ('%' + nomeBusca.lower() + '%',))
    alunos_encontrados = cursor.fetchall()

    conexao.close()

    if alunos_encontrados:
        print("\nRegistros encontrados:")
        print(f'{" Matricula ":=^30} {" Nome ":=^30} {" Instrumento ":=^30} {" Curso ":=^30}')
        for matricula, nome, instrumento, curso in alunos_encontrados:
            print(f'{matricula:^30} {nome:^30} {instrumento:^30} {curso:^30}')
    else:
        print("Nenhum aluno encontrado")

def exibirLista():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    
    conexao.close()

    console = Console()
    tabela = Table(title="Lista de Alunos", style="bold cyan")

    # Definindo colunas da tabela
    tabela.add_column("Matrícula", style="white", justify="center")
    tabela.add_column("Nome", style="white", justify="center")
    tabela.add_column("Instrumento", style="white", justify="center")
    tabela.add_column("Curso", style="white", justify="center")

    # Adicionando dados à tabela
    for matricula, nome, instrumento, curso in alunos:
        tabela.add_row(str(matricula), nome, instrumento, curso)

    console.print(tabela)


            

    
            


        