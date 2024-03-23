
import pandas as pd

class Ghp:
    def __init__(self, bom):
        self.bom = bom
        self.tabela_ghp = {
            "tydzień" : [x for x in range(1,10)],
            "dostępne" : [0 for x in range(1,10)],
            "przewidywany_popyt" : [0,0,0,5,0,30,0,20,0],
            "produkcja" : [0 for x in range(1,10)]
        }
        self.oblicz_ghp()

    def oblicz_ghp(self):
        # początkowy stan magazynu z założeniem braku popytu
        self.tabela_ghp["dostępne"][0] = self.bom.bom["dron"]["dostępne"] 

        self.oblicz_dostepność()
        self.oblicz_produkcje()
 

    def oblicz_dostepność(self, i=1):
        for i in range(i, 9):
            self.tabela_ghp["dostępne"][i] = self.tabela_ghp["dostępne"][i-1] - self.tabela_ghp["przewidywany_popyt"][i] + self.tabela_ghp["produkcja"][i]

    def oblicz_produkcje(self):
        for i in range(1, 9):
            if self.tabela_ghp["dostępne"][i] < 0:
                self.tabela_ghp["produkcja"][i] = abs(self.tabela_ghp["dostępne"][i])
                self.tabela_ghp["dostępne"][i] = 0
                self.oblicz_dostepność(i)

