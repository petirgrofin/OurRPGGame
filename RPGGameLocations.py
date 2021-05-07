import random
import RPGGameCombat as Combat
import MainCharacterClasses as MainClasses


class RandomRoomGeneration:

    def __init__(self):
        self.room_has_battle = None

    def random_room_generator(self):

        possible_room_amount = random.randint(5, 10)

        current_dungeon_rooms = []

        for number_of_rooms in range(1, possible_room_amount + 1):
            current_dungeon_rooms.append(number_of_rooms)

        print(f"After the hamlet's caretaker handed you a map, you found that this dungeon will have {current_dungeon_rooms[-1]} rooms")

        current_dungeon_rooms_dict = dict.fromkeys(current_dungeon_rooms)

        initial_value = 100

        for battle_check in current_dungeon_rooms:

            probability = random.randint(0, 100)

            if probability < initial_value:
                self.room_has_battle = True
            else:
                self.room_has_battle = False

            initial_value -= 10

            updated_dict_value = {battle_check: self.room_has_battle}

            current_dungeon_rooms_dict.update(updated_dict_value)

        return current_dungeon_rooms_dict


class TheCaverns:

    def __init__(self, mission_choose, health):

        self.mission_choose = mission_choose
        self.initial_health_chosen = False
        self.health = health
        self.fight = None
        self.health_left = 0

    def first_mission(self):

        if self.mission_choose == "apprentice level mission":

            print("Loading apprentice level mission...")

            print("In this mission, you must advance through a series of rooms containing enemies to reach a key.")

            print("This key grants access to the veteran chamber, where you will face ever more dangerous foes.")

            loading_screen_end = input("Do you wish to continue?: ")

            if loading_screen_end == "yes":

                random_room_generation = RandomRoomGeneration()
                dungeon_rooms = random_room_generation.random_room_generator()

                start_dungeon = input("Do you wish to start the dungeon?: ")  # room 0
                if start_dungeon == "yes":

                    for all_rooms, battle_rooms in dungeon_rooms.items():

                        if battle_rooms and not self.initial_health_chosen:
                            self.fight = Combat.combat("Cavern", 2, self.health)
                            self.initial_health_chosen = True

                        elif battle_rooms and self.initial_health_chosen:
                            self.fight = Combat.combat("Cavern", 2, self.health_left)

                        if battle_rooms and self.fight[1]:

                            print(f"Reality has broken out around you, and you have been pulled to a fracture in"
                                    f"space and time. Mysterious, human-like and hooded entities have dragged you "
                                    f"back to the Hamlet, "
                                    f"but this journey felt excruciatingly long for your character...")
                            print(f"New trait: have to make traits")
                            break

                        elif battle_rooms and not self.fight[1]:

                                print(f"For the next fight, you will have {self.fight[0]} health")
                                self.health_left = self.fight[0]

                        elif not battle_rooms:
                            print("Room doesn't have anything")

                        choose_to_advance = input("Do you wish to advance, or return to the hamlet?: ")

                        if choose_to_advance == "advance":
                            print(f"You have advanced one room, and you are currently in the room {all_rooms}")
                            if all_rooms == list(dungeon_rooms.keys())[-1]:
                                print("You have finished the dungeon. Returning to hamlet...")
                                break
                            continue

                        elif choose_to_advance == "hamlet":
                            break
