# Imports:
import adivinhacao
import forca

while True:
    print('**************************', end='\n')
    print('Selecione o seu jogo !', end='\n')
    print('**************************', end='\n')

    jogo = int(input('(1) Adivinhacao\n(2) Forca\n(3) Em breve\n'))

    if (jogo == 1):
        adivinhacao.jogar()
        break
    elif (jogo == 2):
        forca.jogar()
        break
    elif (jogo == 3):
        print('jogo disponivel em breve !')
    else:
        print('Jogo nao encontrado ! Tente novamente')