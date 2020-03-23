'''Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.
Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.'''

# ENTRADA
def main():
    num = int(input('Número a ser verificado: '))
    quad_perf(num)

# PROCESSAMENTO
def quad_perf(num):
    dig12 = num // 100
    dig34 = num % 100
    r = num ** (1/2)
    if r % 1 == 0:
        if dig12 + dig34 == r:
            print('O número é um quadrado perfeito.')
        else:
            print('O número não é um quadrado perfeito.')
    else:
        print('O número não é um quadrado perfeito.')

# SAÍDA
main()
