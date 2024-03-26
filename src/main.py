import pandas as pd
import mps, mrp, bom

# GHP drone
bom_drone = bom.Bom().bom["drone"]
ghp_drone = mps.Mps(bom_drone)
droneDf = pd.DataFrame(ghp_drone.table)
print("GHP TABLE drone")
print(droneDf)

# MRP body
bom_body = bom.Bom().bom["drone"]["body"]
mrp_body = mrp.Mrp(bom_body, ghp_drone)
bodyDf = pd.DataFrame(mrp_body.table)
print("MRP TABLE body")
print(bodyDf)

# MRP battery
bom_battery = bom.Bom().bom["drone"]["body"]["battery"]
mrp_battery = mrp.Mrp(bom_battery, mrp_body)
batteryDf = pd.DataFrame(mrp_battery.table)
print("MRP TABLE battery")
print(batteryDf)

# MRP motor
bom_motor = bom.Bom().bom["drone"]["body"]["motor"]
mrp_motor = mrp.Mrp(bom_motor, mrp_body)
motorDf = pd.DataFrame(mrp_motor.table)
print("MRP TABLE motor")
print(motorDf)

# MRP case
bom_case = bom.Bom().bom["drone"]["body"]["case"]
mrp_case = mrp.Mrp(bom_case, mrp_body)
caseDf = pd.DataFrame(mrp_case.table)
print("MRP TABLE case")
print(caseDf)

# MRP propellers
bom_propellers = bom.Bom().bom["drone"]["propellers"]
mrp_propellers = mrp.Mrp(bom_propellers, ghp_drone)
propellersDf = pd.DataFrame(mrp_propellers.table)
print("MRP TABLE propellers")
print(propellersDf)