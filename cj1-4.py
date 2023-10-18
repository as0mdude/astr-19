class FavoriteAnimal:
    def __init__(self, arms_length, legs_length, num_eyes, has_tail, is_furry):
        self.arms_length = arms_length
        self.legs_length = legs_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
        
    def describe_animal(self):
        print(f"Physical characteristics of my favorite animal:")
        print(f"Arms length: {self.arms_length} units")
        print(f"Legs length: {self.legs_length} units")
        print(f"Number of eyes: {self.num_eyes}")
        if self.has_tail:
            print("it has a tail.")
        else:
            print("it doesn't have a tail.")
        if self.is_furry:
            print("it is furry.")
        else:
            print("it is not furry.")

my_favorite_animal = FavoriteAnimal(2.5, 3.0, 2, True, True)
my_favorite_animal.describe_animal()