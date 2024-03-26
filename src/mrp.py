# Material Requirements Planning (MRP) class
class Mrp:
    def __init__(self, bom, parent):
        self.bom = bom
        self.parent = parent
        self.is_ghp = self.is_parent_ghp(parent)
        self.table_size = 10
        self.table = {
            "week" : [x for x in range(1, self.table_size)],
            "total_demand" : [0 for x in range(1, self.table_size)],
            "scheduled_admissions" : [0 for x in range(1, self.table_size)],
            "stock_prediction" : [0 for x in range(1, self.table_size)],
            "net_demand" : [0 for x in range(1, self.table_size)],
            "planned_orders" : [0 for x in range(1, self.table_size)],
            "scheduled_order_admissions" : [0 for x in range(1, self.table_size)]
        }
        self.calculate_mrp()

    def calculate_mrp(self):
        self.calculate_demand()
        self.calculate_stock()

    def calculate_demand(self):
        for i in range(1, self.table_size - 1):
            if self.is_ghp:
                production = self.parent.table["production"][i]
            else:
                production = self.parent.table["planned_orders"][i]

            self.table["total_demand"][i - self.parent.bom["lead_time"]] = production
    
    def calculate_stock(self):
        self.table["stock_prediction"][0] = self.bom["available"]
        for i in range(1, self.table_size - 1):
            self.table["stock_prediction"][i] = self.table["stock_prediction"][i-1] - self.table["total_demand"][i]
            if self.table["stock_prediction"][i] < 0:
                self.table["net_demand"][i] = abs(self.table["stock_prediction"][i])
                if i - self.bom["lead_time"] < 0:
                    print("Can't set order date in the past")   
                self.table["planned_orders"][i - self.bom["lead_time"]] = self.bom["batch_size"]
                self.table["scheduled_order_admissions"][i] = self.bom["batch_size"]
                self.table["stock_prediction"][i] = self.table["stock_prediction"][i] + self.table["scheduled_order_admissions"][i]

    def is_parent_ghp(self, parent):
        if "production" in parent.table:
            return True
        else:
            return False
        