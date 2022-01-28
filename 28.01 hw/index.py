class Animal:
    def __init__(self,species,sounds):
        self.species=species
        self.sounds=sounds
    def species_animal(self):
        print(f"type={self.species}")
    def sound_animal(self):
        print(f"sound= {self.sounds}")
class Dog(Animal):
    def __init__(self, species,sounds):
        super().__init__(species,sounds)

class Cat(Animal):
    def __init__(self, species,sounds):
        super().__init__(species,sounds)

animals=["dog",'cat']

def show_cat_info(x,sounds,species):
    if x in animals:
        x=Cat(species,sounds)
        x.species_animal()
        x.sound_animal()
    else:
        print("error")
show_cat_info("cat","mya","Jojo_ml")
def show_dog_info(x,sounds,species):
    if x in animals:
        x=Cat(species,sounds)
        x.species_animal()
        x.sound_animal()
    else:
        print("error")
show_dog_info("dog","gav","Jojo_st")