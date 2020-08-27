'''Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
· 1, 2, 3 = voto para os respectivos candidatos;
· 9 = voto nulo;
· 0 = voto em branco;
Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
a) total de votos para cada candidato;
b) total de votos nulos;
c) total de votos em branco;
d) quem venceu a eleição.'''

# ENTRADA
def main():
    n = int(input('Número de eleitores: '))
    
    print('-' * 100)
    votos(n)

# PROCESSAMENTO
def votos(n):
    primeiro = 0
    segundo = 0
    terceiro = 0
    nulo = 0
    branco = 0

    cont = 1
    while cont <= n:
        codigo = int(input('Código do candidato: '))

        if codigo == 1:
            primeiro = primeiro + 1
        elif codigo == 2:
            segundo = segundo + 1
        elif codigo == 3:
            terceiro = terceiro + 1
        elif codigo == 9:
            nulo = nulo + 1
        elif codigo == 0:
            branco = branco + 1

        cont = cont + 1

    if primeiro > segundo and primeiro > terceiro and primeiro > nulo and primeiro > branco:
        vencedor = 'Candidato 1'
    elif segundo > primeiro and segundo > terceiro and segundo > nulo and segundo > branco:
        vencedor = 'Candidato 2'
    elif terceiro > segundo and terceiro > primeiro and terceiro > nulo and terceiro > branco:
        vencedor = 'Candidato 3'
    else:
        vencedor = 'Ninguém'
        
    print('-' * 100)
    print(f'Primeiro Candidato: {primeiro} voto(s)')
    print(f'Segundo Candidato:  {segundo} voto(s)')
    print(f'Terceiro Candidato: {terceiro} voto(s)')
    print(f'Votos Nulos:        {nulo} voto(s)')
    print(f'Votos em Branco:    {branco} voto(s)')
    print(f'O vencedor da eleição foi: - {vencedor}')
    print('-' * 100)

# SAÍDA
main()
