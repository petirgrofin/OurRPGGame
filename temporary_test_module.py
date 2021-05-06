import random


class RandomRoomGeneration:

    def __init__(self):
        self.room_has_battle = None
        self.current_dungeon_rooms_dict_with_prefix = None

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

        # viewing_dict_values = current_dungeon_rooms_dict_with_prefix.values()
        # value_iterator = iter(viewing_dict_values)
        # self.first_value = next(value_iterator)

        print(current_dungeon_rooms_dict_with_prefix)


RandomRoomGeneration().random_room_generator()