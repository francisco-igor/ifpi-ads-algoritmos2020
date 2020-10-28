# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

# ENTRADA
dias = int(input('Leia uma idade em dias: '))

# PROCESSAMENTO
anos = dias // 365
meses = (dias % 365) // 30
dias = (dias % 365) % 30

# SAÍDA
print(f'A idade total é de {anos} ano(s), {meses} mês(meses) e {dias} dia(s).')
