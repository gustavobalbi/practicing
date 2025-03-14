import os, shutil, json

def create_dir():
        try:
            os.mkdir('Escolas')
        except FileExistsError:
            pass

def choose_mode():
    answ = int(input("Criar/Reescrever arquivo ou adicionar informação a um existente? \n[1] - CRIAR/REESCREVER \n[2] - ADICIONAR \n-> "))
    if answ == 1:
        mode = 'w'
    else:
        mode = 'a'

    return mode


def create_dict():
    qtd = int(input("Insira quantas turmas você possui. "))
    materias = {}
    count = 0

    while count < qtd:
        materia = input("Insira o nome da matéria. ")
        alunos_dict = {}
        alunos = int(input("Insira a quantidade de alunos matriculados. "))
        for i in range(alunos):
            nome = input('Insira o nome completo do aluno. ')
            notas = []
            for j in range(3):
                nota = float(input(f'Insira a nota da {j+1}ª AVALIAÇÃO de {nome.split()[0].upper()}. '))
                notas.append(nota)

            alunos_dict[nome] = notas
        
        materias[materia] = alunos_dict

        count += 1
    
    return materias

def create_file(dicionario):
    diretorio = 'Escolas'

    nome = input("Qual será o nome do arquivo? (sem símbolos especiais, acentuações e espaços.) ") + '.json'
    nome = os.path.join(diretorio, nome)
    with open(nome, mode) as file:
         json.dump(dicionario, file)

def append_file(dicionario):
    diretorio = 'Escolas'
    
    nome = input("Qual o nome do arquivo? (sem símbolos especiais, acentuações e espaços.) ") + '.json'
    nome = os.path.join(diretorio, nome)
    
    if os.path.exists(nome):
        materia = input("Qual matéria você quer alterar? ")


create_dir()
modo = choose_mode()
dicionario = create_dict()
acess_file(dicionario, modo)


# if os.path.exists(nome):
        
        with open(nome, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(dicionario) 
        
        with open(nome, mode) as file:
            json.dump(existing_data, file)
        
            

