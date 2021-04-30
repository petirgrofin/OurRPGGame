class Mage:

    mage_stats = {
        "mage_damage": 80,
        "mage_speed": 50,
        "mage_health": 200,
        "mage_defense": 50,
        "mage_class_name": "Mage"
    }

    mage_attacks = {
        "mage_attack1": 40 + mage_stats["mage_damage"],
        "mage_attack2": 50 + mage_stats["mage_damage"]
    }


class Swordsman:

    swordsman_stats = {
        "swordsman_damage": 20,
        "swordsman_health": 40,
        "swordsman_defense": 100,
        "swordsman_ speed": 10
    }

    swordsman_attacks = {
        "swordsman_axe_swing": swordsman_stats["swordsman_damage"] + 60,
        "swordsman_arrow": swordsman_stats["swordsman_damage"] + 30
    }


class Ranged:

    ranged_stats = {
        "ranged_damage": 30,
        "ranged_health": 300,
        "ranged_speed": 20,
        "ranged_defense": 75,
    }

    ranged_attacks = {
        "ranged_bullet_attack": 100 + ranged_stats["ranged_damage"],
        "ranged_crossbow_attack": 50 + ranged_stats["ranged_damage"]
    }


class ChosenClass:

    def __init__(self):

        self.picked_class = None
        self.chosen_attack = None

        self.picked_class_health = None
        self.picked_class_defense = None

    def class_choose(self, choose_a_class_question):  # It wasn't working previously because by defining 2 instances
        # of the class, we are calling __init__ again, so it gets returned to None value, and therefore
        # chosen_attack couldn't be found and would return its __init__ value (None)
        if choose_a_class_question == "mage".lower():
            self.picked_class = Mage
            print("You have chosen the Mage")
            self.picked_class_health = Mage.mage_stats["mage_health"]
            self.picked_class_defense = Mage.mage_stats["mage_defense"]
        elif choose_a_class_question == "ranged".lower():
            self.picked_class = Ranged
            print("You have chosen the Ranged class")
            self.picked_class_health = Ranged.ranged_stats["ranged_health"]
            self.picked_class_defense = Ranged.ranged_stats["ranged_defense"]
        elif choose_a_class_question == "swordsman".lower():
            self.picked_class = Swordsman
            print("You have chosen the Swordsman")
            self.picked_class_health = Swordsman.swordsman_stats["swordsman_health"]
            self.picked_class_defense = Swordsman.swordsman_stats["swordsman_defense"]

    def attack_choose(self, choose_an_attack_question):
        if self.picked_class == Mage:  # block of code to define chosen_attack
            if choose_an_attack_question == "attack1".lower():
                self.chosen_attack = Mage.mage_attacks["mage_attack1"]
            elif choose_an_attack_question == "attack2".lower():
                self.chosen_attack = Mage.mage_attacks["mage_attack2"]
        if self.picked_class == Swordsman:
            if choose_an_attack_question == "attack1".lower():
                self.chosen_attack = Swordsman.swordsman_attacks["swordsman_axe_swing"]
            elif choose_an_attack_question == "attack2".lower():
                self.chosen_attack = Swordsman.swordsman_attacks["swordsman_arrow"]
        if self.picked_class == Ranged:
            if choose_an_attack_question == "attack1".lower():
                self.chosen_attack = Ranged.ranged_attacks["ranged_bullet_attack"]
            elif choose_an_attack_question == "attack2".lower():
                self.chosen_attack = Ranged.ranged_attacks["ranged_crossbow_attack"]
        return self.chosen_attack


chosen_class = ChosenClass()

# chosen_class_instance.class_choose(input("Select a class: "))
# chosen_class_instance.attack_choose(input("Select an attack: "))
# print(chosen_class_instance.chosen_attack)
