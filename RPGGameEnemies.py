import random


class Marauder:
    marauder_stats = {
        "marauder_health": 1000,
        "marauder_damage": 90,
        "marauder_speed": 40,
        "marauder_defense": 50,
        "marauder_stun_resistance": 10,
        "marauder_bleed_resistance": 10
    }

    marauder_attacks = {
        "marauder_sword_swing": 50 + marauder_stats["marauder_damage"],
        "marauder_ballista_shot": marauder_stats["marauder_damage"] + 30
    }


class Ectoplasm:
    ectoplasm_stats = {
        "ectoplasm_health": 500,
        "ectoplasm_damage": 60,
        "ectoplasm_speed": 50,
        "ectoplasm_defense": 20,
        "ectoplasm_stun_resistance": 10,
        "ectoplasm_bleed_resistance": 10
    }

    ectoplasm_attacks = {
        "ectoplasm_bounce_attack": 50 + ectoplasm_stats["ectoplasm_damage"],
        "ectoplasm_pistol_shot": 40 + ectoplasm_stats["ectoplasm_damage"]
    }


class CavernEnemies:
    cavern_enemies_stats = {
        "cavern_enemies_assassin_worm_name": "Assassin Worm",
        "cavern_enemies_cave_spider": "Cave Spider",
        "cavern_enemies_health": 1300,
        "cavern_enemies_damage": 90,
        "cavern_enemies_speed": 20,
        "cavern_enemies_defense": 60,
        "cavern_enemies_stun_resistance": 10,
        "cavern_enemies_bleed_resistance": 30
    }

    cavern_enemies_assassin_worm_attack = {
        "cavern_enemies_assassin_worm_pounce": 30 + cavern_enemies_stats["cavern_enemies_damage"],
        "cavern_enemies_assassin_worm_pistol_attack": cavern_enemies_stats["cavern_enemies_damage"] + 20,
    }

    cavern_enemies_cave_spider_attack ={
        "cavern_enemies_cave_spider_bite": 20 + cavern_enemies_stats["cavern_enemies_damage"],
        "cavern_enemies_cave_spider_venom_sting": cavern_enemies_stats["cavern_enemies_damage"] + 40,
    }

class RandomEnemy:

    def __init__(self):

        self.picked_enemy = None
        self.enemy_name = None
        self.enemy_attack = None
        self.picked_enemy_health = None
        self.enemy_already_chosen = None
        self.enemy_attack_name = None
        self.stun_resist = None
        self.bleed_resist = None

    def enemy_choose(self):
        self.picked_enemy = random.choice([Marauder, Ectoplasm])
        if self.picked_enemy == Marauder:
            self.enemy_name = "Marauder"
            self.picked_enemy_health = Marauder.marauder_stats["marauder_health"]
            self.stun_resist = Marauder.marauder_stats["marauder_stun_resistance"]
            self.bleed_resist = Marauder.marauder_stats["marauder_bleed_resistance"]

        elif self.picked_enemy == Ectoplasm:
            self.enemy_name = "Ectoplasm"
            self.picked_enemy_health = Ectoplasm.ectoplasm_stats["ectoplasm_health"]
            self.stun_resist = Ectoplasm.ectoplasm_stats["ectoplasm_stun_resistance"]
            self.bleed_resist = Ectoplasm.ectoplasm_stats["ectoplasm_bleed_resistance"]

        elif self.picked_enemy == CavernEnemies:
            self.enemy_name = "Assassin Worm"
            self.picked_enemy_health = CavernEnemies.cavern_enemies_stats["cavern_enemies_health"]
            self.stun_resist = CavernEnemies.cavern_enemies_stats["cavern_enemies_stun_resistance"]
            self.bleed_resist = CavernEnemies.cavern_enemies_stats["cavern_enemies_bleed_resistance"]

        elif self.picked_enemy == CavernEnemies:
            self.enemy_name = "Cave Spider"
            self.picked_enemy_health = CavernEnemies.cavern_enemies_stats["cavern_enemies_health"]
            self.stun_resist = CavernEnemies.cavern_enemies_stats["cavern_enemies_stun_resistance"]
            self.bleed_resist = CavernEnemies.cavern_enemies_stats["cavern_enemies_bleed_resistance"]

    def enemy_attack_chooser(self):

        if self.picked_enemy == Marauder:
            self.enemy_attack = random.choice([Marauder.marauder_attacks["marauder_sword_swing"],
                                               Marauder.marauder_attacks["marauder_ballista_shot"]])
            if self.enemy_attack == Marauder.marauder_attacks["marauder_sword_swing"]:
                self.enemy_attack_name = "Sword Swing"
            elif self.enemy_attack == Marauder.marauder_attacks["marauder_ballista_shot"]:
                self.enemy_attack_name = "Ballista Shot"

        elif self.picked_enemy == Ectoplasm:
            self.enemy_attack = random.choice([Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"],
                                               Ectoplasm.ectoplasm_attacks["ectoplasm_pistol_shot"]])
            if self.enemy_attack == Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"]:
                self.enemy_attack_name = "Bounce Attack"
            elif self.enemy_attack == Ectoplasm.ectoplasm_attacks["ectoplasm_pistol_shot"]:
                self.enemy_attack_name = "Pistol Shot"

        elif self.picked_enemy == CavernEnemies:
            self.enemy_attack = random.choice([CavernEnemies.cavern_enemies_assassin_worm_attack["assassin_worm_pounce"],
                                               CavernEnemies.cavern_enemies_assassin_worm_attack["assassin_worm_pistol_attack"]])
            if self.enemy_attack == CavernEnemies.cavern_enemies_assassin_worm_attack["assassin_worm_pounce"]:
                self.enemy_attack_name = "Pounce"
            elif self.enemy_attack == CavernEnemies.cavern_enemies_assassin_worm_attack["assassin_worm_pistol_attack"]:
                self.enemy_attack_name = "Pistol Attack"

        elif self.picked_enemy == CavernEnemies:
            self.enemy_attack = random.choice([CavernEnemies.cavern_enemies_cave_spider_attack["cave_spider_bite"],
                                               CavernEnemies.cavern_enemies_cave_spider_attack["cave_spider_venom_sting"]])
            if self.enemy_attack == CavernEnemies.cavern_enemies_cave_spider_attack["cave_spider_bite"]:
                self.enemy_attack_name = "Bite"
            elif self.enemy_attack == CavernEnemies.cavern_enemies_cave_spider_attack["cave_spider_venom_sting"]:
                self.enemy_attack_name = "Venom Sting"


random_enemy = RandomEnemy()
