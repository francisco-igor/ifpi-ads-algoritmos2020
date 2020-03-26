'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
          Até 5 Kg          Acima de 5 Kg
Filé      R$ 4,90 por Kg    R$ 5,80 por Kg
Alcatra   R$ 5,90 por Kg    R$ 6,80 por Kg
Picanha   R$ 6,90 por Kg    R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

# ENTRADA
def main():
    carne = str(input('Informe o tipo de carne: '))
    quant = float(input('Informe a quantidade em Kg: '))
    cartão = str(input('Pretende usar o cartão Tabajara na compra do produto: '))
    
    nome_carne(carne)
    valor_carne(carne, quant)
    cartao(cartão)
    desconto(valor_carne(carne, quant), cartao(cartão))
    valor_descontado(valor_carne(carne, quant), cartao(cartão))

    print('-'*45)
    print('-'*15,'Cupom Fiscal','-'*16)
    print('-'*45)
    print(f'Tipo e quantidade de carne: {nome_carne(carne)} {quant} kg')
    print(f'Preço total do produto: R$ {valor_carne(carne, quant):.2f}')
    print(f'Tipo de pagamento: {cartao(cartão)}')
    print(f'Valor do desconto: R$ {desconto(valor_carne(carne, quant), cartao(cartão)):.2f}')
    print(f'Valor a pagar: R$ {valor_descontado(valor_carne(carne, quant), cartao(cartão)):.2f}')
    print('-'*45)

# PROCESSAMENTO
def nome_carne(a):
    if a == 'file' or a == 'filé' or a == 'Filé':
        return 'Filé'
        
    elif a == 'alcatra' or a == 'alcatara':
        return 'Alcatra'
        
    elif a == 'picanha':
        return 'Picanha'

def valor_carne(t, q):
    ''' Determina o valor dos produtos. '''
    if t == 'file' or t == 'filé':
        if q <= 5:
            valor = q * 4.90
            return valor
        else:
            valor = (4.90 * 5) + ((q - 5) * 5.80)
            return valor
    
    elif t == 'alcatra' or t == 'alcatara':
        if q <= 5:
            valor = q * 5.90
            return valor
        else:
            valor = (5.90 * 5) + ((q - 5) * 6.80)
            return valor
    
    elif t == 'picanha':
        if q <= 5:
            valor = q * 6.90
            return valor
        else:
            valor = (6.90 * 5) + ((q - 5) * 7.80)
            return valor

def cartao(c):
    ''' Define se o cliente escolheu pagar com cartão Tabajara ou não. '''
    if c == 'sim':
        return 'Cartão Tabajara'
    elif c == 'não' or 'nao':
        return 'Dinheiro'

def desconto(valor, cartão):
    ''' Determina o valor do desconto dependendo da forma de pagamento do cliente. '''
    if cartão == 'Cartão Tabajara':
        desconto = (valor * 5) / 100
        return desconto
    else:
        return 0

def valor_descontado(valor, cartão):
    if cartão == 'Cartão Tabajara':
        desconto = (valor * 5) / 100
        total = valor - desconto
        return total
    else:
        return valor

# SAÍDA
main()
