import json

# Bill of Materials (BOM) class
class Bom:
    def __init__(self):
        # self.bom = json.load(open('./src/resources/bom.json', 'r'))
        try:
            self.bom = json.load(open('bom.json', 'r'))
        except:
            self.bom = open('bom.json', 'w')
            jsonString = json.dumps({
                    "drone" : {
                        "lead_time": 1,
                        "available": 5,
                        "body" : {
                            "quantity": 1,
                            "lead_time": 2,
                            "batch_size": 20,
                            "available": 3,
                            "battery": {
                                "quantity": 2,
                                "lead_time": 2,
                                "batch_size": 30,
                                "available": 22
                            },
                            "motor": {
                                "quantity": 1,
                                "lead_time": 1,
                                "batch_size": 20,
                                "available": 3
                            },
                            "case": {
                                "quantity": 1,
                                "lead_time": 2,
                                "batch_size": 40,
                                "available": 22
                            }
                        },
                        "propellers": {
                            "quantity": 4,
                            "lead_time": 1,
                            "batch_size": 50,
                            "available": 30
                        }
                    }
                })
            self.bom.write(jsonString)
            self.bom.close()
            self.bom = json.load(open('bom.json', 'r'))
my_bom = Bom()