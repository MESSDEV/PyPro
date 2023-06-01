from random import randint
 
class Hero():
    def __init__(self, name, health, armor, power):
       self.name = name
       self.health = health
       self.armor = armor
       self.power = power
       self.new = True
    #printing character info:
    def print_info(self):
       print('Health level:', self.health)
       print('Armor class:', self.armor)
   
    #check if the character is alive
    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False
   
    #striking:
    def strike(self, enemy):
       enemy.armor -= self.power
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
 
class Warrior(Hero):
    def hello(self):
        if self.new:
            print('-> NEW HERO! A skilled warrior appears from the forest depths', self.name )
            self.new = False
        else:
            print('The martial', self.name, 'appears again')
   
    #method for displaying a text description of the attack on the screen
    def attack(self, enemy):
        print(self.name , 'fearlessly pounces on', enemy.name )
        print('The fight outcome for', self.name )
        self.print_info()
        print('The fight outcome for', enemy.name )
        enemy.print_info()
 
class Dragon(Hero):
    def hello(self):
        if self.new:
            print('-> NEW HERO! The fierce dragon', self.name, ' descends from the sky')
            self.new = False
        else:
            print('Once again the furious dragon', self.name, 'appears before us')
   
    def attack(self, enemy):
        print(self.name , 'directs a stream of deadly fire at', enemy.name )
        print('The fight outcome for', self.name )
        self.print_info()
        print('The fight outcome for', enemy.name )
        enemy.print_info()
 
knight = Warrior('Richard', 50, 25, 20)
print('Hail to thee, good knight', knight.name )
print('You are standing at the entrance to the forest full of deadly dangers. Are you ready to go there and fight the enemies (yes/no)?')
answer = input()
if answer == 'yes':
    play = True
    print('\n***Let the fight begin!*** \n')
else:
    play = False
 
enemies = list()
enemies.append(Warrior('Peter', 15, 0, 10))
enemies.append(Warrior('Sergio', 10, 15, 5))
enemies.append(Dragon('Drogon', 1, 25, 60))
enemies.append(Dragon('Viserion', 1, 10, 30))
 
while play:
    #we determine who the knight will fight with
    #we take the length of the list as an index, because after killing enemies, the list will shrink  
    enemy = enemies[randint(0,len(enemies)-1)]
    enemy.hello()
    enemy.print_info()
 
    is_attack = input('Join the fight (yes/no)?')
    if is_attack == 'yes':
        if randint(0,1) == 1:
            fighters = [knight, enemy]
        else:
            fighters = [enemy, knight]
        fighters [0].strike(fighters[1])
        fighters [0].attack(fighters[1])
    print('---')
 
    #check if the current enemy is dead and if so, remove them from the list
    if enemy.check_alive() == False:
        print(enemy.name , 'died by hand of', knight.name, '\n')
        enemies.remove(enemy)
   
    #we check the conditions of the game end (the Knight died or all the enemies were killed)
    if knight.check_alive() == False:
        print('The brave knight', knight.name , 'died in battle with enemies')
        play = False
    if len(enemies) == 0:
        print('The brave Knight', knight.name , 'defeated all the enemies!')
        play = False
print('That is the end of the fairy tale')
