import random
import MainCharacterClasses as MainClasses


class Marauder:

    marauder_stats = {
        "marauder_health": 300,
        "marauder_damage": 30,
        "marauder_speed": 40,
        "marauder_defense": 50
    }

    marauder_attacks = {
        "marauder_sword_swing": (50 + marauder_stats["marauder_damage"]),
        "marauder_ballista_shot": (marauder_stats["marauder_damage"] + 30)
    }


class Ectoplasm:

    ectoplasm_stats = {
        "ectoplasm_health": 200,
        "ectoplasm_damage": 50,
        "ectoplasm_speed": 50,
        "ectoplasm_defense": 20
    }

    ectoplasm_attacks = {
        "ectoplasm_bounce_attack": (50 + ectoplasm_stats["ectoplasm_damage"]),
        "ectoplasm_pistol_shot": (40 + ectoplasm_stats["ectoplasm_damage"])
    }


class RandomEnemy:

    def __init__(self):
        self.picked_enemy = None
        self.enemy_name = None
        self.enemy_attack = None
        self.picked_enemy_health = None
        self.enemy_already_chosen = None

    def enemy_choose(self):
        self.picked_enemy = random.choice([Marauder, Ectoplasm])
        if self.picked_enemy == Marauder:
            self.enemy_name = "Marauder"
            self.picked_enemy_health = Marauder.marauder_stats["marauder_health"]
        elif self.picked_enemy == Ectoplasm:
            self.enemy_name = "Ectoplasm"
            self.picked_enemy_health = Ectoplasm.ectoplasm_stats["ectoplasm_health"]
        self.enemy_already_chosen = True
        return self.picked_enemy, self.enemy_name, self.enemy_already_chosen, self.picked_enemy_health

    def enemy_attack_chooser(self):
        if self.picked_enemy == Marauder:
            self.enemy_attack = random.choice([Marauder.marauder_attacks["marauder_sword_swing"],
                                               Marauder.marauder_attacks["marauder_ballista_shot"]])
        elif self.picked_enemy == Ectoplasm:
            self.enemy_attack = random.choice([Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"],
                                               Ectoplasm.ectoplasm_attacks["ectoplasm_pistol_shot"]])
        return self.enemy_attack


random_enemy = RandomEnemy()
