class Pokemon:
    
    def __init__(self, lines, pokeId):
        line = lines[pokeId].split()


        attributes = line[4].split("/")
        
        self.id = line[1]
        self.name = line[3]
        self.lvl = 1
        self.experience = 0
        self.attribute1 = attributes[0]
        
        self.baseAttack = line[6]
        self.baseHp = line[5]
        self.baseDefence = line[7]
        self.baseSpAttack = line[8]
        self.baseSpDefence = line[9]
        self.baseSpeed = line[10]

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

    def evolve(self, lines):
        pokeId = int(self.id[:1]) - 1
        

        
        

#Test shit, not part of class

from random import randint
pokemonlista = open('pokemonlista.txt',"r")
lines = pokemonlista.readlines()
pokemonlista.close()

pokemon = Pokemon(lines, randint(1,151))
pokemon.lvlup()
print(pokemon.getInfo())



        

    
    
    
