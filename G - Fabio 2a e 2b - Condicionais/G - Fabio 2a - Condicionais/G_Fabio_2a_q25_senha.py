'''Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
uma mensagem de permissão de acesso ou não.'''

# ENTRADA
def main():
    senha = int(input('Senha do usuário: '))
    verificar(senha)

# PROCESSAMENTO
def verificar(senha):
    digito1 = senha // 1000
    digito2 = (senha % 1000) // 100
    digito3 = ((senha % 1000) % 100) // 10
    digito4 = ((senha % 1000) % 100) % 10
      
    if digito1 == 1 and digito2 == 2 and digito3 == 3 and digito4 == 4:
        print('Acesso Permitido!')
    else:
        print('Acesso Negado!')

# SAÍDA
main()
