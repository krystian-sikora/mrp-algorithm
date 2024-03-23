class Mrp:
    def __init__(self, bom, parent):
        self.bom = bom
        self.parent = parent
        self.tabela_mrp = {
            "okres" : [x for x in range(1,6)],
            "całkowite_zapotrzebowanie" : [0 for x in range(1,6)],
            "planowane_przyjęcia" : [0 for x in range(1,6)],
            "przewidywane_na_stanie" : [0 for x in range(1,6)],
            "zapotrzebowanie_netto" : [0 for x in range(1,6)],
            "planowane_zamówienia" : [0 for x in range(1,6)],
            "planowane_przyjęcia_zamówień" : [0 for x in range(1,6)]
        }

    def get_mrp(self):
        return self.bom