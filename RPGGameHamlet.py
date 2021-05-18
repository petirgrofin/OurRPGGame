import MainCharacterClasses as MainClasses
import RPGGameLocations as Locations
import RPGGameCombat as Combat


class Hamlet:

    def hamlet_introduction(self):

        print("Welcome to the old hamlet, once prosperous, now in ruins. Your mission is to end with the Beast, whose\n"
              "name is unknown, and power unmeasurable. You may attempt to kill the Beast at any given moment, but \n"
              "doing so poses a great risk. You must be prepared.")
        print(
            "You may visit 4 other locations, all which hold a powerful king that treasures an ancient tablet written"
            "\n "
            "in strange languages, that will give you more information about the Beast and how to defeat it")
        print(
            "You can retreat from quests in any given moment: losing a battle will signify a scar to your character,\n"
            "that can only be cured through careful and lengthy meditation and treatment")
        print(
            "In the hamlet, you may upgrade your abilities, which will upgrade your critical chance and boost damage \n")
        print(
            "You may also engage in training with certain captured enemies to try different strategies and attacks \n")
        print("If you want to check this introduction during your stay at the hamlet, simply input help")

    def hamlet_general(self):

        moving_through_hamlet = input(">")
        if moving_through_hamlet == "guild":
            print("Welcome to the guild")
            hamlet.hamlet_guild()
        elif moving_through_hamlet == "sanatorium":
            print("Welcome to the sanatorium")
        elif moving_through_hamlet == "training room":
            print("Welcome to the training room")
        elif moving_through_hamlet == "world locations":
            hamlet.world_locations()

    def hamlet_guild(self):

        upgrading_attacks_price = {

            "apprentice_level_attack_upgrade_price": 50

        }

        attacks = {keys: values for keys, values in MainClasses.Mage.mage_attacks.items()}

        print("You have the following attacks: ")

        for key, value in attacks.items():
            print(str(key) + ", damage: " + str(value))

        upgrading_skills = MainClasses.chosen_class.attack_choose(input("Choose a skill to upgrade, or exit the guild: "))

        while True:
            if upgrading_skills == "attack1":
                print(f"This upgrade will cost you {upgrading_attacks_price['apprentice_level_attacks_upgrade_price']} pieces of gold. Do you wish to continue?")
                if upgrading_skills == "yes" and MainClasses.chosen_class.gold_pieces > upgrading_attacks_price["apprentice_level_attack_upgrade_price"]:
                    upgrading_skills += 100
                    print(f"Your skill has been upgraded, and it now has {upgrading_skills[0]} damage")
                elif MainClasses.chosen_class.gold_pieces < upgrading_attacks_price["apprentice_level_attack_upgrade_price"]:
                    print("You currently don't have enough gold pieces to upgrade this skill")
                    continue
            elif upgrading_skills == "exit" or "quit" or "break":
                print("You are exiting the guild")
                break

        hamlet.hamlet_general()

    def world_locations(self):

        print("There are four dangerous locations, plagued by dark and treacherous monsters, whose sole purpose is to"
              "corrupt what these lands once were.")
        print("You are tasked to kill every monster in the dungeons, the swamps, the caverns and the castle,"
              "with the hope of bringing a slight glimmer of prosperity to the lands once well regarded.")
        print("These abhorrent beasts grow ever stronger, and you must put an end to their feasts of"
              "madness and bloodshed.")

        location_choose = input("Where do you want to go?: ")
        if location_choose == "The Caverns":
            the_caverns = Locations.TheCaverns("apprentice level mission", MainClasses.chosen_class.picked_class_health)
            the_caverns.first_mission()


hamlet = Hamlet()

