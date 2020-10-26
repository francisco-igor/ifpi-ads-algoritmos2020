# ENTRADA
def main():
    msg = input('Mensagem: ')
    cod = int(input('Código: '))
    
    encriptador(msg, cod)

# PROCESSAMENTO
def encriptador(m, c):
    texto = ''
    for unidade in m:
        if letra(unidade):
            rotacionar = rotate_word(unidade, c)
            texto = texto + rotacionar
        else:
            texto = texto + unidade
    
    print(f'A mensagem criptografada é: {texto}')

def rotate_word(s, p):
    simbolo = ord(s)
    novo = simbolo + p
    if maiuscula(s) and novo > 90:
        novo = novo - 26
    
    if minuscula(s) and novo > 122:
        novo = novo - 26
    
    simbolo_rotacionado = chr(novo)
    return simbolo_rotacionado

def letra(s):
    if maiuscula(s) or minuscula(s):
        return s

def maiuscula(s):
    if ord(s) >= 65 and ord(s) <= 90:
        return s

def minuscula(s):
    if ord(s) >= 97 and ord(s) <= 122:
        return s

# SAÍDA
main()
