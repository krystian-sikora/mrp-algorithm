import pandas as pd
import ghp, mrp, bom

# GHP dron
bom_dron = bom.Bom().bom["dron"]
ghp_dron = ghp.Ghp(bom_dron)
dronDf = pd.DataFrame(ghp_dron.tabela)
print("TABELA GHP")
print(dronDf)

# MRP kadłub
bom_kadlub = bom.Bom().bom["dron"]["kadłub"]
mrp_kadlub = mrp.Mrp(bom_kadlub, ghp_dron)
kadlubDf = pd.DataFrame(mrp_kadlub.tabela)
print("TABELA MRP kadłub")
print(kadlubDf)

# MRP bateria
bom_bateria = bom.Bom().bom["dron"]["kadłub"]["bateria"]
mrp_bateria = mrp.Mrp(bom_bateria, mrp_kadlub)
bateriaDf = pd.DataFrame(mrp_bateria.tabela)
print("TABELA MRP bateria")
print(bateriaDf)

# MRP silnik
bom_silnik = bom.Bom().bom["dron"]["kadłub"]["silnik"]
mrp_silnik = mrp.Mrp(bom_silnik, mrp_kadlub)
silnikDf = pd.DataFrame(mrp_silnik.tabela)
print("TABELA MRP silnik")
print(silnikDf)

# MRP obudowa
bom_obudowa = bom.Bom().bom["dron"]["kadłub"]["obudowa"]
mrp_obudowa = mrp.Mrp(bom_obudowa, mrp_kadlub)
obudowaDf = pd.DataFrame(mrp_obudowa.tabela)
print("TABELA MRP obudowa")
print(obudowaDf)

# MRP śmigła
bom_smigla = bom.Bom().bom["dron"]["śmigła"]
mrp_smigla = mrp.Mrp(bom_smigla, ghp_dron)
smiglaDf = pd.DataFrame(mrp_smigla.tabela)
print("TABELA MRP śmigła")
print(smiglaDf)