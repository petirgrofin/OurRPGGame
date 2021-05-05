import random
import RPGGameCombat as Combat


class RandomRoomGeneration:

    def __init__(self):
        self.room_has_battle = None
        self.first_value = None

    def random_room_generator(self):

        possible_room_amount = random.randint(5, 10)

        current_dungeon_rooms = []

        for number_of_rooms in range(1, possible_room_amount + 1):
            current_dungeon_rooms.append(number_of_rooms)

        print(f"After one of the villagers handed you a map, you found that this dungeon will have {current_dungeon_rooms[-1]} rooms")

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

        prefix = "Room "  # adding prefix to current_dungeon_rooms_dict
        current_dungeon_rooms_dict_with_prefix = {prefix + str(key): val for key, val in current_dungeon_rooms_dict.items()}

        viewing_dict_values = current_dungeon_rooms_dict_with_prefix.values()
        value_iterator = iter(viewing_dict_values)
        self.first_value = next(value_iterator)


class TheCaverns:

    def __init__(self, mission_choose):

        self.mission_choose = mission_choose

    def first_mission(self):

        if self.mission_choose == "apprentice level mission":

            print("Loading apprentice level mission...")

            print("In this mission, you must advance through a series of rooms containing enemies to reach a key.")

            print("This key grants access to the veteran chamber, where you will face ever more dangerous foes.")

            loading_screen_end = input("Do you wish to continue?: ")

            if loading_screen_end == "yes":

                random_room_generation = RandomRoomGeneration()
                random_room_generation.random_room_generator()

                choose_to_advance = input("Do you wish to advance, or return to the hamlet?: ")
                if choose_to_advance == "advance":
                    print("You have advanced one room")
                    if random_room_generation.first_value:
                        Combat.combat("Cavern", 2)


TheCaverns("apprentice level mission").first_mission()
