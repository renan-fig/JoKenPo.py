from random import randint
from time import sleep

print('='*7, 'BEM-VINDO AO JO-KEN-PO', '='*7)
start = str(input('Digite "start" para iniciar:'))
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)

while start == 'start':
    print('SUAS OPÇÕES:')
    print('[ 1 ] PEDRA')
    print('[ 2 ] PAPEL')
    print('[ 3 ] TESOURA')
    user = int(input('Qual será sua jogada?'))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('<=>'*10)
    if pc == 0:
        if user == 1:
            print('EMPATE!!')
        elif user == 2:
            print(' \33[1;32mVOCÊ VENCEU!!')
        elif user == 3:
            print('\33[1;31mVOCÊ PERDEU!!')
    elif pc == 1:
        if user == 1:
            print('\33[1;31mVOCÊ PERDEU!!')
        elif user == 2:
            print('EMPATE!!')
        elif user == 3:
            print(' \33[1;32mVOCÊ VENCEU!!')
    elif pc == 2:
        if user == 1:
            print(' \33[1;32mVOCÊ VENCEU!!')
        elif user == 2:
            print('\33[1;31mVOCÊ PERDEU!!')
        elif user == 3:
            print('EMPATE!!')
    stop = str(input('Deseja continuar? (sim/não)'))
    if stop == 'não':
        break;


