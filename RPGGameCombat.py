import MainCharacterClasses as MainClasses
import RPGGameEnemies as Enemies


def tutorial():

    print("All classes have 2 attacks: attack1, and attack2.")
    print("To input an attack, simply say attack1 or attack2.")
    print("The enemy will attack you too. If your health goes down to 0, you'll lose.")
    print("If the enemy health goes down to 0, the enemy will die.")
    print("You can debuff an enemy, but this mechanic is entirely random.")
    print("Try it yourself:")

    Enemies.random_enemy.enemy_choose()
    enemy_name = Enemies.random_enemy.enemy_name

    character_health_total = MainClasses.chosen_class.picked_class_health
    character_defense = MainClasses.chosen_class.picked_class_defense

    enemy_health_left = Enemies.random_enemy.picked_enemy_health

    print(f"You are fighting against the {enemy_name}")

    while character_health_total > 0:

        MainClasses.chosen_class.attack_choose(input("Select an attack: "))  # choose an attack
        print(f"You have dealt {MainClasses.chosen_class.chosen_attack} damage")

        MainClasses.chosen_class.stun_debuffs()

        if MainClasses.chosen_class.stun_capable_attack:
            print("The enemy has been stunned!")
            enemy_health_left -= MainClasses.chosen_class.chosen_attack
            if enemy_health_left < 0 or 0:
                print(f"The {enemy_name} has died")
                break
            else:
                print(f"The enemy has {enemy_health_left} health left")
                continue

        else:  # enemy turn

            enemy_health_left -= MainClasses.chosen_class.chosen_attack

            if enemy_health_left < 0 or 0:
                print(f"The {enemy_name} has died")
                print("Now you know the basic mechanics")
                break

            print(f"The enemy has {enemy_health_left} health left")

            Enemies.random_enemy.enemy_attack_chooser()

            character_health_total -= Enemies.random_enemy.enemy_attack - character_defense

            print(f"The {enemy_name} has dealt {Enemies.random_enemy.enemy_attack - character_defense} damage")
            print(f"You have {character_health_total} health left")

    else:
        print("You have lost")


def combat():

    Enemies.random_enemy.enemy_choose()
    enemy_name = Enemies.random_enemy.enemy_name

    character_health_total = MainClasses.chosen_class.picked_class_health
    character_defense = MainClasses.chosen_class.picked_class_defense

    enemy_health_left = Enemies.random_enemy.picked_enemy_health

    print(f"You are fighting against the {enemy_name}")

    while character_health_total > 0:

        MainClasses.chosen_class.attack_choose(input("Select an attack: "))  # choose an attack
        print(f"You have dealt {MainClasses.chosen_class.chosen_attack} damage")

        MainClasses.chosen_class.stun_debuffs()

        if MainClasses.chosen_class.stun_capable_attack:
            print("The enemy has been stunned, and will skip a turn")
            enemy_health_left -= MainClasses.chosen_class.chosen_attack
            if enemy_health_left < 0 or 0:
                print(f"The {enemy_name} has died")
                break
            else:
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

            print(f"The {enemy_name} has dealt {Enemies.random_enemy.enemy_attack - character_defense} damage")
            print(f"You have {character_health_total} health left")

    else:
        print("You have lost")

