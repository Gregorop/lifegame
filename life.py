from random import randint,choice
from colors import *

class Life:
    all_lifes = []
    all_genders = ['male','female','bimale']

    def __init__(self, cell, sex):
        if cell.value: return None

        self.sex = sex
        self.cell = cell
        self.cell.value = self

        if sex == 'male':
            self.color = RED
        elif sex == 'female':
            self.color = GREEN
        elif sex == 'bimale':
            self.color = BLUE

        self.cell.color = self.color

        self.age = 0
        self.die_age = randint(0,100)

        Life.all_lifes.append(self)

    def spawn(n,field):
        for i in range(n):
            Life(choice(field.cells),choice(Life.all_genders))

    def die(self):
        self.cell.color = WHITE
        self.cell.value = 0
        Life.all_lifes.remove(self)

    def get_elder(self):
        self.age += 1
        if self.age > self.die_age:
            self.die()    
            return 0
        return 1

    def born_new(new_cell,life1,life2):
        if life1.age > 14 and life2.age > 14:
            if randint(0, 10) > 5:
                Life(new_cell,choice(Life.all_genders))

    def move(self):
        if self.get_elder():
            new_cell = choice(list(self.cell.nebgs.values()))
            if not new_cell.value:
                self.cell.color = WHITE
                self.cell.value = 0
                new_cell.color = self.color
                self.cell = new_cell
                self.cell.value = self
