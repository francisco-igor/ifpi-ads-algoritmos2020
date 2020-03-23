'''Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45² = 2025.'''

# ENTRADA
def main():
    num = int(input('Número a ser verificado: '))
    esp(num)

# PROCESSAMENTO
def esp(num):
    if 1000 < num < 9999:
        mc = num // 100
        du = num % 100
        third = mc + du
        if third ** 2 == num:
            print('O número é especial!')
        else:
            print('O número é comum!')
    else:
        print('O número é comum!')

# SAÍDA
main()
