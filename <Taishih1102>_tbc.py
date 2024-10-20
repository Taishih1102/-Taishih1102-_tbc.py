import random

class Character:
    def __init__(self, name = "Anonymnus", hitPoints = 0, hitChance = 0, maxDamage = 0, armor = 0 ):
        super().__init__()
        self.__name = name
        self.__hitPoints = hitPoints
        self.__hitChance = hitChance
        self.__maxDamage = maxDamage
        self.__armor = armor

    @ property
    def name(self):
        return self.__name

    @name.setter
    def name (self,value):
        self.__name = value

    @ property
    def hitPoints(self):
        return self.__hitPoints

    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = value
            
    @ property
    def hitChance(self):
        return self.__hitChance

    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = value
            
    @ property
    def maxDamage(self):
        return self.__maxDamage

    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = value
            
    @ property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value
             

    def printStats(self):
        print(f"\n{self.name}")
        print("≡" * 20)
        print(f"Hit points: {self.__hitPoints}")
        print(f"Hit chance: {self.__hitChance}%")
        print(f"Max damage: {self.__maxDamage}")
        print(f"Armor:      {self.__armor}")
        
        
class Fight:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster

    def attack(self, attacker, defender):
        chance = random.randint(1, 100)
        if chance <= attacker.hitChance:
            damage = random.randint(1, attacker.maxDamage)
            absorbed = min(defender.armor,damage)
            finalDamage = damage - absorbed
            defender.hitPoints = defender.hitPoints - finalDamage
            if attacker.name == "Student":
                print (f"\n{attacker.name} skipped the lecture...")    
                print(f"{attacker.name} hits {defender.name} for {damage} points of damage")
                print(f"{defender.name}'s armor absorbs {absorbed} points\n")
            if attacker.name == "Professor":
                print (f"\n{attacker.name} gave out an assignment...")
                print(f"{attacker.name} hits {defender.name} for {damage} points of damage")
                print(f"{defender.name}'s armor absorbs {absorbed} points")
        else:
            print(f"{attacker.name} missed the attack!")
            
    def fightscene(self):

        print("\n\nThe battle between the student and the professor have been perpetuating since the emergence of the educational system.")
        print("Today is the day to put an end to the never-ending conflict.")
        input("\n Press to start the game: \n")
        
        keepGoing = True
        while keepGoing:
            
            self.attack(self.hero, self.monster)
            if self.monster.hitPoints <= 0:
                print(f"\n{self.monster.name} is defeated! {self.hero.name} wins!")
                keepGoing = False
                
            if keepGoing:
                self.attack(self.monster, self.hero)
                if self.hero.hitPoints <= 0:
                    print(f"\n{self.hero.name} is defeated! {self.monster.name} wins!")
                    keepGoing = False

            print(f"\n{self.hero.name}: {self.hero.hitPoints} HP")
            print(f"{self.monster.name}: {self.monster.hitPoints} HP")

            input("\nPress Enter for another round: \n")
            print("≡"* 60)
            print("")


def main():
    hero = Character()
    hero.name = "Student"
    hero.hitPoints = 15
    hero.hitChance = 55
    hero.maxDamage = 5
    hero.armor = 2

    monster = Character("Professor", 30, 35, 6, 0)

    hero.printStats()
    monster.printStats()
    
    game = Fight(hero,monster)
    game.fightscene()
    
if __name__ == "__main__":
    main()
    
