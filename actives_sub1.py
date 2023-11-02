from read import*
from utility import*
from actives_calculations import*
from actives import exits_sub2
actives_sub1 = frames_sub1["actives"]
actives_sub2 = frames_sub2["actives"]

# lookup opening balances from previous schedules
employee_opening, employer_opening = opening_balances(actives_sub1, frames_sub1["prev_actives"])

# add opening balance columns to actives df
actives_sub1["EE Opening Balance"] = employee_opening
actives_sub1["ER Opening Balance"] = employer_opening

actives_sub1.to_excel("actives_computations_sub1.xlsx")

# identify and separate exits
exits_sub1 = actives_sub1
drop_index = []

for row_index in range(len(actives_sub1)):

    if any(member_ref == actives_sub1.loc[row_index, "Member Ref"] for member_ref in exits_sub2["Member Ref"]):

        drop_index.append(row_index)

exits_sub1.drop(index=drop_index)
actives_sub1.drop(index=drop_index)


exits_sub1.to_excel("exits_computations_sub1.xlsx")
actives_sub1.to_excel("actives_computations_sub1.xlsx")