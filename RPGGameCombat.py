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

    combat("Tutorial", 1)

class CharacterDebuffs:

    def __init__(self, character_original_stun_resistance):

        self.character_is_stunned = None

        self.character_original_stun_resistance = None

        self.character_is_bleeding = None
        self.dot_bleed = None

    def character_stuns_check(self):

        Enemies.random_enemy.enemy_stun_debuff(self)

        self.character_is_stunned = False
        probability = random.randint(0, 100)

class Debuffs:

    def __init__(self, first_enemy_original_stun_resistance, additional_enemy_original_stun_resistance):

        self.first_enemy_is_stunned = None
        self.second_enemy_is_stunned = None

        self.first_enemy_original_stun_resistance = first_enemy_original_stun_resistance
        self.additional_enemy_original_stun_resistance = additional_enemy_original_stun_resistance

        self.first_enemy_is_bleeding = None
        self.second_enemy_is_bleeding = None

        self.enemy_resisted_bleed = None

    def stuns_check(self, stun_target):

        MainClasses.chosen_class.stun_debuffs()

        self.first_enemy_is_stunned = False
        self.second_enemy_is_stunned = False
        probability = random.randint(0, 100)

        if MainClasses.chosen_class.stun_capable_attack:

            if stun_target == Enemies.random_enemy.enemy_name:

                if MainClasses.chosen_class.stun_chance > Enemies.random_enemy.stun_resist:

                    if probability < MainClasses.chosen_class.stun_chance - Enemies.random_enemy.stun_resist:

                        self.first_enemy_is_stunned = True
                        Enemies.random_enemy.stun_resist += 50

                    else:
                        print(f"Stun failed because the {Enemies.random_enemy.enemy_name} resisted")

            elif stun_target == Enemies.random_enemy.additional_enemy_name:

                if MainClasses.chosen_class.stun_chance > Enemies.random_enemy.additional_enemy_stun_resist:

                    if probability < MainClasses.chosen_class.stun_chance - Enemies.random_enemy.additional_enemy_stun_resist:
                        self.second_enemy_is_stunned = True
                        Enemies.random_enemy.additional_enemy_stun_resist += 50
                    else:
                        print(f"Stun failed because the {Enemies.random_enemy.additional_enemy_name} resisted")

            return self.first_enemy_is_stunned

    def bleed_check(self, bleed_target):

        MainClasses.chosen_class.bleed_debuffs()

        probability = random.randint(0, 100)

        if MainClasses.chosen_class.bleed_capable_attack:

            print("A bleed capable attack was chosen")

            if bleed_target == Enemies.random_enemy.enemy_name:

                if MainClasses.chosen_class.bleed_chance > Enemies.random_enemy.bleed_resist:

                    if probability < MainClasses.chosen_class.bleed_chance - Enemies.random_enemy.bleed_resist:

                        self.first_enemy_is_bleeding = True
                        self.enemy_resisted_bleed = False

                    else:
                        print("The enemy resisted against the hemorrhage")
                        self.enemy_resisted_bleed = True
                else:
                    print("Bleed ineffective because enemy bleed resistance is too high")

            elif bleed_target == Enemies.random_enemy.additional_enemy_name:

                if MainClasses.chosen_class.bleed_chance > Enemies.random_enemy.additional_enemy_bleed_resist:

                    if probability < MainClasses.chosen_class.bleed_chance - Enemies.random_enemy.additional_enemy_bleed_resist:

                        self.second_enemy_is_bleeding = True

                    else:
                        print("The enemy resisted against the hemorrhage")
                else:
                    print("Bleed ineffective because enemy bleed resistance is too high")

    def poison_check(self):
        pass


