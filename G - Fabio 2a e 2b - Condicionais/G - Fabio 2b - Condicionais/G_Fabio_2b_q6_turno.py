'''Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

# ENTRADA
def main():
    t = str(input('Em que turno você estuda? '))
    turno(t)

# PROCESSAMENTO
def turno(t):
    if t == 'M':
        print('Bom Dia!')
    elif t == 'V':
        print('Boa Tarde!')
    elif t == 'N':
        print('Boa Noite')
    else:
        print('Valor Inválido.')

# SAÍDA
main()
