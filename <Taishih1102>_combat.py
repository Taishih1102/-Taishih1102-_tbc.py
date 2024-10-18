import tbc

def main():
    hero = tbc.Character()
    hero.name = "Student"
    hero.hitPoints = 15
    hero.hitChance = 55
    hero.maxDamage = 5
    hero.armor = 2

    monster = tbc.Character("Professor", 30, 35, 6, 0)

    hero.printStats()
    monster.printStats()

    game = tbc.Fight(hero, monster)
    game.fightscene()

if __name__ == "__main__":
    main()

