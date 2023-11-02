import pandas as pd

# SUB ACCOUNT 1

# dictionary of pandas dataframes
frames_sub1 = {
    "prev_actives": pd.DataFrame(), "prev_pending": pd.DataFrame(), "prev_paid": pd.DataFrame(),
    "actives": pd.DataFrame(), "unclaimed": pd.DataFrame()}

# read the dataframes from excel
for frame in frames_sub1:

    frames_sub1[frame] = pd.read_excel("review_data_sub1.xlsx", sheet_name=frame)

    # remove all whitespaces and null values
    frames_sub1[frame] = frames_sub1[frame].fillna(0)
    for column in frame:

        for value in column:

            value = value.strip()

# SUB ACCOUNT 2
frames_sub2 = {
    "prev_actives": pd.DataFrame(), "prev_pending": pd.DataFrame(), "prev_paid": pd.DataFrame(),
    "actives": pd.DataFrame(), "unclaimed": pd.DataFrame()}

# read the dataframes from excel
for frame in frames_sub2:

    frames_sub2[frame] = pd.read_excel("review_data_sub2.xlsx", sheet_name=frame)

    # remove all whitespaces and null values
    frames_sub2[frame] = frames_sub2[frame].fillna(0)
    for column in frame:

        for value in column:

            value = value.strip()
