
class Dog:

    def __init__(self, name, is_loyal):
        self.name = name
        self.is_loyal = is_loyal

    def checking_dog_characteristics(self):

        print(f"The dog is named {self.name}")
        print(f"The dog is loyal: {self.is_loyal}")


akira_dog = Dog(name="Akira", is_loyal=True)


class Cats:

    are_cute = True  # always
    legs = 4  # hopefully always
    head = 1

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def checking_cat_characteristics(self):

        print(f"The cat is named {self.name}")
        print(f"The cat is cute: {Cats.are_cute}")
        print(f"The cat's owner is: {self.owner}")
        print(f"The cat has {Cats.legs} legs and {Cats.head} head")
        print(f"The cat is of a {self.breed} race")


kiu_cat = Cats(name="Kiu", breed="mixed", owner="Sofi")
oliver_cat = Cats(name="Oliver", breed="unknown", owner="Sofi")

kiu_cat.checking_cat_characteristics()
oliver_cat.checking_cat_characteristics()