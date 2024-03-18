class Thing:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Inanimate(Thing):
    pass

class Animate(Thing):
    pass

class Sidewalk(Inanimate):
    pass

class Animal(Animate):
    def breathe(self):
        print(f'{self.name} breathing')
    def move(self):
        print(f'{self.name} moving')
    def eat_food(self):
        print(f'{self.name} eating food')

class Mammal(Animal):
    def feed_young_with_milk(self):
        print(f'{self.name} feeding young')

class Giraffe(Mammal):
    def find_food(self):
        print(f'{self.name} finding food')
        self.move()
        print(f'{self.name} found leaves on a tree')
        self.eat_leaves_from_trees()
    def eat_leaves_from_trees(self):
        print(f'{self.name} eating leaves')
    def what_color(self):
        print(f'{self.name} is {self.color}')


reginald = Giraffe('Reginald', 'Brown')
harriet = Giraffe('Harriet', 'Purple')

reginald.move()
harriet.eat_food()
reginald.find_food()
reginald.what_color()
harriet.what_color()