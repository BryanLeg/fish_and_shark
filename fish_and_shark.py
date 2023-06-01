# https://scipython.com/blog/wa-tor-world/

import random 
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


NB_ROWS, NB_COLUMNS = 8, 15
PROBA_FISH, PROBA_SHARK = 30/100, 10/100
EMPTY = 0
FISH = 1
SHARK = 2

initial_energies = {FISH: 20, SHARK: 3}
fertility_thresholds = {FISH: 4, SHARK: 12}
# ∞

class Creatures:
    def __init__(self, id, x, y, energy, fertility_threshold):
        self.id = id
        self.x, self.y = x, y
        self.energy = energy
        self.fertility_threshold = fertility_threshold
        self.fertility = 0
        self.dead = False

class Ocean:
    
    def __init__(self, length=NB_ROWS, width=NB_COLUMNS):
        self.length, self.width = length, width
        self.ncells = length*width
        self.water = [[EMPTY]*width for y in range(length)]
        self.creatures = []

    def create_creature(self, creature_id: int, x: int, y:int):
        """Create a creature with an ID: creature_id at position x,y.

        Args:
            creature_id (int): ID de la creature, 1 for fish and 2 for shark
            x (int): horizontal position
            y (int): vertical position
        """
        creature = Creatures(creature_id, x, y, initial_energies[creature_id], fertility_thresholds[creature_id])
        self.creatures.append(creature)
        self.water[y][x] = creature

    def populate_water(self, nfish=120, nshark=40):
        self.nfish, self.nshark = nfish, nshark

        def place_creature(ncreatures, creature_id):
            for i in range(ncreatures):
                while True:
                    x, y = divmod(random.randrange(self.ncells), self.length)
                    if not self.water[x][y]:
                        self.create_creature(creature_id, x, y)
                        break

        place_creature(self.nfish, FISH)
        place_creature(self.nshark, SHARK)

    def get_water(self):
        return [[self.water[y][x].id if self.water[y][x] else 0
                    for x in range(self.width)] for y in range(self.length)]

