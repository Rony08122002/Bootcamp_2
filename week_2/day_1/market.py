#class Market:
#    def __init__(self, name):
#        self.name = name
#        self.animals = {}
#    def add_animal(self, animal, count=1):
#        if animal in self.animals:
#            self.animals[animal] += count
#        else:
#            self.animals[animal] = count

#    def get_info(self):
#        info = f'{self.name} market\n'
#        for animal, count in sorted(self.animals.items()):
#            info += f"{animal} : {count}\n"
#        info += "!E-I-E-I-0"
#        return info

#macdonald = Market("McDonald")
#macdonald.add_animal('cow', 5)
#macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
#macdonald.add_animal('goat', 12)

#print(macdonald.get_info())

