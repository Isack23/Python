#arquivo = open("arquivo.txt")
#ret = arquivo.read()
#print(type(ret))
#print(ret)

#arquivo = open('novoarquivo.txt','w')
#arquivo.write('Um novo texto \n')
#arquivo.write('Adicionar uma nova linha\n')
#arquivo.close()

with open('frutas.txt', 'w') as arquivo:
    while True:
        time = input('informe seu time de futebol: ')
        if time != 'sair':
            arquivo.write(time)
            arquivo.write('\n')
        else:
            break