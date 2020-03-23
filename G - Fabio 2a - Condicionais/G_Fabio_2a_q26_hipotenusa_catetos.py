'''Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.'''

# ENTRADA
def main():
    lado1 = float(input('Primeiro lado: '))
    lado2 = float(input('Segundo lado: '))
    lado3 = float(input('Terceiro lado: '))
    hipotenusa(lado1, lado2, lado3)

# PROCESSAMENTO
def hipotenusa(lado1, lado2, lado3):
    if lado1 > lado2 and lado1 > lado3:
        print('O primeiro lado é a hipotenusa e os outros lados são catetos.')
    elif lado2 > lado1 and lado2 > lado3:
        print('O segundo lado é a hipotenusa e os outros lados são catetos.')
    elif lado3 > lado1 and lado3 > lado2:
        print('O terceiro lado é a hipotenusa e os outros lados são catetos.')

# SAÍDA
main()
