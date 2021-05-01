import MainCharacterClasses as MainClasses
import RPGGameEnemies as Enemies
import random


def tutorial():
    print("All classes have 2 attacks: attack1, and attack2.")
    print("To input an attack, simply say attack1 or attack2.")
    print("The enemy will attack you too. If your health goes down to 0, you'll lose.")
    print("If the enemy health goes down to 0, the enemy will die.")
    print("You can debuff an enemy, but this mechanic depends on several factors.")
    print("Try it yourself:")

    combat()


class Debuffs:

    def __init__(self):
        self.enemy_stun_resistance_increased = None

    def stuns_check(self):
        MainClasses.chosen_class.stun_debuffs()
        enemy_is_stunned = False
        if MainClasses.chosen_class.stun_capable_attack:
            if MainClasses.chosen_class.stun_chance > Enemies.random_enemy.stun_resist and random.randint(0, 100) > MainClasses.chosen_class.stun_chance - Enemies.random_enemy.stun_resist:
                print("The enemy is stunned, and will skip a turn.")
                enemy_is_stunned = True
                Enemies.random_enemy.stun_resist += 50
                self.enemy_stun_resistance_increased = True

            elif MainClasses.chosen_class.stun_chance > Enemies.random_enemy.stun_resist and random.randint(0, 100) > MainClasses.chosen_class.stun_chance - Enemies.random_enemy.stun_resist and self.enemy_stun_resistance_increased:
                print("The enemy was stunned again, and will skip a turn.")
                enemy_is_stunned = True
                Enemies.random_enemy.stun_resist += 50
            else:
                print("Stun failed")
                if self.enemy_stun_resistance_increased:
                    Enemies.random_enemy.stun_resist -= 50
                    self.enemy_stun_resistance_increased = False

        return enemy_is_stunned

    def bleed_check(self):
        pass

    def poison_check(self):
        pass


def combat():

    debuffs = Debuffs()

    Enemies.random_enemy.enemy_choose()
    enemy_name = Enemies.random_enemy.enemy_name

    character_health_total = MainClasses.chosen_class.picked_class_health
    character_defense = MainClasses.chosen_class.picked_class_defense

    enemy_health_left = Enemies.random_enemy.picked_enemy_health

    print(f"You are fighting against the {enemy_name}")

    while character_health_total > 0:

        MainClasses.chosen_class.attack_choose(input("Select an attack: "))  # choose an attack
        print(f"You have dealt {MainClasses.chosen_class.chosen_attack} damage")

        if debuffs.stuns_check():
            enemy_health_left -= MainClasses.chosen_class.chosen_attack
            if enemy_health_left < 0 or 0:
                print(f"The {enemy_name} has died")
                break
            print(f"The enemy has {enemy_health_left} health left")
            continue

        else:  # enemy turn

            enemy_health_left -= MainClasses.chosen_class.chosen_attack

            if enemy_health_left < 0 or 0:
                print(f"The {enemy_name} has died")
                break

            print(f"The enemy has {enemy_health_left} health left")

            Enemies.random_enemy.enemy_attack_chooser()

            character_health_total -= Enemies.random_enemy.enemy_attack - character_defense

            print(
                f"The {enemy_name} has dealt {Enemies.random_enemy.enemy_attack - character_defense} damage with his {Enemies.random_enemy.enemy_attack_name}")
            print(f"You have {character_health_total} health left")

    else:
        print("You have lost")
