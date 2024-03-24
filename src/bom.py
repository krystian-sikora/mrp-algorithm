import json

# Bill of Materials (BOM) class
class Bom:
    def __init__(self):
        self.bom = json.load(open('./src/resources/bom.json', 'r'))
    
my_bom = Bom()