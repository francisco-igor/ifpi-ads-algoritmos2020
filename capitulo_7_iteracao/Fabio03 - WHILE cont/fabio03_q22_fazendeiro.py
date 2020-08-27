'''Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
numero de identificação e o peso do boi mais magro e do boi mais gordo.'''

# ENTRADA
def main():
    f = int(input('Informe o número de fichas: '))

    print('-' * 30)
    fichas(f)

# PROCESSAMENTO
def fichas(f):
    
    mais_gordo = 0
    mais_magro = 10000
    cont = 1

    while cont <= f:
        cod = int(input('Informe o número: '))
        peso = int(input('Informe o peso: '))
        print('-' * 25)
    
        if peso > mais_gordo:
            mais_gordo = peso
            cod_gordo = cod

        if peso < mais_magro:
            mais_magro = peso
            cod_magro = cod

        cont = cont + 1

    print('-' * 48)
    print(f'Número de identificação: {cod_gordo} \nPeso do boi mais gordo: {mais_gordo} Kg')
    print('-' * 48)
    print(f'Número de identificação: {cod_magro} \nPeso do boi mais magro: {mais_magro} Kg')
    print('-' * 48)

# SAÍDA
main()
