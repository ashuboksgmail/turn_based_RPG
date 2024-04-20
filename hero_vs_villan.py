class Hero:
    def __init__(self,name,health,stamina,weapon,is_dead,potion):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.weapon = weapon
        self.is_dead = is_dead
        self.potion = potion

    def attack(self):
         print('Attack')
        
    def use_potions(self):
         print('use potion')
          
    def die(self):
         print('die')
        

class Villan:
    def __init__(self,name,health,stamina,weapon,is_dead):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.weapon = weapon
        self.is_dead = is_dead
        
    def attack(self):
        print('Attack')
                  
    def die(self):
        print('die')
          
                

     

