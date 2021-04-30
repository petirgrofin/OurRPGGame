import MainCharacterClasses as MainClasses
import RPGGameEnemies as Enemies


def tutorial():

    print("Welcome to the tutorial")
    print("All classes have 2 attacks: attack1, and attack2")
    print("To input an attack, simply say attack1 or attack2")
    print("God help us")
    print("a")


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

        enemy_health_left -= MainClasses.chosen_class.chosen_attack

        if enemy_health_left < 0:
            print(f"The {enemy_name} has died")
            break

        print(f"The enemy has {enemy_health_left} health left")

        Enemies.random_enemy.enemy_attack_chooser()

        character_health_total -= Enemies.random_enemy.enemy_attack - character_defense

        print(f"The {enemy_name} has dealt {Enemies.random_enemy.enemy_attack - character_defense} damage")
        print(f"You have {character_health_total} health left")

    else:
        print("You have lost")

