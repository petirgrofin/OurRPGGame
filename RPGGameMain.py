import RPGGameCombat as Combat
import MainCharacterClasses as MainClasses


def introduction():
    confirm_class_question = input("Do you wish to continue?: ")
    if confirm_class_question == "yes":
        character_name = input("Choose your character's name: ")
        print(f"Your character will be named {character_name}")
        tutorial_question = input("Do you wish to see the tutorial?: ")
        if tutorial_question == "yes".lower():
            Combat.tutorial()
        elif tutorial_question == "no".lower():
            Combat.combat()


MainClasses.chosen_class.class_choose(input("Select a class: "))
print("Hello, welcome to my game.")
introduction()
