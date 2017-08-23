class Pokemon:
    
    def __init__(self, lines, pokeId):
        line = lines[pokeId].split()

        attributes = line[4].split("/")
        
        self.id = line[1]
        self.name = line[3]
        self.renamed = False
        self.lvl = 1
        self.experience = 0
        self.attribute1 = attributes[0]
        
        self.baseAttack = line[6]
        self.baseHp = line[5]
        self.baseDefence = line[7]
        self.baseSpAttack = line[8]
        self.baseSpDefence = line[9]
        self.baseSpeed = line[10]

        if len(line) > 12:
            self.evolutionLevel = line[12]
            self.evolutionTarget = line[13]
        else:
            evolutionLevel = ''
            evolutionTarget = ''

        grejer = 1

        self.attack = self.baseAttack * grejer
        self.hp = self.baseHp * grejer
        self.defence = self.baseAttack * grejer
        self.spAttack = self.baseSpAttack * grejer
        self.spDefence = self.baseSpDefence * grejer
        self.speed = self.baseSpeed * grejer
        
        if len(attributes) > 1:
            self.attribute2 = attributes[1]
        else:
            self.attribute2 = ''


    def __init__(self, lines, name):
        i = 0
        for line in lines:
            if line.split()[0] == name.lower():
                break
            elif i >= 151:
                i = 1
            else:
                i += 1
            
            
        
        line = lines[i].split()

        attributes = line[4].split("/")
        
        self.id = line[1]
        self.name = line[3]
        self.lvl = 1
        self.experience = 0
        self.attribute1 = attributes[0]
        self.renamed = False
        
        self.baseAttack = line[6]
        self.baseHp = line[5]
        self.baseDefence = line[7]
        self.baseSpAttack = line[8]
        self.baseSpDefence = line[9]
        self.baseSpeed = line[10]
        if len(line) > 12:
            self.evolutionLevel = line[12]
            self.evolutionTarget = line[13]
        else:
            self.evolutionLevel = ''
            self.evolutionTarget = ''

        grejer = 1

        self.attack = self.baseAttack * grejer
        self.hp = self.baseHp * grejer
        self.defence = self.baseAttack * grejer
        self.spAttack = self.baseSpAttack * grejer
        self.spDefence = self.baseSpDefence * grejer
        self.speed = self.baseSpeed * grejer
        
        if len(attributes) > 1:
            self.attribute2 = attributes[1]
        else:
            self.attribute2 = ''
        
    def lvlup(self):
        self.lvl += 1
            
    def getInfo(self):
        i = 3 - len(str(self.id))
        pokeId = ''
        while i > 0:
            pokeId += '0'
            i -= 1
        pokeId += str(self.id)
        
        if self.attribute2 != '':
            attributes = self.attribute1 + '/' + self.attribute2
        else:
            attributes = self.attribute1
            
        return pokeId + ', ' + self.name + '\nAttributes: ' + attributes + '\nLevel: ' + str(self.lvl) + '\nAttack: ' + str(self.attack) + '\nDefence: ' + str(self.defence) + '\nSpecial attack: ' + str(self.spAttack) + '\nSpecial defence: ' + str(self.spDefence) + '\nSpeed: ' + self.speed

    def rename(self, name):
        self.name = name
        self.renamed = True

    def evolve(self,lines):
        if self.evolutionTarget != '':
            line = lines[int(self.evolutionTarget)].split()
            attributes = line[4].split('/')
                
            self.id = line[1]
            if self.renamed == False:
                self.name = line[3]
            self.lvl = 1
            self.experience = 0
            self.attribute1 = attributes[0]
            if len(attributes) > 1:
                self.attribute2 = attributes[1]
        
            self.baseAttack = line[6]
            self.baseHp = line[5]
            self.baseDefence = line[7]
            self.baseSpAttack = line[8]
            self.baseSpDefence = line[9]
            self.baseSpeed = line[10]
            if len(line) > 12:
                self.evolutionLevel = line[12]
                self.evolutionTarget = line[13]
            else:
                self.evolutionLevel = ''
                self.evolutionTarget = ''
        
            grejer = 1
        
            self.attack = self.baseAttack * grejer
            self.hp = self.baseHp * grejer
            self.defence = self.baseAttack * grejer
            self.spAttack = self.baseSpAttack * grejer
            self.spDefence = self.baseSpDefence * grejer
            self.speed = self.baseSpeed * grejer
        else:
            print('Pokemon cannot evolve')
        

#Test shit, not part of class

from random import randint
pokemonlista = open('pokemonlista.txt',"r")
lines = pokemonlista.readlines()
pokemonlista.close()

while True:
    pokemon = Pokemon(lines,input('Skriv en pokemon: '))
    pokemon.evolve(lines)
    print(pokemon.getInfo())
    
    





        

    
    
    
