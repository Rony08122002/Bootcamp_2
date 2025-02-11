#1
#class Cat:
#    def __init__(self, cat_name, cat_age):
#        self.name = cat_name
#        self.age = cat_age

#cat_1 = Cat('toma', 25)
#cat_2 = Cat('jhon', 20)
#cat_3 = Cat('arthur', 27)

#def find_oldest_cat(cats):
#    return max(cats, key=lambda cat: cat.age)

#oldest_cat = find_oldest_cat([cat_1, cat_2, cat_3])

#print(f"The oldest cat in Birmingham is {oldest_cat.name}, and he is {oldest_cat.age} years old.")

#2
#class Dog:
#    def __init__(self, name, height ):
#        self.name = name
#        self.height = height

#   def bark(self):
#        print(f"{self.name} goes woof!")
#    def jump(self):
#        jump_height = self.height * 2
#        print(f"{self.name} jumps {jump_height} cm high!")



#dog_1 = Dog('git', 54)
#dog_2 = Dog('hub', 48)
#davids_dog = Dog('Rex', 50)
#sarahs_dog = Dog('Teacup', 20)

#dog_1.bark()
#og_2.bark()
#davids_dog.bark()
#sarahs_dog.bark()

#dog_1.jump()
#dog_2.jump()
#davids_dog.jump()
#sarahs_dog.jump()

#def find_height_dog(dogs):
#    return max(dogs, key=lambda dog: dog.height)

#height_dog = find_height_dog([dog_1, dog_2, davids_dog, sarahs_dog])

#print(f"The biggest dog is {height_dog.name}, and he is {height_dog.height} cm.")

#3
#class Song:
   # def __init__(self, lyrics):
   #     self.lyrics = lyrics

  #  def sing_me_a_song(self):
  #      for line in self.lyrics:
 #        print(line)

#song = Song(['this is my song',
 #            'this is a good song',
 #            'wtf am i doing'])
        

#song.sing_me_a_song()
#stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#stairway.sing_me_a_song()

#4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} was sold and removed from the zoo.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()  # לוקח את האות הראשונה
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)

        return grouped_animals

my_zoo = Zoo("madagascar")

my_zoo.add_animal("Lion")
my_zoo.add_animal("Zebra")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Giraffe")
my_zoo.add_animal("Hippo")

#my_zoo.sell_animal("Zebra")
#my_zoo.sell_animal("Lion")
#my_zoo.sell_animal("Giraffe")
#my_zoo.sell_animal("Hippo")

#print(my_zoo.name)
#print(my_zoo.animals)

sorted_animals = my_zoo.sort_animals()

#print(my_zoo.animals)
print(sorted_animals)

#לבקש מרקאל עזרה לסעיף 8
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} was sold and removed from the zoo.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()  # לוקח את האות הראשונה
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)

        return grouped_animals

ramat_gan_zoo = Zoo("madagascar")

ramat_gan_zoo.add_animal("Lion")
ramat_gan_zoo.add_animal("Zebra")
ramat_gan_zoo.add_animal("Lion")
ramat_gan_zoo.add_animal("Giraffe")
ramat_gan_zoo.add_animal("Hippo")

#mramat_gan_zoo.sell_animal("Zebra")
#ramat_gan_zoo.sell_animal("Lion")
#ramat_gan_zoo.sell_animal("Giraffe")
#ramat_gan_zoo.sell_animal("Hippo")

#print(ramat_gan_zoo.name)
#print(ramat_gan_zoo.animals)

sorted_animals = ramat_gan_zoo.sort_animals()

#print(ramat_gan_zoo.animals)
print(sorted_animals)
