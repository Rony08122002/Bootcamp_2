#1
#class Pets():
#    def __init__(self, animals):
#        self.animals = animals

#    def walk(self):
#        for animal in self.animals:
#            print(animal.walk())

#class Cat():
#    is_lazy = True

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def walk(self):
#        return f'{self.name} is just walking around'

#class Bengal(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#class Chartreux(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'
    
#class Siamese(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#all_cats = [
#    Bengal("Simba", 2),
#    Chartreux("Muffasa", 4),
#    Siamese("Nala", 3)
#]
#sara_pets = all_cats
#for cat in sara_pets:
#    print(f"{cat.name} is {cat.age} years old.")

#for cat in sara_pets:
#    print(cat.walk())

#2
#class Dog():
#    def __init__(self, name, age, weight):
#        self.name = name
#        self.age = age
#        self.weight = weight
#     
#    def bark(self):
#        print(f"{self.name} barked, WAF !")

#    def run_speed(self):
#        return self.weight / (self.age * 10)

#    def fight(self, other_dog):
#        if self.run_speed() > other_dog.run_speed():
#            return f"{self.name} won the fight!"
#        elif self.run_speed() < other_dog.run_speed():
#            return f"{other_dog.name} won the fight!"
#        else:
#            return "It's a tie!"
        
#dog_1 = Dog('max', 3, 20)
#dog_2 = Dog('duke', 5, 25)
#dog_3 = Dog('gor', 3, 15)

#print(dog_1.bark())
#print(dog_2.run_speed())
#print(dog_1.fight(dog_3))

#3
#import random
#from Dog import dog
#class PetDog(Dog):
#    def __init__(self, name, age, weight):
#        super().__init__(name, age, weight)
#        self.trained = False
#    
#    def train(self):
#        self.bark()
#        self.trained = True
#    
#    def play(self, *dog_names):
#        print(f"{', '.join(dog_names)} all play together")
#    
#    def do_a_trick(self):
#        if self.trained:
#           tricks = [
#                f"{self.name} does a barrel roll",
#                f"{self.name} stands on his back legs",
#                f"{self.name} shakes your hand",
#                f"{self.name} plays dead"
#            ]
#            print(random.choice(tricks))
#        else:
#            print(f"{self.name} is not trained yet!")

#dog1 = PetDog("Buddy", 3, 20)

#dog1.train()
#dog1.play("Max", "Charlie", "Rocky")
#dog1.do_a_trick()

#4
#class Family:
#    def __init__(self, last_name):
#        self.last_name = last_name
#        self.members = []

#    def add_member(self, member):
#        if isinstance(member, dict):
#            self.members.append(member)
#            print(f"Added: {member}")
#        else:
#            print("Member should be a dictionary!")

#    def get_members(self):
#        return self.members
#    def born(self, **kwargs):
#        self.members.append(kwargs)
#        print(F"mazal tov!A new baby has been born: {kwargs['name']}")
#    def is_18(self, name):
#        for member in self.members:
#            if member["name"] == name:
#                return member["age"] >= 18
#    def family_presentation(self):
#        print(f"Family {self.last_name}:")
#        for member in self.members:
#            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}")

#family1 = Family("Cohen")

#family1.add_member({"name": "Doron", "age": 22, "gender": "male"})
#family1.add_member({"name": "Daniel", "age": 20, "gender": "female"})
#family1.born(name="Tal", age=0, gender="male")

#print("Family Members:", family1.get_members())
#print(f"Is Doron 18+? {family1.is_18('Doron')}")
#print(f"Is David 18+? {family1.is_18('David')}")
#family1.family_presentation()

#5
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(member)

class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)

    def add_member(self, member):
        if "power" not in member or "incredible_name" not in member:
            print("Every member of TheIncredibles must have a power and an incredible name!")
        else:
            super().add_member(member)

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}!")
                else:
                    raise Exception(f"{name} is not over 18 and cannot use their power!")

    def incredible_presentation(self):
        print("**Here is our powerful family**")
        super().family_presentation()

incredible_family = TheIncredibles("Parr")

incredible_family.add_member({"name": "Bob", "age": 40, "gender": "Male", "power": "Super strength", "incredible_name": "Mr. Incredible"})
incredible_family.add_member({"name": "Helen", "age": 38, "gender": "Female", "power": "Elasticity", "incredible_name": "Elastigirl"})
incredible_family.add_member({"name": "Violet", "age": 16, "gender": "Female", "power": "Invisibility", "incredible_name": "VJ"})
incredible_family.add_member({"name": "Dash", "age": 10, "gender": "Male", "power": "Super speed", "incredible_name": "Dash"})
incredible_family.add_member({"name": "Michael", "age": 35, "gender": "Male", "power": "Fly", "incredible_name": "MikeFly"})
incredible_family.add_member({"name": "Sarah", "age": 32, "gender": "Female", "power": "Read minds", "incredible_name": "SuperWoman"})
incredible_family.born(name="Jack", age=0, gender="Male", power="Unknown Power", incredible_name="Baby Jack")


incredible_family.incredible_presentation()
incredible_family.use_power("Bob")
incredible_family.use_power("Helen")


