#VOLTEI! depois de muito tempo sem entrar no
#github eu voltei e agora estou estudando classes e objetos XD

from time import sleep


class CaixaEletronico:
    """
    classe para criação de um sistema de caixa 24 horas
    :param deposito: saldo disponível na conta do usuário, 
    retorna 0 enquanto o usuário não depositar
    """

    def __init__(self, deposito=float(0)):
        self.deposito = deposito

    def verificar_saldo(self):
        """verifica o saldo atual na conta do usuário"""
        if self.deposito > 0:
            print(f'Saldo Atual: R${self.deposito:.2f}')
        else:
            print('Você não tem saldo neste banco!')

    def depositar(self, depositar=float(0), comprovante=False):
        """
        função que deposita o valor escolhido pelo usuário e retorna 0 caso não for informado nada
        :param depositar: valor X que o usuário deseja depositar na conta
        :param comprovante: imprimi o comprovante do depósito caso seja informado True
        """
        self.deposito += depositar
        if comprovante is True:
            print('====== COMPROVANTE ======')
            print(f'Depósito:    R${depositar:.2f}')
            print(f'Saldo Atual: R${self.deposito:.2f}')

    def sacar(self, saque=float(0), taxa=float(0), comprovante=False):
        """
        função para sacar o valor desejado pelo usuário
        :param saque: valor X que o usuário deseja sacar e retorna 0 caso não for informado nada
        :param taxa: taxa X que o usuário devera pagar para fazer o saque do dinheiro no banco desejado, 
        retorna 0 caso o banco não tenha taxa estabelecida
        :param comprovante: imprime um comprovante do saque feito pelo usuário caso seja informado True
        """
        if saque + taxa > self.deposito:
            if taxa >= self.deposito:
                print(
                    f'Saldo insuficiente! Para sacar é preciso ter acima de R${taxa:.2f} na conta!')
            else:
                saldo_antes = self.deposito
                resto = self.deposito - taxa
                self.deposito -= self.deposito
                if comprovante is True:
                    print('====== COMPROVANTE ======')
                    print(f'Saldo de antes: R${saldo_antes}')
                    print(f'Saque:          R${saque:.2f}')
                    print(f'Taxa de saque:  R${taxa:.2f}')
                    print(f'Saque pós taxa: R${resto:.2f}')
                    print(f'Saldo Atual:    R${self.deposito:.2f}')
        elif self.deposito <= 0:
            self.deposito = 0
            print('Você não tem saldo neste banco!')
        else:
            self.deposito -= saque
            self.deposito -= taxa
            if comprovante is True:
                print('====== COMPROVANTE ======')
                print(f'Saque:         R${saque:.2f}')
                print(f'Taxa de saque: R${taxa:.2f}')
                print(f'Saldo Atual:   R${self.deposito:.2f}')


itau = CaixaEletronico()
nubank = CaixaEletronico()
santander = CaixaEletronico()

print('===== BEM VINDO AO CAIXA ELETRÔNICO SANTANDER! =====')
while True:
    print('\n')
    print('''DEPOSITAR
SACAR
SALDO
SAIR''')
    OP = str(input('O que deseja fazer? ')).upper().strip()
    print('\n')

