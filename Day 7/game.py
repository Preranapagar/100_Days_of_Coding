from actors import *
import random

def print_header():
    print('_'*100)
    print(' '*40 + "Wizard Game")
    print('_'*100)
    print()

def game_loop():
    creatures =[
        Creature('Bat',5),
        Creature('Toad',1),
        Creature('Tiger',12),
        Dragon('Black Dragon', 50, scaliness = 2, breaths_fire = False),
        Wizard('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True :

        active_creature = random.choice(creatures)

        print("A {} of level {} has appear from dark and foggy forest..."
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print("The wizard defeated {}".format(active_creature.name))
            else:
                print("The Wizard has been defeated by the powerful {}".format(active_creature.name))

        elif cmd == 'r':
            print("The wizard has become unsure of his power and flees !!")

        elif cmd =='l':
            print("The wizard {} takes in the surrounding and sees:".format(hero.name))
            for c in creatures:
                print("* {} of level {}".format(c.name,c.level))

        else:
            print("Okay! existing Game!!")
            break

        if not creatures:
            print("You have defeated all the creatures, well done !")
            break

        print()

def main():
    print_header()
    game_loop()

if __name__ =="__main__":
    main()