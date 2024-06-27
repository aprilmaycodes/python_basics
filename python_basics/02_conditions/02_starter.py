pikachu = {
    'name': 'Pikachu',
    'type': 'Electric',
    'hp': 35,
    'evolution': True
    }

gengar = {
    'name': 'Gengar',
    'type': 'Ghost/Poison',
    'hp': 60,
    'evolution': True
    }

paras = {
    'name': 'Paras',
    'type': 'Bug/Grass',
    'hp': 35,
    'evolution': False
    }

pokedex = {'pikachu': pikachu, 'gengar': gengar, 'paras': paras}

choice = input('Which pokemon would you like to learn about? Pikachu, gengar, or paras?').lower()

req_info = input('What info would you like to know? Name, type, hp, or evolution? ').lower()

answer = pokedex[choice][req_info]
print(f"The information you requested is: {answer}")