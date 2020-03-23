'''Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
contrario, é arredondado para o inteiro imediatamente inferior.'''

# ENTRADA
def main():
    num = float(input('Escreva um número a ser arredondado: '))
    arredondar(num)

# PROCESSAMENTO
def arredondar(num):
    if num >= (num // 1) + 0.50:
        numero = (num + 1) // 1
        print(f'O número foi arredondado para {numero}')
    else:
        numero = num // 1
        print(f'O número foi arredondado para {numero}')

# SAÍDA
main()
