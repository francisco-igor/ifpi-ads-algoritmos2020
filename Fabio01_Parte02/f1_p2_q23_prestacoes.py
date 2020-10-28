# Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a cada uma das duas prestações; estas devem ser iguais, inteiras e as maiores possíveis. Por exemplo, se o valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais a R$ 90,00; se o valor da mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00. Escreva um algoritmo que receba o valor da mercadoria e forneça o valor da entrada e das duas prestações, de acordo com as regras acima.

# ENTRADA
valor = float(input('Qual o preço do produto (R$): '))

# PROCESSAMENTO
prestacao1 = valor // 3

prestacao2 = prestacao1

entrada = valor - (prestacao1 + prestacao2)

# SAÍDA
cupom = 9 * ' ' + '**** Nota ****\n'
cupom += '----'*8
cupom += f'\nValor da Entrada: R$ {entrada:.2f}'
cupom += f'\nValor da 1ª Prestação: R$ {prestacao1:.2f}'
cupom += f'\nValor da 2ª Prestação: R$ {prestacao2:.2f}'
print(cupom)
