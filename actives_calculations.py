import pandas as pd


def separate_reserve(schedule):
    '''SEPARATES ERGross in schedule into ERNet and Reserve'''

    schedule_copy = schedule
    i = 0  # for tracking column index
    for column in schedule_copy:
        i += 1

        if "ERGross" in column:
            # take the date of the ERGross
            _date = column.strip("ERGross")
            # use date to get the corresponding ERNet
            _net = _date + "ERNet"

            # calculate Reserve
            reserve = []
            for row_index in range(len(schedule_copy)):
                reserve.append(
                    schedule.loc[row_index, column] - schedule.loc[row_index, _net]  # ERGross - ERNet
                )
            _reserve = _date + "Reserve"

            schedule.insert(i, _reserve, reserve)
    return schedule


def drop_gross(schedule):
    '''DROP EEGross and ERGross from the schedule'''
    drop_columns = []
    for column in schedule:

        if "EEGross" in column or "ERGross" in column:
            drop_columns.append(column)
    schedule = schedule.drop(columns=drop_columns)
    return schedule


def contributions(schedule, interest, num_of_months):
    '''CALCULATES AND RETURNS:
    # ee-cont-before-interest
    # er-cont-before-interest
    # reserve-cont-before-int
    # ee-cont-after-interest
    # er-cont-after-interest
    # reserve-cont-after-int
    '''

    employee_cont_before_interest, employer_cont_before_interest, reserve_cont_before_interest = [], [], []
    employee_cont_after_interest, employer_cont_after_interest, reserve_cont_after_interest = [], [], []
    for row_index in range(len(schedule)):
        ee, er, r = [], [], []  # before interest
        ee_i, er_i, r_i = [], [], []  # after interest

        for column in schedule:
            ee_month = 0
            er_month = 0
            r_month = 0

            if "EENet" in column:
                ee_month += 1
                ee.append(schedule.loc[row_index, column])
                ee_i.append(schedule.loc[row_index, column] * pow(1 + interest, (num_of_months - ee_month) / num_of_months))
            elif "ERNet" in column:
                er_month += 1
                er.append(schedule.loc[row_index, column])
                er_i.append(schedule.loc[row_index, column] * pow(1 + interest, (num_of_months - er_month) / num_of_months))
            elif "Reserve" in column:
                r_month += 1
                r.append(schedule.loc[row_index, column])
                r_i.append(schedule.loc[row_index, column] * pow(1 + interest, (num_of_months - r_month) / num_of_months))

        # before interest
        employee_cont_before_interest.append(sum(ee))
        employer_cont_before_interest.append(sum(er))
        reserve_cont_before_interest.append(sum(r))

        # after interest
        employee_cont_after_interest.append(sum(ee_i))
        employer_cont_after_interest.append(sum(er_i))
        reserve_cont_after_interest.append(sum(r_i))

    return {"before_interest": (employee_cont_before_interest, employer_cont_before_interest,
            reserve_cont_before_interest),
            "after_interest": (employee_cont_after_interest, employer_cont_after_interest,
            reserve_cont_after_interest)}




