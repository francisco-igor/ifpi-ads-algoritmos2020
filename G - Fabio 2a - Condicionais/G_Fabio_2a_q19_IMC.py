'''Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea (IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).'''

# ENTRADA
def main():
    altura = float(input('Qual a sua altura em metros: '))
    peso = float(input('Qual o seu peso em Kg: '))
    imc(altura, peso)

# PROCESSAMENTO
def imc(altura, peso):
    IMC = peso / altura ** 2
    if peso > 0:
        if IMC < 25:
            print('Seu peso está normal.')
        elif 25 <= IMC <= 30:
            print('Você está obeso.')
        else:
            print('Você está com obesidade mórbida.')

# SAÍDA
main()
