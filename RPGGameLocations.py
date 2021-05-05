import random


class RandomRoomGeneration:

    def __init__(self):
        self.room_has_battle = None

    def random_room_generator(self):

        room_amount = random.randint(5, 10)

        print(f"After scouting, you found that the dungeon will have {room_amount} rooms")

        rooms = 1

        A = list()

        initial_value = 0

        for _ in range(1, room_amount + 1):
            A.append(rooms)
            rooms += 1

        for _ in A:

            probability = random.randint(0, 100)

            if probability > initial_value:
                self.room_has_battle = True
            else:
                self.room_has_battle = False

            print(self.room_has_battle)
            initial_value += 20

        rooms_dictionary = dict.fromkeys(rooms, self.room_has_battle)

        print(rooms_dictionary)


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

                RandomRoomGeneration().random_room_generator()


TheCaverns("apprentice level mission").first_mission()
