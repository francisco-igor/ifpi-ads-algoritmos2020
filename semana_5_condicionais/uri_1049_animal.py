def main():
    tipo1 = input()
    tipo2 = input()
    tipo3 = input()

    animal = tipo(tipo1, tipo2, tipo3)
    print(animal)

def tipo(tipo1, tipo2, tipo3):
    if tipo1 == 'vertebrado':
        if tipo2 == 'ave':
            if tipo3 == 'carnivoro':
                animal = 'aguia'
            elif tipo3 == 'onivoro':
                animal = 'pomba'
        elif tipo2 == 'mamifero':
            if tipo3 == 'onivoro':
                animal = 'homem'
            elif tipo3 == 'herbivoro':
                animal = 'vaca'
    elif tipo1 == 'invertebrado':
        if tipo2 == 'inseto':
            if tipo3 == 'hematofago':
                animal = 'pulga'
            elif tipo3 == 'herbivoro':
                animal = 'lagarta'
        elif tipo2 == 'anelideo':
            if tipo3 == 'hematofago':
                animal = 'sanguessuga'
            elif tipo3 == 'onivoro':
                animal = 'minhoca'
    return animal

main()
