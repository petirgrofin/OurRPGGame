import random


class Marauder:
    marauder_stats = {
        "marauder_health": 800,
        "marauder_damage": 80,
        "marauder_speed": 40,
        "marauder_defense": 50,
        "marauder_stun_resistance": 10,
        "marauder_bleed_resistance": 10
    }

    marauder_possible_drops = {
        "gold": 50
    }

    marauder_attacks = {
        "marauder_sword_swing": 50 + marauder_stats["marauder_damage"],
        "marauder_ballista_shot": marauder_stats["marauder_damage"] + 30
    }


class Ectoplasm:
    ectoplasm_stats = {
        "ectoplasm_health": 800,
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

    ectoplasm_possible_drops = {
        "gold": 50
    }


class CavernEnemies:

    cavern_enemies_stats = {
        "cavern_enemies_assassin_worm_name": "Assassin Worm",
        "cavern_enemies_cave_spider": "Cave Spider",
        "cavern_enemies_choletinia": "Choletinia",
        "cavern_enemies_health": 1300,
        "cavern_enemies_damage": 90,
        "cavern_enemies_speed": 20,
        "cavern_enemies_defense": 60,
        "cavern_enemies_stun_resistance": 10,
        "cavern_enemies_bleed_resistance": 30
    }

    @staticmethod
    def stats_increase(increase_or_decrease):

        original_cavern_enemies_stats = CavernEnemies.cavern_enemies_stats

        if increase_or_decrease == "increase":

            dictionary_of_stats = {key: value for key, value in CavernEnemies.cavern_enemies_stats.items()
                                   if "health" in key or "damage" in key or "speed" in key or "defense" in key or "stun"
                                   in key or "bleed" in key}

            updated_values = {key: value + 300 for key, value in dictionary_of_stats.items()}

            CavernEnemies.cavern_enemies_stats.update(updated_values)

            print(CavernEnemies.cavern_enemies_stats)

        else:

            CavernEnemies.cavern_enemies_stats.update(original_cavern_enemies_stats)


class AssassinWorm(CavernEnemies):

    cavern_enemies_assassin_worm_attack = {
        "assassin_worm_pounce": 30 + CavernEnemies.cavern_enemies_stats["cavern_enemies_damage"],
        "assassin_worm_pistol_attack": CavernEnemies.cavern_enemies_stats["cavern_enemies_damage"] + 20,
    }


class CaveSpider(CavernEnemies):
    cavern_enemies_cave_spider_attack = {
        "cave_spider_bite": 20 + CavernEnemies.cavern_enemies_stats["cavern_enemies_damage"],
        "cave_spider_venom_sting": CavernEnemies.cavern_enemies_stats["cavern_enemies_damage"] + 40,
    }


class Choletinia(CavernEnemies):
    cavern_enemies_choletinia_attack = {
        "choletinia_massive_antennas": 10 + CavernEnemies.cavern_enemies_stats["cavern_enemies_damage"],
        "choletinia_screech": CavernEnemies.cavern_enemies_stats["cavern_enemies_damage"] + 30,

    }


class CastleEnemies:
    castle_enemies_stats = {
        "castle_enemies_skeleton": "Skeleton",
        "castle_enemies_the_princess": "The Princess",
        "castle_enemies_the_king": "The King",
        "castle_enemies_health": 2000,
        "castle_enemies_damage": 80,
        "castle_enemies_speed": 30,
        "castle_enemies_defense": 50,
        "castle_enemies_stun_resistance": 30,
        "castle_enemies_bleed_resistance": 30
    }


class Skeleton(CastleEnemies):
    castle_enemies_skeleton_attack = {
        "skeleton_bow_shot": 30 + CastleEnemies.castle_enemies_stats["castle_enemies_damage"],
        "skeleton_fire_arrow": CastleEnemies.castle_enemies_stats["castle_enemies_damage"] + 40,
    }


class ThePrincess(CastleEnemies):
    castle_enemies_the_princess_attack = {
        "the_princess_magic_powder": 20 + CastleEnemies.castle_enemies_stats["castle_enemies_damage"],
        "the_princess_rainbow_attack": CastleEnemies.castle_enemies_stats["castle_enemies_damage"] + 50,
    }


class TheKing(CastleEnemies):
    castle_enemies_the_king_attack = {
        "the_king_knife_cut": 10 + CastleEnemies.castle_enemies_stats["castle_enemies_damage"],
        "the_king_knife_throwing_attack": CastleEnemies.castle_enemies_stats["castle_enemies_damage"] + 30,
    }



class SwampEnemies:
    swamp_enemies_stats = {
        "swamp_enemies_slime": "Slime",
        "swamp_enemies_mudman": "Mudman",
        "swamp_enemies_swamp_crab": "Swamp Crab",
        "swamp_enemies_health": 1700,
        "swamp_enemies_damage": 70,
        "swamp_enemies_speed": 10,
        "swamp_enemies_defense": 20,
        "swamp_enemies_stun_resistance": 60,
        "swamp_enemies_bleed_resistance": 40
    }


class Slime(SwampEnemies):
    swamp_enemies_slime_attack = {
        "slime_acid_spit": 20 + SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"],
        "slime_grow_attack": SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"] + 15,
    }


class Mudman(SwampEnemies):
    swamp_enemies_mudman_attack = {
        "mudman_mud_ball": 25 + SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"],
        "mudman_grab_attack": SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"] + 30,
        "mudman_poisonous_water": 35 + SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"],
    }


class SwampCrab(SwampEnemies):
    swamp_enemies_swamp_crab_attack = {
        "swamp_crab_scissors_attack": 20 + SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"],
        "swamp_crab_toxic_algae": SwampEnemies.swamp_enemies_stats["swamp_enemies_damage"] + 10,
    }


class RandomEnemy:

    def __init__(self):

        self.picked_enemy = None
        self.additional_picked_enemy = None

        self.enemy_name = None
        self.enemy_attack = None
        self.enemy_attack_name = None
        self.picked_enemy_health = None
        self.first_enemy_drops = None
        self.second_enemy_drops = None

        self.stun_resist = None
        self.bleed_resist = None

        self.additional_enemy_name = None
        self.additional_enemy_attack = None
        self.additional_enemy_health = None
        self.additional_enemy_attack_name = None

        self.additional_enemy_stun_resist = None
        self.additional_enemy_bleed_resist = None

        self.enemy_stun_capable_attack = None
        self.enemy_stun_chance = None
        self.additional_enemy_stun_capable_attack = None
        self.additional_enemy_stun_chance = None

    def enemy_choose(self):

        self.picked_enemy = random.choice([Marauder, Ectoplasm])
        self.additional_picked_enemy = random.choice([Marauder, Ectoplasm])  # starting to implement more enemies

        if self.picked_enemy == self.additional_picked_enemy:
            if self.picked_enemy == Marauder:
                self.additional_picked_enemy = Ectoplasm
            if self.picked_enemy == Ectoplasm:
                self.additional_picked_enemy = Marauder

        if self.picked_enemy == Marauder:
            self.enemy_name = "Marauder"
            self.picked_enemy_health = Marauder.marauder_stats["marauder_health"]
            self.stun_resist = Marauder.marauder_stats["marauder_stun_resistance"]
            self.bleed_resist = Marauder.marauder_stats["marauder_bleed_resistance"]
            self.first_enemy_drops = Marauder.marauder_possible_drops["gold"]

        elif self.picked_enemy == Ectoplasm:
            self.enemy_name = "Ectoplasm"
            self.picked_enemy_health = Ectoplasm.ectoplasm_stats["ectoplasm_health"]
            self.stun_resist = Ectoplasm.ectoplasm_stats["ectoplasm_stun_resistance"]
            self.bleed_resist = Ectoplasm.ectoplasm_stats["ectoplasm_bleed_resistance"]
            self.first_enemy_drops = Ectoplasm.ectoplasm_possible_drops["gold"]

        if self.additional_picked_enemy == Marauder:
            self.additional_enemy_name = "Marauder"
            self.additional_enemy_health = Marauder.marauder_stats["marauder_health"]
            self.additional_enemy_bleed_resist = Marauder.marauder_stats["marauder_bleed_resistance"]
            self.additional_enemy_stun_resist = Marauder.marauder_stats["marauder_stun_resistance"]
            self.second_enemy_drops = Marauder.marauder_possible_drops["gold"]

        elif self.additional_picked_enemy == Ectoplasm:
            self.additional_enemy_name = "Ectoplasm"
            self.additional_enemy_health = Ectoplasm.ectoplasm_stats["ectoplasm_health"]
            self.additional_enemy_bleed_resist = Ectoplasm.ectoplasm_stats["ectoplasm_bleed_resistance"]
            self.additional_enemy_stun_resist = Ectoplasm.ectoplasm_stats["ectoplasm_stun_resistance"]
            self.second_enemy_drops = Ectoplasm.ectoplasm_possible_drops["gold"]

    def cavern_enemy_choose(self):

        self.picked_enemy = random.choice([AssassinWorm, CaveSpider, Choletinia])
        self.additional_picked_enemy = random.choice([AssassinWorm, CaveSpider, Choletinia])

        if self.picked_enemy == self.additional_picked_enemy:
            if self.picked_enemy == AssassinWorm:
                self.additional_picked_enemy = random.choice([CaveSpider, Choletinia])
            if self.picked_enemy == CaveSpider:
                self.additional_picked_enemy = random.choice([AssassinWorm, Choletinia])
            if self.picked_enemy == Choletinia:
                self.additional_picked_enemy = random.choice([AssassinWorm, CaveSpider])

        if self.picked_enemy == AssassinWorm:
            self.enemy_name = "Assassin Worm"
            self.picked_enemy_health = AssassinWorm.cavern_enemies_stats["cavern_enemies_health"]
            self.stun_resist = AssassinWorm.cavern_enemies_stats["cavern_enemies_stun_resistance"]
            self.bleed_resist = AssassinWorm.cavern_enemies_stats["cavern_enemies_bleed_resistance"]

        elif self.picked_enemy == CaveSpider:
            self.enemy_name = "Cave Spider"
            self.picked_enemy_health = CaveSpider.cavern_enemies_stats["cavern_enemies_health"]
            self.stun_resist = CaveSpider.cavern_enemies_stats["cavern_enemies_stun_resistance"]
            self.bleed_resist = CaveSpider.cavern_enemies_stats["cavern_enemies_bleed_resistance"]

        elif self.picked_enemy == Choletinia:
            self.enemy_name = "Choletinia"
            self.picked_enemy_health = Choletinia.cavern_enemies_stats["cavern_enemies_health"]
            self.stun_resist = Choletinia.cavern_enemies_stats["cavern_enemies_stun_resistance"]
            self.bleed_resist = Choletinia.cavern_enemies_stats["cavern_enemies_bleed_resistance"]

    def castle_enemy_choose(self):

        self.picked_enemy = random.choice([Skeleton, ThePrincess, TheKing])
        self.additional_picked_enemy = random.choice([Skeleton, ThePrincess, TheKing])

        if self.picked_enemy == self.additional_picked_enemy:
            if self.picked_enemy == Skeleton:
                self.additional_picked_enemy = random.choice([ThePrincess, TheKing])
            if self.picked_enemy == ThePrincess:
                self.additional_picked_enemy = random.choice([Skeleton, TheKing])
            if self.picked_enemy == TheKing:
                self.additional_picked_enemy = random.choice([Skeleton, ThePrincess])

        if self.picked_enemy == Skeleton:
            self.enemy_name = "Skeleton"
            self.picked_enemy_health = Skeleton.castle_enemies_stats["castle_enemies_health"]
            self.stun_resist = Skeleton.castle_enemies_stats["castle_enemies_stun_resistance"]
            self.bleed_resist = Skeleton.castle_enemies_stats["castle_enemies_bleed_resistance"]

        elif self.picked_enemy == ThePrincess:
            self.enemy_name = "The Princess"
            self.picked_enemy_health = ThePrincess.castle_enemies_stats["castle_enemies_health"]
            self.stun_resist = ThePrincess.castle_enemies_stats["castle_enemies_stun_resistance"]
            self.bleed_resist = ThePrincess.castle_enemies_stats["castle_enemies_bleed_resistance"]


        elif self.picked_enemy == TheKing:
            self.enemy_name = "The King"
            self.picked_enemy_health = TheKing.castle_enemies_stats["castle_enemies_health"]
            self.stun_resist = TheKing.castle_enemies_stats["castle_enemies_stun_resistance"]
            self.bleed_resist = TheKing.castle_enemies_stats["castle_enemies_bleed_resistance"]

    def swamp_enemy_choose(self):

        self.picked_enemy = random.choice([Slime, Mudman, SwampCrab])
        self.additional_picked_enemy = random.choice([Slime, Mudman, SwampCrab])

        if self.picked_enemy == self.additional_picked_enemy:
            if self.picked_enemy == Slime:
                self.additional_picked_enemy = random.choice([Mudman, SwampCrab])
            if self.picked_enemy == Mudman:
                self.additional_picked_enemy = random.choice([Slime, SwampCrab])
            if self.picked_enemy == SwampCrab:
                self.additional_picked_enemy = random.choice([Slime, Mudman])

        if self.picked_enemy == Slime:
            self.enemy_name = "Slime"
            self.picked_enemy_health = Slime.swamp_enemies_stats["swamp_enemies_health"]
            self.stun_resist = Slime.swamp_enemies_stats["swamp_enemies_stun_resistance"]
            self.bleed_resist = Slime.swamp_enemies_stats["swamp_enemies_bleed_resistance"]

        elif self.picked_enemy == Mudman:
            self.enemy_name = "Mudman"
            self.picked_enemy_health = Mudman.swamp_enemies_stats["swamp_enemies_health"]
            self.stun_resist = Mudman.swamp_enemies_stats["swamp_enemies_stun_resistance"]
            self.bleed_resist = Mudman.swamp_enemies_stats["swamp_enemies_bleed_resistance"]


        elif self.picked_enemy == SwampCrab:
            self.enemy_name = "Swamp Crab"
            self.picked_enemy_health = SwampCrab.swamp_enemies_stats["swamp_enemies_health"]
            self.stun_resist = SwampCrab.swamp_enemies_stats["swamp_enemies_stun_resistance"]
            self.bleed_resist = SwampCrab.swamp_enemies_stats["swamp_enemies_bleed_resistance"]


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

        if self.additional_picked_enemy == Marauder:

            self.additional_enemy_attack = random.choice([Marauder.marauder_attacks["marauder_sword_swing"],
                                                          Marauder.marauder_attacks["marauder_ballista_shot"]])
            if self.additional_enemy_attack == Marauder.marauder_attacks["marauder_sword_swing"]:
                self.additional_enemy_attack_name = "Sword Swing"
            elif self.additional_enemy_attack == Marauder.marauder_attacks["marauder_ballista_shot"]:
                self.additional_enemy_attack_name = "Ballista Shot"

        elif self.additional_picked_enemy == Ectoplasm:

            self.additional_enemy_attack = random.choice([Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"],
                                                          Ectoplasm.ectoplasm_attacks["ectoplasm_pistol_shot"]])
            if self.additional_enemy_attack == Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"]:
                self.additional_enemy_attack_name = "Bounce Attack"
            elif self.additional_enemy_attack == Ectoplasm.ectoplasm_attacks["ectoplasm_pistol_shot"]:
                self.additional_enemy_attack_name = "Pistol Shot"


        elif self.picked_enemy == AssassinWorm:
            self.enemy_attack = random.choice([AssassinWorm.cavern_enemies_assassin_worm_attack["assassin_worm_pounce"],
                                               AssassinWorm.cavern_enemies_assassin_worm_attack[
                                                   "assassin_worm_pistol_attack"]])
            if self.enemy_attack == AssassinWorm.cavern_enemies_assassin_worm_attack["assassin_worm_pounce"]:
                self.enemy_attack_name = "Pounce"
            elif self.enemy_attack == AssassinWorm.cavern_enemies_assassin_worm_attack["assassin_worm_pistol_attack"]:
                self.enemy_attack_name = "Pistol Attack"

        elif self.picked_enemy == CaveSpider:
            self.enemy_attack = random.choice([CaveSpider.cavern_enemies_cave_spider_attack["cave_spider_bite"],
                                               CaveSpider.cavern_enemies_cave_spider_attack["cave_spider_venom_sting"]])
            if self.enemy_attack == CaveSpider.cavern_enemies_cave_spider_attack["cave_spider_bite"]:
                self.enemy_attack_name = "Bite"
            elif self.enemy_attack == CaveSpider.cavern_enemies_cave_spider_attack["cave_spider_venom_sting"]:
                self.enemy_attack_name = "Venom Sting"

        elif self.picked_enemy == Choletinia:
            self.enemy_attack = random.choice(
                [Choletinia.cavern_enemies_choletinia_attack["choletinia_massive_antennas"],
                 Choletinia.cavern_enemies_choletinia_attack["choletinia_screech"]])
            if self.enemy_attack == Choletinia.cavern_enemies_choletinia_attack["choletinia_massive_antennas"]:
                self.enemy_attack_name = "Massive Antennas"
            elif self.enemy_attack == Choletinia.cavern_enemies_choletinia_attack["choletinia_screech"]:
                self.enemy_attack_name = "Screech"


        elif self.picked_enemy == Skeleton:
            self.enemy_attack = random.choice([Skeleton.castle_enemies_skeleton_attack["skeleton_bow_shot"],
                                               Skeleton.castle_enemies_skeleton_attack["skeleton_fire_arrow"]])
            if self.enemy_attack == Skeleton.castle_enemies_skeleton_attack["skeleton_bow_shot"]:
                self.enemy_attack_name = "Bow Shot"
            elif self.enemy_attack == Skeleton.castle_enemies_skeleton_attack["skeleton_fire_arrow"]:
                self.enemy_attack_name = "Fire Arrow"

        elif self.picked_enemy == ThePrincess:

            self.enemy_attack = random.choice(
                [ThePrincess.castle_enemies_the_princess_attack["the_princess_magic_powder"],
                 ThePrincess.castle_enemies_the_princess_attack["the_princess_rainbow_shot"]])
            if self.enemy_attack == ThePrincess.castle_enemies_the_princess_attack["the_princess_magic_powder"]:
                self.enemy_attack_name = "Magic Powder"
            elif self.enemy_attack == ThePrincess.castle_enemies_the_princess_attack["the_princess_rainbow_shot"]:
                self.enemy_attack_name = "Rainbow Shot"

        elif self.picked_enemy == TheKing:
            self.enemy_attack = random.choice([TheKing.castle_enemies_the_king_attack["the_king_knife_cut"],
                                               TheKing.castle_enemies_the_king_attack[
                                                   "the_king_knife_throwing_attack"]])
            if self.enemy_attack == TheKing.castle_enemies_the_king_attack["the_king_knife_cut"]:
                self.enemy_attack_name = "Knife Cut"
            elif self.enemy_attack == TheKing.castle_enemies_the_king_attack["the_king_knife_throwing_attack"]:
                self.enemy_attack_name = "Knife Throwing Attack"


        elif self.picked_enemy == Slime:
            self.enemy_attack = random.choice([Slime.swamp_enemies_slime_attack["slime_acid_spit"],
                                               Slime.swamp_enemies_slime_attack[ "slime_grow_attack"]])
            if self.enemy_attack == Slime.swamp_enemies_slime_attack["slime_acid_spit"]:
                self.enemy_attack_name = "Acid Spit"
            elif self.enemy_attack == Slime.swamp_enemies_slime_attack["slime_grow_attack"]:
                self.enemy_attack_name = "Grow Attack"

        elif self.picked_enemy == Mudman:
            self.enemy_attack = random.choice([Mudman.swamp_enemies_mudman_attack["mudman_mud_ball"],
                                               Mudman.swamp_enemies_mudman_attack["mudman_grab_attack"],
                                               Mudman.swamp_enemies_mudman_attack["mudman_poisonous_water"]])
            if self.enemy_attack == Mudman.swamp_enemies_mudman_attack["mudman_mud_ball"]:
                self.enemy_attack_name = "Mud Ball"
            elif self.enemy_attack == Mudman.swamp_enemies_mudman_attack["mudman_grab_attack"]:
                self.enemy_attack_name = "Grab Attack"
            elif self.enemy_attack == Mudman.swamp_enemies_mudman_attack["mudman_poisonous_water"]:
                self.enemy_attack_name = "Poisonous Water"

        elif self.picked_enemy == SwampCrab:
            self.enemy_attack = random.choice([SwampCrab.swamp_enemies_swamp_crab_attack["swamp_crab_scissors_attack"],
                                               SwampCrab.swamp_enemies_swamp_crab_attack[ "swamp_crab_toxic_algae"]])
            if self.enemy_attack == SwampCrab.swamp_enemies_swamp_crab_attack["swamp_crab_scissors_attack"]:
                self.enemy_attack_name = "Scissors Attack"
            elif self.enemy_attack == SwampCrab.swamp_enemies_swamp_crab_attack["swamp_crab_toxic_algae"]:
                self.enemy_attack_name = "Toxic Algae"


    def enemy_stun_debuff(self):

        if self.picked_enemy == Marauder:
            if self.enemy_attack == Marauder.marauder_attacks["marauder_ballista_shot"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == Ectoplasm:
            if self.enemy_attack == Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == AssassinWorm:
            if self.enemy_attack == AssassinWorm.cavern_enemies_assassin_worm_attack["assassin_worm_pounce"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == CaveSpider:
            if self.enemy_attack == CaveSpider.cavern_enemies_cave_spider_attack["cave_spider_venom_sting"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == Choletinia:
            if self.enemy_attack == Choletinia.cavern_enemies_choletinia_attack["choletinia_screech"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == Skeleton:
            if self.enemy_attack == Skeleton.castle_enemies_skeleton_attack["skeleton_fire_arrow"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == ThePrincess:
            if self.enemy_attack == ThePrincess.castle_enemies_the_princess_attack["the_princess_rainbow_shot"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.picked_enemy == TheKing:
            if self.enemy_attack == TheKing.castle_enemies_the_king_attack["the_king_knife_throwing_attack"]:
                self.enemy_stun_capable_attack = True
                self.enemy_stun_chance = 100
            else:
                self.enemy_stun_capable_attack = False

        if self.additional_picked_enemy == Marauder:  # additional enemies
            if self.additional_enemy_attack == Marauder.marauder_attacks["marauder_ballista_shot"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == Ectoplasm:
            if self.additional_enemy_attack == Ectoplasm.ectoplasm_attacks["ectoplasm_bounce_attack"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == AssassinWorm:
            if self.additional_enemy_attack == AssassinWorm.cavern_enemies_assassin_worm_attack["assassin_worm_pounce"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == CaveSpider:
            if self.additional_enemy_attack == CaveSpider.cavern_enemies_cave_spider_attack["cave_spider_venom_sting"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == Choletinia:
            if self.additional_enemy_attack == Choletinia.cavern_enemies_choletinia_attack["choletinia_screech"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == Skeleton:
            if self.additional_enemy_attack == Skeleton.castle_enemies_skeleton_attack["skeleton_fire_arrow"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == ThePrincess:
            if self.additional_enemy_attack == ThePrincess.castle_enemies_the_princess_attack[
                "the_princess_rainbow_shot"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False

        if self.additional_picked_enemy == TheKing:
            if self.additional_enemy_attack == TheKing.castle_enemies_the_king_attack["the_king_knife_throwing_attack"]:
                self.additional_enemy_stun_capable_attack = True
                self.additional_enemy_stun_chance = 100
            else:
                self.additional_enemy_stun_capable_attack = False



