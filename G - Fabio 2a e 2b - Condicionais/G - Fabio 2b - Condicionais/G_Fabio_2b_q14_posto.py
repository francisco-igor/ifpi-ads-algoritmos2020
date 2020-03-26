'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
1. Álcool:
· até 20 litros, desconto de 3% por litro
· acima de 20 litros, desconto de 5% por litro
2. Gasolina:
· até 20 litros, desconto de 4% por litro
· acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

# ENTRADA
def main():
    A = float(input('Quantos litros de álcool: '))
    G = float(input('Quantos litros de gasolina: '))
    
    print(f'O preço a ser pago pelo álcool é R$ {desc_al(A):.2f} e o preço', end=' ')
    print(f'a ser pago pela gasolina é R$ {desc_gas(G):.2f}.')

# PROCESSAMENTO
def desc_al(a):
    p = 1.90
    if a <= 20:
        '''Calcula o valor já descontado'''
        desconto_por_litro = p - ((p * 3) / 100)
        desconto = desconto_por_litro * a
        return desconto
    elif a > 20:
        desconto_por_litro2 = p - ((p * 5) / 100)
        desconto = ((p - ((p * 3) / 100)) * 20) + (desconto_por_litro2 * (a - 20))
        return desconto

def desc_gas(g):
    p = 2.50
    if g <= 20:
        desconto_por_litro = p - ((p * 4) / 100)
        desconto = desconto_por_litro * g
        return desconto
    elif g > 20:
        desconto_por_litro2 = p - ((p * 6) / 100)
        desconto = ((p - ((p * 4) / 100)) * 20) + (desconto_por_litro2 * (g - 20))
        return desconto

# SAÍDA
main()
