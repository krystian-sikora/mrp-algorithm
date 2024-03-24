class Ghp:
    def __init__(self, bom):
        self.bom = bom
        self.tabela = {
            "tydzień" : [x for x in range(1,10)],
            "dostępne" : [0 for x in range(1,10)],
            "przewidywany_popyt" : [0, 0, 0, 0, 0, 0, 10, 0, 20],
            "produkcja" : [0 for x in range(1,10)]
        }
        self.oblicz_ghp()

    def oblicz_ghp(self):
        # początkowy stan magazynu z założeniem braku popytu
        self.tabela["dostępne"][0] = self.bom["dostępne"] 

        self.oblicz_dostepność()
        self.oblicz_produkcje()
 

    def oblicz_dostepność(self, i=1):
        for i in range(i, 9):
            self.tabela["dostępne"][i] = self.tabela["dostępne"][i-1] - self.tabela["przewidywany_popyt"][i] + self.tabela["produkcja"][i]

    def oblicz_produkcje(self):
        for i in range(1, 9):
            if self.tabela["dostępne"][i] < 0:
                self.tabela["produkcja"][i] = abs(self.tabela["dostępne"][i])
                self.tabela["dostępne"][i] = 0
                self.oblicz_dostepność(i)

