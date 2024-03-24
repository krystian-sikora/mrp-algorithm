

class Mrp:
    def __init__(self, bom, parent):
        self.bom = bom
        self.parent = parent
        self.is_ghp = self.is_parent_ghp(parent)
        self.rozmiar_tabeli = 10
        self.tabela = {
            "okres" : [x for x in range(1, self.rozmiar_tabeli)],
            "całkowite_zapotrzebowanie" : [0 for x in range(1, self.rozmiar_tabeli)],
            "planowane_przyjęcia" : [0 for x in range(1, self.rozmiar_tabeli)],
            "przewidywane_na_stanie" : [0 for x in range(1, self.rozmiar_tabeli)],
            "zapotrzebowanie_netto" : [0 for x in range(1, self.rozmiar_tabeli)],
            "planowane_zamówienia" : [0 for x in range(1, self.rozmiar_tabeli)],
            "planowane_przyjęcia_zamówień" : [0 for x in range(1, self.rozmiar_tabeli)]
        }
        self.oblicz_mrp()

    def oblicz_mrp(self):
        self.oblicz_zapotrzebowanie()
        self.oblicz_przewidywane_na_stanie()

    def oblicz_zapotrzebowanie(self):
        for i in range(1, self.rozmiar_tabeli - 1):
            if self.is_ghp:
                produkcja = self.parent.tabela["produkcja"][i]
            else:
                produkcja = self.parent.tabela["planowane_zamówienia"][i]

            self.tabela["całkowite_zapotrzebowanie"][i - self.parent.bom["czas_realizacji"]] = produkcja
    
    def oblicz_przewidywane_na_stanie(self):
        self.tabela["przewidywane_na_stanie"][0] = self.bom["dostępne"]
        for i in range(1, self.rozmiar_tabeli - 1):
            self.tabela["przewidywane_na_stanie"][i] = self.tabela["przewidywane_na_stanie"][i-1] - self.tabela["całkowite_zapotrzebowanie"][i]
            if self.tabela["przewidywane_na_stanie"][i] < 0:
                self.tabela["zapotrzebowanie_netto"][i] = abs(self.tabela["przewidywane_na_stanie"][i])
                if i - self.bom["czas_realizacji"] < 0:
                    print("nie można zamawiać na datę wstecz")
                self.tabela["planowane_zamówienia"][i - self.bom["czas_realizacji"]] = self.bom["wielkość_partii"]
                self.tabela["planowane_przyjęcia_zamówień"][i] = self.bom["wielkość_partii"]
                self.tabela["przewidywane_na_stanie"][i] = self.tabela["przewidywane_na_stanie"][i] + self.tabela["planowane_przyjęcia_zamówień"][i]

    def is_parent_ghp(self, parent):
        if "produkcja" in parent.tabela:
            return True
        else:
            return False
        