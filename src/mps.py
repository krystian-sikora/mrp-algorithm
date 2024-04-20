# Master Production Schedule (MPS) class
class Mps:
    def __init__(self, bom, demand):
        self.bom = bom
        self.table = {
            "week" : [x for x in range(1,10)],
            "available" : [0 for x in range(1,10)],
            "anticipated_demand" : demand,
            "production" : [0 for x in range(1,10)]
        }
        self.calculate_ghp()

    def calculate_ghp(self):
        # initial available stock is equal to the available stock from the bom
        self.table["available"][0] = self.bom["available"] 

        self.calculate_available()
        self.calculate_production()
 

    def calculate_available(self, i=1):
        for i in range(i, 9):
            self.table["available"][i] = self.table["available"][i-1] - self.table["anticipated_demand"][i] + self.table["production"][i]

    def calculate_production(self):
        for i in range(1, 9):
            if self.table["available"][i] < 0:
                self.table["production"][i] = abs(self.table["available"][i])
                self.table["available"][i] = 0
                self.calculate_available(i)

