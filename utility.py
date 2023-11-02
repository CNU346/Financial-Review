# GLOBALS
from read import frames_sub1, frames_sub2
interest = 0.12
max_interest = 0
num_of_months = 12


def add_totals(frame):

    '''ADDS A ROW OF THE TOTAL OF COLUMNS AT THE END OF A DATA FRAME'''
    totals = []
    for column in frame:
        try:
            column_total = sum(frame[column])
        except:
            column_total = 0

        totals.append(column_total)
    # write the totals at the end of the data frame
    frame.loc[len(frame)] = totals


def lookup(lookup_value, lookup_column, lookup_frame, return_column):
    '''LOOKUP A VALUE FOR ONE FIELD IN THE DATA FRAME AND RETURN A VALUE IN ANOTHER FIELD OF THE DATA FRAME'''

    for row_index in range(len(lookup_frame)):

        if lookup_frame.loc[row_index, lookup_column] == lookup_value:

            return lookup_frame.loc[row_index, return_column]
    return 0   # not found


def opening_balance(member_ref, prev_schedule):
    '''LOOKUP THE OPENING BALANCES FOR ONE MEMBER'''

    ee = lookup(member_ref, "Member Ref", prev_schedule, "Employee Closing Balance")
    er = lookup(member_ref, "Member Ref", prev_schedule, "Employer Closing Balance")

    return ee, er


def opening_balances(current_schedule, prev_schedule):
    '''LOOKUP Balances from prev_schedule'''

    employee_opening = []
    employer_opening = []
    for member_ref in current_schedule["Member Ref"]:
        # lookup closing balance from previous schedule
        ee, er = opening_balance(member_ref, prev_schedule)
        employee_opening.append(ee)
        employer_opening.append(er)

    return employee_opening, employer_opening

