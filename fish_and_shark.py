import random 
NB_ROWS, NB_COLUMNS = 8, 15
PROBA_FISH, PROBA_SHARK = 30/100, 10/100
# ∞
class Ocean:
    
    def __init__(self):
        self.water = []
        self.fishes = 0
        self.sharks = 0

    def create_fishes(self):
        if random.random() < PROBA_FISH:
            return 1
        else:
            return 0
    
    def create_sharks(self):
        if random.random() < PROBA_SHARK:
            return 1
        else:
            return 0

    def create_and_populate_water(self):
        for i in range (NB_ROWS):
            row = []
            for j in range(NB_COLUMNS):
                if self.create_fishes() != 0:
                    row.append(" ∞ ")
                    self.fishes+= 1
                elif self.create_sharks() != 0:
                    row.append(" ^ ")
                    self.sharks+= 1
                else: 
                    row.append(" - ")
            self.water.append(row)

    def show_water(self):
        print("  " + "-"*60)
        for row in self.water:
            print(' |', end="")
            for item in row:
                print(item, end=" ")
            print("| ")
        print("  " + "-"*60)

    def start(self):
        self.create_and_populate_water()
        print()
        self.show_water()

Ocean = Ocean()
Ocean.start()