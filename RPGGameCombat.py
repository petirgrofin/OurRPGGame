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

    def __init__(self, original_stun_resistance, original_bleed_duration):

        self.enemy_is_stunned = None
        self.original_stun_resistance = original_stun_resistance

        self.enemy_is_bleeding = None
        self.original_bleed_duration = original_bleed_duration
        self.accumulative_bleed_damage = 0  # initial value, MainClasses.chosen_class.base_bleed_damage is added later

    def stuns_check(self):

        MainClasses.chosen_class.stun_debuffs()

        self.enemy_is_stunned = False
        probability = random.randint(0, 100)

        if MainClasses.chosen_class.stun_capable_attack:

            if MainClasses.chosen_class.stun_chance > Enemies.random_enemy.stun_resist:

                if probability < MainClasses.chosen_class.stun_chance - Enemies.random_enemy.stun_resist:
                    self.enemy_is_stunned = True
                    Enemies.random_enemy.stun_resist += 50

                else:
                    print("Stun failed because the enemy resisted")

        return self.enemy_is_stunned

    def bleed_check(self):

        MainClasses.chosen_class.bleed_debuffs()

        probability = random.randint(0, 100)

        if MainClasses.chosen_class.bleed_capable_attack:

            print("A bleed capable attack was chosen")

            if MainClasses.chosen_class.bleed_chance > Enemies.random_enemy.bleed_resist:

                if probability < MainClasses.chosen_class.bleed_chance - Enemies.random_enemy.bleed_resist:

                    self.enemy_is_bleeding = True

                else:
                    print("The enemy resisted against the hemorrhage")
            else:
                print("Bleed ineffective because enemy bleed resistance is too high")

    def poison_check(self):
        pass


def combat():

    Enemies.random_enemy.enemy_choose()

    debuffs = Debuffs(Enemies.random_enemy.stun_resist, MainClasses.chosen_class.bleed_duration)

    enemy_name = Enemies.random_enemy.enemy_name

    character_health_total = MainClasses.chosen_class.picked_class_health
    character_defense = MainClasses.chosen_class.picked_class_defense

    enemy_health_left = Enemies.random_enemy.picked_enemy_health

    print(f"You are fighting against the {enemy_name}")

    while character_health_total > 0:

        MainClasses.chosen_class.attack_choose(input("Select an attack: "))  # choose an attack

        if MainClasses.chosen_class.chosen_attack is None:
            print("Invalid attack")
            continue

        print(f"You have dealt {MainClasses.chosen_class.chosen_attack} damage")

        debuffs.stuns_check()
        debuffs.bleed_check()

        if debuffs.enemy_is_stunned:

            print("The enemy is stunned, and will skip a turn.")

            if debuffs.enemy_is_bleeding:  # since stunning skips a turn, have to check and apply bleed damage here

                if MainClasses.chosen_class.bleed_duration > 0:
                    print(
                        f"The enemy is bleeding, and will take {debuffs.accumulative_bleed_damage} damage for {MainClasses.chosen_class.bleed_duration} turns")

                MainClasses.chosen_class.bleed_duration -= 1
                enemy_health_left -= debuffs.accumulative_bleed_damage + MainClasses.chosen_class.chosen_attack

                if MainClasses.chosen_class.bleed_duration < 0:
                    print("The enemy has stopped bleeding")
                    debuffs.enemy_is_bleeding = False
                    MainClasses.chosen_class.bleed_duration = debuffs.original_bleed_duration

                if enemy_health_left < 0:
                    print(f"The {enemy_name} has died")
                    break

            else:
                enemy_health_left -= MainClasses.chosen_class.chosen_attack

            if enemy_health_left < 0 or 0:
                print(f"The {enemy_name} has died")
                break
            print(f"The enemy has {enemy_health_left} health left")
            continue

        if debuffs.enemy_is_bleeding:

            if MainClasses.chosen_class.bleed_capable_attack:  # accumulative property
                debuffs.accumulative_bleed_damage += MainClasses.chosen_class.base_bleed_damage

            if MainClasses.chosen_class.bleed_duration > 0:
                print(
                    f"The enemy is bleeding, and will take {debuffs.accumulative_bleed_damage} damage for {MainClasses.chosen_class.bleed_duration} turns")

            MainClasses.chosen_class.bleed_duration -= 1
            enemy_health_left -= debuffs.accumulative_bleed_damage

            if MainClasses.chosen_class.bleed_duration < 0:
                print("The enemy has stopped bleeding")
                debuffs.enemy_is_bleeding = False

            if enemy_health_left < 0:
                print(f"The {enemy_name} has died")
                break

        if not debuffs.enemy_is_stunned:  # enemy turn

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

            if Enemies.random_enemy.stun_resist != debuffs.original_stun_resistance:
                Enemies.random_enemy.stun_resist -= 50

            if not debuffs.enemy_is_bleeding:
                debuffs.accumulative_bleed_damage = 0  # initial value

    else:

        print("You have lost")
