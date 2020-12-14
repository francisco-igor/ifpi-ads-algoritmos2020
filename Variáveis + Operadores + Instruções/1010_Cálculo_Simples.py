cod1, qtd1, valor1 = input().split(' ')
cod2, qtd2, valor2 = input().split(' ')

total = (int(qtd1) * float(valor1)) + (int(qtd2) * float(valor2))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
