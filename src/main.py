import pandas as pd
import mps, mrp, bom, table
import tkinter as tk
from functools import partial

bom_class = bom.Bom()

details = ["quantity", "lead_time", "batch_size", "available"]
demand = [0 for x in range(0, 9)]
entries = []
component_instances = {}
root = tk.Tk()
demand_frame = tk.Frame(root)
menu_frame = tk.Frame(root)
demand_frame.grid()
menu_frame.grid()


def print_components(json_obj, parent=None):
    for component in json_obj:
        if component not in details:
            print(component)
            parent_obj = create_df(json_obj[component], parent)
            component_instances[component] = parent_obj.table
            print_components(json_obj[component], parent_obj)
    
def create_df(component_bom, parent=None):
    if parent is None:
        mps_component = mps.Mps(component_bom, demand)
        print('=' * 20)
        print(pd.DataFrame(mps_component.table))
        return mps_component
    else:
        mrp_component = mrp.Mrp(component_bom, parent)
        print('=' * 20)
        print(pd.DataFrame(mrp_component.table))
        return mrp_component
    
def create_table(component):
    table_frame = tk.Frame(root)
    table_frame.grid()
    table.Table(table_frame, component_instances[component], component)
    print('****')

def create_menu():
    for component in component_instances:
        tk.Button(menu_frame, text=f"{component}", command=partial(create_table, component)).pack()
    
def submit():
    for i in range(0, 9):
        demand[i] = int(entries[i].get())
    print_components(bom_class.bom)
    demand_frame.destroy()
    create_menu()

def set_labels():
    for number in range(1, 10):
        entry = tk.Entry(demand_frame)
        tk.Label(demand_frame, text="Week").grid(row=1, column=0)
        tk.Label(demand_frame, text=f"{number}").grid(row=1, column=number + 1)
        tk.Label(demand_frame, text="Demand").grid(row=2, column=0)
        entry.insert(0, 0)
        entry.grid(row=2, column=number + 1)
        entries.append(entry)
        tk.Button(demand_frame, text="Submit", command=submit).grid(row=3, columnspan=10)

def input_demand():
    tk.Label(demand_frame, text="Please enter expected demand for each week").grid(row=0, columnspan=10)
    set_labels()
    
    root.mainloop()

input_demand()




