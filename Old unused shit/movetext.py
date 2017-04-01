import codecs

source = codecs.open('dump.txt','r','utf-8')
lines = source.readlines()
source.close()

lista = []
lista.append('Line\tLevel\tTarget')
index = 0
i = 6
j = 1
balle = 0
k = 4
kuk = 7
while k < 564:
    index = lines[k].find('#') + 1
    index1 = lines[j].find('#') + 1
    if kuk < 564:
        if lines[kuk][25:-6] == '':
            lista.append(str(int(lines[j][index1:(index1 + 3)])) + '\t' + lines[i][19:-6] + '\t' + str(int(lines[k][index:(index + 3)])))
    k += 9
    balle += 1
    kuk += 9
    i += 9
    j += 9
grej = ''
cp = 1
with open('pokemonlista.txt','r') as src:
    with open('pokemonlista1.txt','w') as target:
        for line in src:
            if line[:4] == 'Name':
                target.write(line)
                continue
            if cp < len(lista):
                if int(lista[cp].split()[0]) == int(line.split()[1][1:]):
                    rad = lista[cp].split()
                    grej = line[:-1] + rad[1] + '\t' + rad[2] + '\n'
                    cp += 1
                else:
                    grej = line[:-1] + ' \t \n'
            else:
                grej = line[:-1] + ' \t \n'
            target.write(grej)
            




