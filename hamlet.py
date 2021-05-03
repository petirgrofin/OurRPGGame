import MainCharacterClasses as MainClasses


class Hamlet:

    def hamlet_introduction(self):

        print("Welcome to the old hamlet, once prosperous, now in ruins. Your mission is to end with the Beast, whose\n"
              "name is unknown, and power unmeasurable. You may attempt to kill the Beast at any given moment, but \n"
              "doing so poses a great risk. You must be prepared.")
        print(
            "You may visit 4 other locations, all which hold a powerful king that treasures an ancient tablet written "
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
        elif moving_through_hamlet == "sanatorium":
            print("Welcome to the sanatorium")
        elif moving_through_hamlet == "training room":
            print("Welcome to the training room")

    def hamlet_guild(self):

        test = list(MainClasses.Mage.mage_attacks.keys())
        print("You have the following attacks:")
        for keys in test:
            print(keys)


hamlet = Hamlet()
hamlet.hamlet_guild()
