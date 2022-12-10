from random import randint
from modulos_pessoais import cores

comp = randint(1, 3)
# 1 = Pedra, 2 = Papel, 3 = Tesoura

cores.amarelo('Vamos jogar pedra, papel, tesoura? Você começa!')
while True:
    try:
        jog = int(input('Sua opção [1 = Pedra, 2 = Papel, 3 = Tesoura]: '))
    except (ValueError, TypeError):
        cores.amarelo('Por Favor, digite um valor válido!')
    else:
        if jog == 1 and comp == 3 or jog == 2 and comp == 1 or jog == 3 and comp == 2:
            cores.verde('Você Ganhou!')
        elif jog == 3 and comp == 1 or jog == 1 and comp == 2 or jog == 2 and comp == 3:
            cores.vermelho('Você Perdeu!')
        elif jog == comp:
            cores.azul('EMPATE!')
    finally:
        continua = str(input('Quer continuar?[S/N]: ')).upper().strip()
        if continua not in 'SN':
            cores.amarelo('Por Favor, digite um valor válido!')
        else:
            if continua == 'N':
                break
