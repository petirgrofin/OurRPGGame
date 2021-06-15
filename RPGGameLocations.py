import random
import RPGGameCombat as Combat
import MainCharacterClasses as MainClasses
import RPGGameHamlet as Hamlet


class RandomRoomGeneration:

    def __init__(self):
        self.room_has_battle = None

    def random_room_generator(self, level):

        possible_room_amount = 0

        if level == "apprentice":

            possible_room_amount = random.randint(5, 10)

        elif level == "veteran":

            possible_room_amount = random.randint(8, 12)

        current_dungeon_rooms = [number_of_rooms for number_of_rooms in range(1, possible_room_amount + 1)]

        print(
            f"After the hamlet's caretaker handed you a map, you found that this dungeon will have {current_dungeon_rooms[-1]} rooms")

        current_dungeon_rooms_dict = dict.fromkeys(current_dungeon_rooms)

        initial_value = 100

        for battle_check in current_dungeon_rooms:

            probability = random.randint(0, 100)

            if probability < initial_value:
                self.room_has_battle = True
            else:
                self.room_has_battle = False

            initial_value -= 20

            updated_dict_value = {battle_check: self.room_has_battle}

            current_dungeon_rooms_dict.update(updated_dict_value)

            if initial_value == 0:
                initial_value = 100

        return current_dungeon_rooms_dict


class Dungeons:

    def __init__(self, mission_choose, health):

        self.mission_choose = mission_choose
        self.initial_health_chosen = False
        self.health = health
        self.fight_outcome = None
        self.health_left = 0

    def missions(self, location):

        dungeon_rooms = {}

        if self.mission_choose == "apprentice level mission":

            random_room_generation = RandomRoomGeneration()
            dungeon_rooms = random_room_generation.random_room_generator("apprentice")

        elif self.mission_choose == "veteran level mission":

            random_room_generation = RandomRoomGeneration()
            dungeon_rooms = random_room_generation.random_room_generator("veteran")

        dungeon_fights = Combat.combat

        print(dungeon_fights)

        print("Loading apprentice level mission...")

        print("In this mission, you must advance through a series of rooms containing enemies to reach a key.")

        print("This key grants access to the veteran chamber, where you will face ever more dangerous foes.")

        start_dungeon = input("Do you wish to start the dungeon?: ")  # starting at room 0

        if start_dungeon == "yes":

            for all_rooms, battle_rooms in dungeon_rooms.items():

                if battle_rooms and not self.initial_health_chosen:
                    if location == "Caverns":  # can probably find a way to optimize this
                        self.fight_outcome = dungeon_fights("Caverns", 2,
                                                            gold_ammount=MainClasses.chosen_class.gold_pieces,
                                                            health_for_next_fight=MainClasses.chosen_class.picked_class_health)
                    self.initial_health_chosen = True

                elif battle_rooms and self.initial_health_chosen:
                    if location == "Caverns":
                        self.fight_outcome = dungeon_fights("Caverns", 2,
                                                            gold_ammount=MainClasses.chosen_class.gold_pieces,
                                                            health_for_next_fight=self.health_left)

                if battle_rooms and self.fight_outcome[1]:

                    print(f"Reality has broken out around you, and you have been pulled to a fracture in"
                          f"space and time. Mysterious, human-like and hooded entities have dragged you "
                          f"back to the Hamlet, "
                          f"but this journey felt excruciatingly long for your character...")
                    print(f"New trait: have to make traits")
                    break

                elif battle_rooms and not self.fight_outcome[1]:
                    print(f"For the next fight, you will have {self.fight_outcome[0]} health")
                    self.health_left = self.fight_outcome[0]

                elif not battle_rooms:
                    print("Room doesn't have anything")

                choose_to_advance = input("Do you wish to advance, or return to the hamlet?: ")

                if choose_to_advance == "advance":
                    print(f"You have advanced one room, and you are currently in the room {all_rooms}")
                    if all_rooms == list(dungeon_rooms.keys())[-1]:
                        print("You have finished the dungeon. You have unlocked a key. Returning to "
                              "hamlet...")
                        veteran_access = True
                        return veteran_access

                    continue

                elif choose_to_advance == "hamlet":
                    Hamlet.hamlet.hamlet_general()
                    break
