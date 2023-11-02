from read import*
from utility import*
from actives_calculations import*

actives_sub2 = frames_sub2["actives"]


# SUB ACCOUNT 2

# separate reserve
actives_sub2 = separate_reserve(actives_sub2)

# Drop EEGross and ERGross
actives_sub2 = drop_gross(actives_sub2)

# lookup opening balances from previous schedules
employee_opening, employer_opening = opening_balances(actives_sub2, frames_sub2["prev_actives"])

# add opening balance columns to actives df
actives_sub2["EE Opening Balance"] = employee_opening
actives_sub2["ER Opening Balance"] = employer_opening

# contributions
conts = contributions(actives_sub2, interest, num_of_months)

# before interests
employee_cont_before_interest, employer_cont_before_interest, reserve_cont_before_interest = conts["before_interest"]

# after interests
employee_cont_after_interest, employer_cont_after_interest, reserve_cont_after_interest = conts["after_interest"]
employee_opening_with_i = [opening * (1 + interest) for opening in employee_opening]
employer_opening_with_i = [opening * (1 + interest) for opening in employer_opening]


# closing balances
employee_closing = [opening + cont for opening, cont in zip(employee_opening_with_i, employee_cont_after_interest)]
employer_closing = [opening + cont for opening, cont in zip(employer_opening_with_i, employer_cont_after_interest)]


# add columns
actives_sub2["EE cont Before i"] = employee_cont_before_interest
actives_sub2["ER cont Before i"] = employer_cont_before_interest
actives_sub2["Reserve cont Before i"] = reserve_cont_before_interest
actives_sub2["EE Opening with i"] = employee_opening_with_i
actives_sub2["ER Opening with i"] = employer_opening_with_i
actives_sub2["EE cont with i"] = employee_cont_after_interest
actives_sub2["ER cont with i"] = employer_cont_after_interest
actives_sub2["Reserve cont with i"] = reserve_cont_after_interest
actives_sub2["EE Closing Balance"] = employee_closing
actives_sub2["ER Closing Balance"] = employer_closing


actives_sub2.to_excel("actives_computations_sub2.xlsx")

# identify and separate exits of the period
exits_sub2 = pd.read_excel("actives_computations_sub2.xlsx", nrows=0)  # empty data frame with the headings of actives
exits_sub2 = exits_sub2.fillna(0)
actives_sub2_copy = actives_sub2
for row_index in range(len(actives_sub2_copy)):

    # check for December contribution
    if actives_sub2_copy.loc[row_index, "Dec2022 ERNet"] == 0 and actives_sub2_copy.loc[row_index, "Member Ref"] != 0:
        exits_sub2.loc[len(exits_sub2)] = actives_sub2_copy.loc[row_index]
        actives_sub2 = actives_sub2.drop(index=row_index)

exits_sub2.to_excel("exits_computations_sub2.xlsx")





