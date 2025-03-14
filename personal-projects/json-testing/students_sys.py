#Code developed to practice concepts related to .json and dictionaries. This system allows students to register themselves acording to their characteristics. Incomplete.


import os, shutil, json

try:
    os.mkdir('UFPA')
except FileExistsError:
    pass

directory = 'C:/Python/PLN/UFPA'

status = True

while status:

    name = input("Enter your name. ")
    file_name = name.replace(' ', '-') + '.json'

    age = input('Enter your age. ')

    genders = {0: 'Male', 1: 'Female', 2: 'Other'}
    gender = int(input('Enter your gender. \nMALE - [0] \nFEMALE - [1] \nOTHER - [2] \n'))
    if gender in genders:
        gender = genders[gender]

    city = input("Enter your city. ")

    dictionary = {}
    dictionary = [name, age, gender, city]

    file_name = os.path.join(directory, file_name)
    with open(file_name, 'w') as file:
        json.dump(dictionary, file)

    condition = int(input('Add another student? \nYES - [0] \nNO - [1] \n'))
    if condition == 1:
        status = False