def combat(enemy_group, enemy_number):

    select_who_to_attack = any
    targeted_enemy_name = None
    targeted_first_enemy = None
    targeted_additional_enemy = None
    debuffs = None
    additional_enemy_is_dead = None
    first_enemy_is_dead = None
    bleed_dot_duration_for_first_enemy = None
    bleed_dot_duration_for_second_enemy = None
    have_to_register_bleed_properties = True
    bleed_dot_damage_first_enemy = 0
    bleed_dot_damage_second_enemy = 0
    first_enemy_is_stunned = None
    second_enemy_is_stunned = None
    character_dead = False

    if enemy_group == "Tutorial":

        Enemies.random_enemy.enemy_choose()

    elif enemy_group == "Cavern" or "Caverns":

        Enemies.random_enemy.cavern_enemy_choose()

    elif enemy_group == "Castle":

        Enemies.random_enemy.castle_enemy_choose()

    elif enemy_group == "Swamp":

        Enemies.random_enemy.swamp_enemy_choose()

    if enemy_number == 1:

        debuffs = Debuffs(Enemies.random_enemy.stun_resist, None)

    elif enemy_number == 2:

        debuffs = Debuffs(Enemies.random_enemy.stun_resist, Enemies.random_enemy.additional_enemy_stun_resist)

    first_enemy_name = Enemies.random_enemy.enemy_name
    additional_enemy_name = Enemies.random_enemy.additional_enemy_name

    character_health_total = MainClasses.chosen_class.picked_class_health
    character_defense = MainClasses.chosen_class.picked_class_defense

    enemy_health_left = Enemies.random_enemy.picked_enemy_health
    additional_enemy_health_left = Enemies.random_enemy.additional_enemy_health

    if enemy_number == 1:

        print(f"You are fighting against the {first_enemy_name}")

    elif enemy_number == 2:

        print(f"You are fighting against the {first_enemy_name} and the {additional_enemy_name}")

    while character_health_total > 0:

        if enemy_number == 1:

            MainClasses.chosen_class.attack_choose(input("Select an attack: "))  # choose an attack

            targeted_enemy_name = first_enemy_name

        elif enemy_number == 2:

            select_who_to_attack = input("Who do you wish to attack?: ")

            if select_who_to_attack == first_enemy_name:

                MainClasses.chosen_class.attack_choose(input("Select an attack: "))

                targeted_enemy_name = first_enemy_name

                targeted_first_enemy = True
                targeted_additional_enemy = False

            elif select_who_to_attack == additional_enemy_name:

                MainClasses.chosen_class.attack_choose(input("Select an attack: "))

                targeted_enemy_name = additional_enemy_name

                targeted_additional_enemy = True
                targeted_first_enemy = False

            else:
                select_who_to_attack = None

        if MainClasses.chosen_class.chosen_attack is None or select_who_to_attack is None:
            print("Invalid input")
            continue

        print(f"You have dealt {MainClasses.chosen_class.chosen_attack} damage to the {targeted_enemy_name}")

        debuffs.stuns_check(targeted_enemy_name)

        debuffs.bleed_check(targeted_enemy_name)

        if debuffs.first_enemy_is_stunned or debuffs.second_enemy_is_stunned:

            print(f"The {targeted_enemy_name} is stunned, and will skip a turn.")

            if targeted_first_enemy:
                enemy_health_left -= MainClasses.chosen_class.chosen_attack
                first_enemy_is_stunned = True

            elif targeted_additional_enemy:
                additional_enemy_health_left -= MainClasses.chosen_class.chosen_attack
                second_enemy_is_stunned = True

        if debuffs.first_enemy_is_bleeding:

            if have_to_register_bleed_properties:
                bleed_dot_duration_for_first_enemy = MainClasses.chosen_class.bleed_duration
                bleed_dot_duration_for_second_enemy = MainClasses.chosen_class.bleed_duration
                have_to_register_bleed_properties = False

            if MainClasses.chosen_class.bleed_capable_attack and not debuffs.enemy_resisted_bleed:  # accumulative property

                if targeted_first_enemy:
                    bleed_dot_damage_first_enemy += MainClasses.chosen_class.base_bleed_damage
                    bleed_dot_duration_for_first_enemy = MainClasses.chosen_class.bleed_duration
                    debuffs.first_enemy_is_bleeding = True

                elif targeted_additional_enemy:
                    bleed_dot_damage_second_enemy += MainClasses.chosen_class.base_bleed_damage
                    bleed_dot_duration_for_second_enemy = MainClasses.chosen_class.bleed_duration
                    debuffs.second_enemy_is_bleeding = True

            if bleed_dot_duration_for_first_enemy == 0 and not first_enemy_is_dead:
                print(f"The {Enemies.random_enemy.enemy_name} has stopped bleeding")
                debuffs.first_enemy_is_bleeding = False
                bleed_dot_duration_for_first_enemy = MainClasses.chosen_class.bleed_duration
                bleed_dot_damage_first_enemy = MainClasses.chosen_class.base_bleed_damage

            elif bleed_dot_duration_for_second_enemy == 0 and not additional_enemy_is_dead:
                print(f"The {Enemies.random_enemy.additional_enemy_name} has stopped bleeding")
                debuffs.second_enemy_is_bleeding = False
                bleed_dot_duration_for_second_enemy = MainClasses.chosen_class.bleed_duration
                bleed_dot_damage_second_enemy = MainClasses.chosen_class.base_bleed_damage

            if debuffs.first_enemy_is_bleeding and bleed_dot_duration_for_first_enemy != 0 and not first_enemy_is_dead:
                print(
                    f"The {first_enemy_name} is bleeding, and will take {bleed_dot_damage_first_enemy} damage for {bleed_dot_duration_for_first_enemy} turns")

            if debuffs.second_enemy_is_bleeding and bleed_dot_duration_for_second_enemy != 0 and not additional_enemy_is_dead:
                print(
                    f"The {additional_enemy_name} is bleeding, and will take {bleed_dot_damage_second_enemy} damage for {bleed_dot_duration_for_second_enemy} turns")

            if debuffs.first_enemy_is_bleeding and bleed_dot_duration_for_first_enemy != 0:
                enemy_health_left -= bleed_dot_damage_first_enemy
                bleed_dot_duration_for_first_enemy -= 1

            if debuffs.second_enemy_is_bleeding and bleed_dot_duration_for_second_enemy != 0:
                additional_enemy_health_left -= bleed_dot_damage_second_enemy
                bleed_dot_duration_for_second_enemy -= 1

            if not debuffs.second_enemy_is_bleeding and not debuffs.first_enemy_is_bleeding:
                have_to_register_bleed_properties = True

        if enemy_number > 1:

            if targeted_first_enemy:  # enemy turn

                enemy_health_left -= MainClasses.chosen_class.chosen_attack

            elif targeted_additional_enemy:

                additional_enemy_health_left -= MainClasses.chosen_class.chosen_attack

        elif enemy_number == 1:

            enemy_health_left -= MainClasses.chosen_class.chosen_attack
            if enemy_health_left < 0:
                print(f"The {first_enemy_is_dead} has died")
                break
            print(f"The {first_enemy_name} has {enemy_health_left} health left")

        if enemy_health_left < 0 and not first_enemy_is_dead:  # check if first enemy is dead
            print(f"The {first_enemy_name} has died")
            first_enemy_is_dead = True

        if enemy_number > 1 and additional_enemy_health_left < 0 and not additional_enemy_is_dead:  # check if second enemy is dead
            print(f"The {additional_enemy_name} has died")
            additional_enemy_is_dead = True

        if additional_enemy_is_dead and first_enemy_is_dead:  # check if both dead
            print("You have killed the enemies")
            break

        if enemy_number > 1 and not first_enemy_is_dead and not additional_enemy_is_dead:
            print(
                f"The {first_enemy_name} has {enemy_health_left} health left, and the {additional_enemy_name} has {additional_enemy_health_left} health left")

        elif enemy_number > 1 and not first_enemy_is_dead:
            print(f"The {first_enemy_name} has {enemy_health_left} health left")

        elif enemy_number > 1 and not additional_enemy_is_dead:
            print(
                f"The {additional_enemy_name} has {additional_enemy_health_left} health left")

        Enemies.random_enemy.enemy_attack_chooser()

        if not first_enemy_is_stunned and not first_enemy_is_dead:

            character_health_total -= Enemies.random_enemy.enemy_attack - character_defense

            print(
                f"The {first_enemy_name} has dealt {Enemies.random_enemy.enemy_attack - character_defense} damage with his {Enemies.random_enemy.enemy_attack_name}")

        if not second_enemy_is_stunned and not additional_enemy_is_dead:

            character_health_total -= Enemies.random_enemy.additional_enemy_attack - character_defense

            if enemy_number > 1:
                print(
                    f"The {additional_enemy_name} has dealt {Enemies.random_enemy.additional_enemy_attack - character_defense} damage with his {Enemies.random_enemy.additional_enemy_attack_name}")

        print(f"You have {character_health_total} health left")

        if Enemies.random_enemy.stun_resist != debuffs.first_enemy_original_stun_resistance and not first_enemy_is_stunned:
            Enemies.random_enemy.first_enemy_original_stun_resistance -= 50

        if Enemies.random_enemy.stun_resist != debuffs.additional_enemy_original_stun_resistance and not second_enemy_is_stunned:
            Enemies.random_enemy.additional_enemy_stun_resist -= 50

    else:

        print("You have lost")
        character_dead = True
    return character_dead
