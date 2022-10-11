from corrente import Corrente
conta1 = Corrente(3134,'Paulo Plinio', 545)

conta1.alterarNome('Paulo')
conta1.deposito(120)
conta1.saque(60)
print('\nSaldo R$',conta1.saldo)

