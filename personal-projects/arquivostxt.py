import os, shutil, json

try:
    os.mkdir('UFPA')
except FileExistsError:
    pass

diretorio = 'C:/Python/PLN/UFPA'

stts = True

while stts:

    nome = input("Insira seu nome. ")
    nome_arquivo = nome.replace(' ', '-') + '.json'

    idade = input('Insira sua idade. ')

    generos = {0: 'Masculino', 1: 'Feminino', 2: 'Outro'}
    genero = int(input('Insira seu gênero. \nMASCULINO - [0] \nFEMININO - [1] \nOUTRO - [2] \n'))
    if genero in generos:
        genero = generos[genero]

    cidade = input("Insira sua cidade. ")

    dicionario = {}
    dicionario = [nome, idade, genero, cidade]

    nome_arquivo = os.path.join(diretorio, nome_arquivo)
    with open(nome_arquivo, 'w') as file:
        json.dump(dicionario, file)

    condicao = int(input('Adicionar mais um aluno? \nSIM - [0] \nNÃO - [1] \n'))
    if condicao == 1:
        stts = False

