# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint 
from time import sleep

nome = str (input('Digite seu nome:'))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print('''Informe a sua OPÇÃO:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')

jogador = int (input('Qual é a sua jogada?'))
print ('JO') 
sleep (1)
print ('KEN') 
sleep (1)
print ('PO !!!!')
sleep (1)

print ('-=' * 12)
print ('O computador escolheu: {}'.format (itens [computador]))
print ('Você escolheu: {}'.format (itens [jogador]))
print ('-=' * 12)

# verificar quem ganhou 

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print ('EMPATOU, TENTE NOVAMENTE.')
    elif jogador == 1:
        print ('PARABÉNS {}, VOCÊ GANHOU!'.format(nome))
    elif jogador == 2:
        print ('O COMPUTADOR GANHOU. TENTE NOVAMENTE.')
    

if computador == 1:                                                                                                                                     
    if jogador == 0: # computador jogou PAPEL 
        print ('O COMPUTADOR VENCEU. TENTE NOVAMENTE.')
    elif jogador == 1:
        print ('EMPATOU, TENTE NOVAMENTE.')
    elif jogador == 2:
        print ('PARABÉNS {}, VOCÊ GANHOU!'.format(nome))
    
        
    
if computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print (' PARABÉNS {}, VOCÊ GANHOU!'.format(nome))
    elif jogador == 1:
        print ('O COMPUTADOR VENCEU. TENTE NOVAMENTE.')
    elif jogador == 2:
        print ('EMPATOU, TENTE NOVAMENTE.')  


    
  






