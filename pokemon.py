class Pokemon:
    def __init__(self, pokeId = 0):
        self.id = pokeId
        self.name = 'Pikachu'
        self.lvl = 1
        self.exp = 0
        self.atk = 10
        self.hp = 10
        self.defence = 5
        self.attribute1 = 'Lightning'
        self.attribute2 = ''
    def lvlup(self):
        self.lvl += 1

    def showLvl(self):
        print(self.lvl)

Pikachu = Pokemon(15)

Pikachu.showLvl()

Pikachu.lvlup()

Pikachu.showLvl()
    
    
    
