import random
from unidecode import unidecode


def jogar():

    def bem_vindo():
        print("************************************", end="\n")
        print('Bem vindo ao jogo de forca !', end='\n')
        print("************************************", end="\n\n")

    def definir_palavra_secreta():
        escolher_palavra = open('palavras.txt', 'r', encoding='utf-8')
        palavras = escolher_palavra.read().split('\n')
        escolher_palavra.close()

        return palavras[random.randrange(0, 30)]
    
    def perdeu():
        print('Que pena, voce perdeu !', end="\n\n")
        print('A palavra secreta era: ', palavra_secreta, sep="", end="\n\n")

    bem_vindo()

    palavra_secreta = definir_palavra_secreta()
    forcas = 7

    # display = ('{} ' * len(palavra_secreta)).format(*('_ ' * len(palavra_secreta)).split()).split()  # ['_', '_', ...]
    display = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        
        escolha = int(input('O que voce quer fazer ?\n(1) Chutar uma letra\n(2) Adivinhar a palavra secreta\n'))

        if (escolha == 1):
            chute = unidecode(input('Digite uma letra: '))

            index_palavra_secreta = 0
            letras_encontradas = []
            acerto = False
            for letra in palavra_secreta:
                if (unidecode(letra.lower()) == chute.lower()):
                    letras_encontradas.append(index_palavra_secreta)
                    acerto = True
                index_palavra_secreta += 1
            if (acerto):
                for index in letras_encontradas:
                    display[index] = palavra_secreta.capitalize()[index]
                print(*display)
            else:
                forcas -= 1
                print('A letra {} nao existe na palavra secreta !\nForca: {}'.format(chute, forcas))
                print(*display)
            if (not forcas):
                perdeu()
                enforcou = True
        elif (escolha == 2):
            palavra_usuario = input('Digite a palavra: ')
            if (palavra_secreta.lower() == palavra_usuario.lower()):
                print('Parabens ! Voce ganhou !!!')
                acertou = True
            else:
                perdeu()
                enforcou = True
        else:
            print('Escolha uma opcao valida !')

    print('Fim do jogo !')

if (__name__ == '__main__'):
    jogar()
