import random


def jogar():
    print("************************************", end="\n")
    print('Bem vindo ao jogo de adivinhacao !', end='\n')
    print("************************************", end="\n")

    # numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    rodadas = 7

    for c in range(1, rodadas + 1):
        print("Rodada {} de {}".format(c, rodadas))
        numero_usuario = int(input("Digite um Numero: "))

        if (0 > numero_usuario or numero_usuario > 100):
            print('Digite um numero entre 0 e 100 !')
            continue

        # Variaveis
        acertou = numero_usuario == numero_secreto
        maior = numero_usuario > numero_secreto
        menor = numero_usuario < numero_secreto

        if (acertou):
            print("Parabens ! Voce acertou !!!")
            break
        elif (maior and c != rodadas):
            print("O numero secreto e menor !")
        elif (menor and c != rodadas):
            print("O numero secreto e maior !")
        elif (c == rodadas):
            print('Voce perdeu !')
    print('Fim do jogo !')


if (__name__ == '__main__'):
    jogar()
