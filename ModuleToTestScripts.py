import MainCharacterClasses as MainClasses
import RPGGameEnemies as Enemies


class Debuffs:

    def __init__(self, original_stun_resistance, original_bleed_duration, accumulative_bleed_damage):

        self.original_stun_resistance = original_stun_resistance
        self.original_bleed_duration = original_bleed_duration
        self.accumulative_bleed_damage = accumulative_bleed_damage


Enemies.random_enemy.enemy_choose()  # then an enemy
MainClasses.chosen_class.stun_debuffs()  # then check for stuns
MainClasses.chosen_class.bleed_debuffs()  # then check for bleeds

def value_returner():

    debuffs = Debuffs(Enemies.random_enemy.stun_resist, MainClasses.chosen_class.bleed_duration, MainClasses.chosen_class.base_bleed_damage)

    print(f"The debuff resistance is {debuffs.original_stun_resistance}, the bleed duration is {debuffs.original_bleed_duration} and the accumulative bleed damage is {debuffs.accumulative_bleed_damage}")

value_returner()