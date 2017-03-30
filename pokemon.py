class Pokemon:
    def __init__(self, pokeId = 0):
        pokemonlista = open('pokemonlista.txt',"r")
        line = pokemonlista.readlines()[pokeId].split()
        pokemonlista.close

        attributes = line[4].split("/")
        
        self.id = pokeId
        self.name = line[3]
        self.lvl = 1
        self.experience = 0
        self.attack = line[6]
        self.hp = line[5]
        self.defence = line[7]
        self.attribute1 = attributes[0]
        self.spAttack = line[8]
        self.spDefence = line[9]
        self.speed = line[10]
        
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
        return '#' + pokeId + ', ' + self.name + ' Attributes: ' + self.attribute1 + '/' + self.attribute2 + ', Level: ' + str(self.lvl) + ', Attack: ' + str(self.attack) + ', Defence: ' + str(self.defence)
from random import randint




    

pokemon = Pokemon(randint(1,151))



pokemon.lvlup()

print(pokemon.getInfo())


        

    
    
    
