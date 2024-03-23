import ghp
import bom
import pandas as pd

my_bom = bom.Bom()
my_ghp = ghp.Ghp(my_bom)
data = my_ghp.tabela_ghp
data = pd.DataFrame(data)
print("TABELA GHP")
print(data)
