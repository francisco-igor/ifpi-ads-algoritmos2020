'''Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
escreva o quadrado dos números lidos.'''

# ENTRADA
def main():
    variavel1 = int(input('Digite um número inteiro: '))
    variavel2 = int(input('Digite um número inteiro: '))
    multicalc(variavel1, variavel2)

# PROCESSAMENTO
def multicalc(variavel1, variavel2):
    if variavel1 % variavel2 == 1:
        soma = variavel1 + variavel2 + (variavel1 % variavel2)
        print(f'O valor da soma dos números com o resto da divisão é {soma}.')
        
    elif variavel1 % variavel2 == 2:
        if variavel1 % 2 == 0:
            print('O primeiro número é par.')
        else:
            print('O primeiro número é ímpar.')
        if variavel2 % 2 == 0:
            print('O segundo número é par.')
        else:
            print('O segundo número é ímpar.')
            
    elif variavel1 % variavel2 == 3:
        calculo = (variavel1 + variavel2) * variavel1
        print(f'O valor obtido pela soma dos números multiplicada pelo primeiro foi {calculo}.')
        
    elif variavel1 % variavel2 == 4: 
        if variavel2 != 0:
            divisao = (variavel1 + variavel2) / variavel2
            print(f'A divisão da soma dos termos pelo segundo é {divisao}.')
        else:
            print('O segundo termo é zero, o que invalida a operação.')
    else:
        print(f'O quadrado dos números é {variavel1 ** 2} e {variavel2 ** 2}.')

# SAÍDA
main()