# DEPÓSITO DE DINHEIRO
    if OP == 'DEPOSITAR':
        print('ITAÚ | NUBANK | SANTANDER')
        OPBANCO_DEPOSITO = str(
            input('Em qual banco deseja depositar? ')).upper().strip()
        if OPBANCO_DEPOSITO not in 'ITAU|ITAÚ|NUBANK|SANTANDER':
            print('ERRO! Por Favor, digite uma opção válida!')
        else:
            try:
                opdeposito = float(input('Quanto deseja depositar? R$'))
                COMPROVANTE_D = str(input('Deseja comprovante?[S/N]: ')).upper().strip()

                # BANCO ITAÚ
                if OPBANCO_DEPOSITO == 'ITAU' or OPBANCO_DEPOSITO == 'ITAÚ':
                    if COMPROVANTE_D == 'S':
                        itau.depositar(opdeposito, True)
                    elif COMPROVANTE_D == 'N':
                        itau.depositar(opdeposito)
                    else:
                        print('ERRO! Por Favor, digite uma opção válida!')

                # BANCO NUBANK
                elif OPBANCO_DEPOSITO == 'NUBANK':
                    if COMPROVANTE_D == 'S':
                        nubank.depositar(opdeposito, True)
                    elif COMPROVANTE_D == 'N':
                        nubank.depositar(opdeposito)
                    else:
                        print('ERRO! Por Favor, digite uma opção válida!')

                # BANCO SANTANDER
                elif OPBANCO_DEPOSITO == 'SANTANDER':
                    if COMPROVANTE_D == 'S':
                        santander.depositar(opdeposito, True)
                    elif COMPROVANTE_D == 'N':
                        santander.depositar(opdeposito)
                    else:
                        print('ERRO! Por Favor, digite uma opção válida!')
                else:
                    print('ERRO! Por Favor, digite algo válido!')
            except (ValueError, TypeError):
                print('ERRO! Por Favor, digite algo válido!')

# SAQUE DE DINHEIRO
    elif OP == 'SACAR':
        print('ITAÚ | NUBANK | SANTANDER')
        OPBANCO_SAQUE = str(input('Em qual banco deseja sacar? ')).upper().strip()
        if OPBANCO_SAQUE not in 'ITAU|ITAÚ|NUBANK|SANTANDER':
            print('ERRO! Por Favor, digite algo válido!')
        else:
            try:
                opsaque = float(input('Quanto deseja sacar? R$'))
                COMPROVANTE_S = str(input('Deseja comprovante?[S/N]: ')).upper().strip()

                # BANCO ITAÚ
                if OPBANCO_SAQUE == 'ITAU' or OPBANCO_SAQUE == 'ITAÚ':
                    if COMPROVANTE_S == 'S':
                        itau.sacar(opsaque, 50, True)
                    elif COMPROVANTE_S == 'N':
                        itau.sacar(opsaque, 50)
                    else:
                        print('ERRO! Por Favor, digite uma opção válida!')

                # BANCO NUBANK
                if OPBANCO_SAQUE == 'NUBANK':
                    if COMPROVANTE_S == 'S':
                        nubank.sacar(opsaque, True)
                    elif COMPROVANTE_S == 'N':
                        nubank.sacar(opsaque)
                    else:
                        print('ERRO! Por Favor, digite uma opção válida!')

                # BANCO SANTANDER
                if OPBANCO_SAQUE == 'SANTANDER':
                    if COMPROVANTE_S == 'S':
                        santander.sacar(opsaque, 80, True)
                    elif COMPROVANTE_S == 'N':
                        santander.sacar(opsaque, 80)
                    else:
                        print('ERRO! Por Favor, digite uma opção válida!')
            except (ValueError, TypeError):
                print('ERRO! Por Favor, digite algo válido!')

# SALDO DISPONÍVEL
    elif OP == 'SALDO':
        print('ITAÚ | NUBANK | SANTANDER')
        BANCO_SALDO = str(input('Em qual banco deseja verificar o saldo? ')).upper().strip()
        if BANCO_SALDO == 'ITAU' or BANCO_SALDO == 'ITAÚ':
            itau.verificar_saldo()

        elif BANCO_SALDO == 'NUBANK':
            nubank.verificar_saldo()

        elif BANCO_SALDO == 'SANTANDER':
            santander.verificar_saldo()
        else:
            print('ERRO! Por Favor, digite uma opção válida!')

# SAIR DO SISTEMA
    elif OP == 'SAIR':
        print('Saindo do sistema...')
        sleep(3)
        print('Tenha um bom dia :)')
        break
    else:
        print('ERRO! Por Favor, digite uma opção válida!')
