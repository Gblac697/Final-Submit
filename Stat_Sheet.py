class chara_trait: #charaters stats
    def __init__ (self, health, arm):
        self.health = health
        self.arm = arm
        self.inventory = []
    def is_alive(self): #life 
        return self.health > 0
    def arm_pump(self, axe): #axe bonus
     if axe in self.inventory:
         self.arm += axe.stregth 
         
    def route(self, map):
        if map in self.inventory:
            print("You have found da Way!")
        else:
            print("You are lost")
            pass
    
       
            

player_one = chara_trait(100,10)
old_man = chara_trait(100,10)
water_dragon = chara_trait(150,20)

#class for items
class items_used:
    def __init__(self, stregth, weight, speed, ):
        self.stregth = stregth
        self.weight = weight
        self.speed = speed 

map = items_used(1,1,10,)
rope = items_used(2,2,5)
boat = items_used(20,10,12)
axe = items_used(5,5,3)
boards = items_used(1,1,1)
berries = items_used(.5,.1,2)

    