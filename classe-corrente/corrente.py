class Corrente:
    def __init__(self, num_conta, nome_cliente, saldo):
        self.num_conta = num_conta
        self.nome_cliente = nome_cliente
        self.saldo = saldo

    def alterarNome(self, nome_cliente):
        self.nome_cliente = nome_cliente
        print('\nNome do cliente alterado:', self.nome_cliente)

    def deposito(self, valor):
        self.saldo += valor
        print('\nDeposito realizado no valor de: R$', valor, '\nO saldo atual é de: R$', self.saldo)

    def saque(self, valor):
        self.saldo -= valor
        print('\nSaque realizado no valor de: R$', valor, '\nO saldo atual é de: R$', self.saldo)
