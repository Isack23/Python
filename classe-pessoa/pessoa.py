from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, peso, altura):
       self.nome = nome
       self.idade = idade
       self.peso = peso
       self.altura = altura

    def envelhecendo(self, anos):
        self.anos = anos
        print(f'{self.nome} envelheceu ', anos, ' anos. A idade atual é', self.idade, 'anos')

    def engordando(self,pesagem):
        self.peso += pesagem
        print(f'{self.nome} engordou',pesagem, 'kg. O peso atual é', (self.peso), 'kg')

    def emagrecendo(self,pesagem):
        self.peso -= pesagem
        print(f'{self.nome} emagreceu ', pesagem, 'kg. O peso atual é', (self.peso), 'kg')

    def crescendo(self,anos):
        self.idade += anos
        if self.idade < 21:
            crescimento = 0.05*anos
            self.altura += crescimento
            print(f'{self.nome} cresceu ', crescimento, 'm. A altura atual é', round(self.altura), 'm')
        else:
            print(f'{self.nome}', 'não cresceu')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
