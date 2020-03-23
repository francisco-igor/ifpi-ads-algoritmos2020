'''Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
seguinte.'''

# ENTRADA
def main():
    hora_i = int(input('Hora do início: '))
    minutos_i = int(input('Minutos do início: '))

    hora_f = int(input('Hora do final: '))
    minutos_f = int(input('Minutos do final: '))

    saber_hora(hora_i, minutos_i, hora_f, minutos_f)

# PROCESSAMENTO
def saber_hora(hora_i, minutos_i, hora_f, minutos_f):
    if hora_i >= hora_f:
        hora_f = hora_f + 24

    m_t_i = hora_i * 60 + minutos_i
    m_t_f = hora_f * 60 + minutos_f

    duração_h = (m_t_f - m_t_i) // 60
    duração_m = (m_t_f - m_t_i) % 60
    
    print(f'O jogo durou {duração_h}h e {duração_m}min.')

# SAÍDA
main()
