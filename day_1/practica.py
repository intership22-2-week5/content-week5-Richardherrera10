DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 75,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    # 1. obtener todos los desarrolladores de python
    for i in DATA:
      if 'python' in i.values():
        print(i) 
    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    
    python20 = list(filter(lambda person: person['language'] == 'python' and person['age'] > 20,DATA))
    # 3. obtener todos los trabajadores de ciancoders 
    cianCoders = list(filter(lambda person: person['organization'] == 'Ciancoders', DATA))
    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    cianCoders30 = [person for person in DATA if person['organization'] == 'Ciancoders' and person['age']> 30]
   
    # 5. obtener todos los trabajadores de mayores de 18 años
    mayor18 = [person for person in DATA if person['age'] > 18]
    # 6. obtener todos los trabajadores de mayores a 70 años
    mayor70 = [person for person in DATA if person['age'] > 70]
    print(mayor70)
if __name__ == '__main__':
    run()
   