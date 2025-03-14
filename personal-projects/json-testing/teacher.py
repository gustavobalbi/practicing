#Code developed to practice concepts related to .json and dictionaries. This system allows a teacher to register classes, students, and their respective grades. Incomplete.

import os, shutil, json

def create_dir():
    try:
        os.mkdir('Schools')
    except FileExistsError:
        pass

def choose_mode():
    answ = int(input("Create/Overwrite file or add information to an existing one? \n[1] - CREATE/OVERWRITE \n[2] - ADD \n-> "))
    if answ == 1:
        mode = 'w'
    else:
        mode = 'a'

    return mode

def create_dict():
    qtd = int(input("Enter how many classes you have. "))
    subjects = {}
    count = 0

    while count < qtd:
        subject = input("Enter the name of the subject. ")
        students_dict = {}
        students = int(input("Enter the number of students enrolled. "))
        for i in range(students):
            name = input('Enter the full name of the student. ')
            grades = []
            for j in range(3):
                grade = float(input(f'Enter the grade for the {j+1}st EVALUATION of {name.split()[0].upper()}. '))
                grades.append(grade)

            students_dict[name] = grades
        
        subjects[subject] = students_dict

        count += 1
    
    return subjects

def create_file(dictionary):
    directory = 'Schools'

    name = input("What will be the name of the file? (no special symbols, accents, or spaces.) ") + '.json'
    name = os.path.join(directory, name)
    with open(name, mode) as file:
         json.dump(dictionary, file)

def append_file(dictionary):
    directory = 'Schools'
    
    name = input("What is the name of the file? (no special symbols, accents, or spaces.) ") + '.json'
    name = os.path.join(directory, name)
    
    if os.path.exists(name):
        subject = input("Which subject would you like to alter? ")


create_dir()
mode = choose_mode()
dictionary = create_dict()
acess_file(dictionary, mode)


""" if os.path.exists(name):
        
        with open(name, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(dictionary) 
        
        with open(name, mode) as file:
            json.dump(existing_data, file)"""

        
            

