import os
import random


# Trabalhar com uma lista de inteiros e nao string de numeros na hora do sorteio e verificar se eh possivel otimizar essa bagaça, e testar o limpa tela em 100%
def limpa_Tela():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def cria_log(jogador, pontuacao):
    arquivo = open("data_jogadores.txt", "a")
    arquivo.write(jogador + "\n")
    arquivo.write(str(pontuacao) + "\n")
    arquivo.close()


def analisa_log(pontuacao,jogador):
    with open("data_jogadores.txt", "r") as arquivo:
        x = arquivo.read()
        y = x.splitlines()
        i = 0
        while i < len(y):
            if i % 2 != 0:
                if pontuacao < int(y[i]):
                    pontuacao = int(y[i])
                    jogador = y[i - 1]
            i += 1
    return pontuacao,jogador


def genius(jogador, maior_pontuacao):
    numero = random.randint(0, 9)
    jogada = str(numero)
    print("O numero sorteado foi:", numero)
    sequencia = input("Digite o numero desse round:")
    while sequencia == jogada:
        numero = random.randint(0, 9)
        jogada = jogada + str(numero)
        limpa_Tela()
        print("Novo numero :", numero)
        sequencia = input("Digite a sequencia ate agora:")
    print("Errou, errou feio errou rude.")
    pontuacao = len(jogada) - 1
    print("Sua pontuação foi de :", pontuacao)
    if maior_pontuacao < pontuacao:
        maior_pontuacao = pontuacao
    retry = input("Seu jogo acabou deseja tentar novamente? Digite S pra sim e N para nao.")
    if retry == "S":
        genius(jogador,maior_pontuacao)
    else:
        print("Maior pontuação de {} até agora foi de {:.2f}".format(jogador, maior_pontuacao))
        cadastra = cria_log(jogador, maior_pontuacao)
        recorde, top1 = analisa_log(maior_pontuacao,jogador)
        print("O jogador com a maior pontuacao eh {} com {:.2f}".format(top1, recorde))


def main():
    jogador = input("Digite o nome do jogador:")
    maior_pontuacao = 0
    jogo = genius(jogador, maior_pontuacao)


main()
