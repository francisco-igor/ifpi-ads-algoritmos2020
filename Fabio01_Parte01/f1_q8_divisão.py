# ENTRADA
numero1 = int(input('Valor de um número: '))
numero2 = int(input('Valor de outro número: '))

# PROCESSAMENTO
soma = numero1 + numero2
subtração = numero1 - numero2
divisão = soma / subtração

# SAÍDA
print('O valor da divisão da soma pela subtração dos números {} e {} é de {:.0f}'.format(numero1, numero2, divisão))
