'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                Até 5 Kg      Acima de 5 Kg
Morango   R$ 2,50 por Kg     R$ 2,20 por Kg
Maçã      R$ 1,80 por Kg     R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

# ENTRADA
def main():
    morangos = float(input('Quantidade de morangos em Kg: '))
    maçãs = float(input('Quantidade de maçãs em Kg: '))
    compra(morangos, maçãs)
    print(f'O valor a ser pago pela compra é R$ {compra(morangos, maçãs):.2f} .')

# PROCESSAMENTO
def compra(m1, m2):
    valor = morango(m1) + maçã(m2)
    if m1 + m2 > 8 or valor > 25:
        desconto = (valor * 10) / 100
        total = valor - desconto
        return total
    else:
        return valor

def morango(m):
    if m <= 5:
        valor = m * 2.50
        return valor
    else:
        valor = (2.50 * 5) + ((m - 5) * 2.20)
        return valor

def maçã(m):
    if m <= 5:
        valor = m * 1.80
        return valor
    else:
        valor = (1.80 * 5) + ((m - 5) * 1.50)
        return valor

# SAÍDA
main()
