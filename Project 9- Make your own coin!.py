import random

class Pound:
    value = 1.25
    color = "gold"
    num_edges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True

    def __int__(self,rare = False):
        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.color = color
        self.num_edges = num_edges
        self.diameter = diameter
        self.thickness = thickness 
        self.heads = heads

    def __del__(self):
        print("Coin Spent!")
        
    def rust(self):
        self.color ="green"

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice



