from pessoa import Pessoa

p1 = Pessoa('Luiz', 29, 75.5, 1.80)
p2 = Pessoa('João', 32, 80, 1.95)

print(p1.envelhecendo(2))
print(p1.emagrecendo(2))
print(p1.engordando(2))
print(p1.crescendo(0.6))

print(p2.envelhecendo(2))
print(p2.emagrecendo(2))
print(p2.engordando(2))
print(p2.crescendo(0.6))

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
