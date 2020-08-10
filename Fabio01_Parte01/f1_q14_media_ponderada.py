# ENTRADA
nota1 = int(input('Valor da 1ª nota: '))
peso1 = int(input('Peso da 1ª nota: '))

nota2 = int(input('Valor da 2ª nota: '))
peso2 = int(input('Peso da 2ª nota: '))

nota3 = int(input('Valor da 3ª nota: '))
peso3 = int(input('Peso da 3ª nota: '))

# PROCESSAMENTO
soma_das_notas = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
soma_dos_pesos = peso1 + peso2 + peso3

média_ponderada = soma_das_notas / soma_dos_pesos

# SAÍDA
print('A média ponderada das notas do aluno é de {:.1f}'.format(média_ponderada))
