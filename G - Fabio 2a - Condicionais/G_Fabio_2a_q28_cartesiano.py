'''Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
não pode ser negativo.'''

# ENTRADA
def main():
    x = int(input('Digite a coordenada x: '))
    y = int(input('Digite a coordenada y: '))
    area(x, y)

# PROCESSAMENTO
def area(x, y):
    a = x * y
    if a > 0:
        print(f'A área do retângulo é de {a}m².')
    else:
        print('O valor da área não pode ser negativo.')

# SAÍDA
main()
