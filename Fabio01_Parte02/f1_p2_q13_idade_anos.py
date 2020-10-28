# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

# ENTRADA
anos = int(input('Leia uma idade em anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

# PROCESSAMENTO
dias_total = anos * 365 + meses * 30 + dias

# SAÍDA
print(f'A idade total em dias é {dias_total}.')
