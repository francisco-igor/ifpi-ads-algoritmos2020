'''Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
sobre os dois valores lidos.'''

# ENTRADA
def main():
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    valor3 = int(input('Digite um número entre 1 e 4: '))
    operação(valor1, valor2, valor3)

# PROCESSAMENTO
def operação(valor1, valor2, valor3):
    if 1 > valor3 or valor3 > 4:
        print('O número da operação não é válido.')
    elif valor3 == 1:
        soma = valor1 + valor2
        print(f'O resultado da soma dos valores é {soma}.')
    elif valor3 == 2:
        subtração = valor1 - valor2
        print(f'O resultado da subtração dos valores é {subtração}.')
    elif valor3 == 3:
        multiplicação = valor1 * valor2
        print(f'O resultado da multiplicação dos valores é {multiplicação}.')
    elif valor3 == 4:
        divisão = valor1 / valor2
        print(f'O resultado da divisão dos valores é {divisão}.')

# SAÍDA
main()
