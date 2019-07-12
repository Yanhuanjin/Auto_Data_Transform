import pandas as pd
import numpy as np
import sys
from sklearn.preprocessing import LabelEncoder
import re

"""
A project writen in Python to convert any data in .csv format to fully digital data.
Like this:
>> Input: Good, Bad, Good
>> Output: 1, 0, 1 
>> Input: 2019-01-01, 2019-01-02, 2019-01-03
>> Output: 1, 2, 3
>> Usage: python data_interface.py target.csv
>> OUT: target_out.csv
"""

def load_data(filename):
    df = pd.read_csv(filename)
    return df

def specify_types(df, column_label):
    """
    Read the columns' name of the read_csv and return their types,
    like: Time Categories Strings Num
    :return: types in (Time Categories Strings Num)
    """
    data_1 = str(df[column_label][1])
    if data_1.isdigit():
        return(np.array(df[column_label]))
    else:
        flag_is_date = date_check(data_1)
        if flag_is_date:
            return(np.array(date_transform(df, column_label)))
        else:
            return(np.array(string_transform(df, column_label)))

def date_check(data):
    """
    :param data:
    :return whether a data is a date form:
    """
    pattern = re.compile(r"\d{1,4}(/|-)\d{1,2}(/|-)\d{1,2}")
    match = pattern.match(data)
    if match:
        return True
    else:
        return False

def date_transform(data_frame, label):
    """
    Transform the time format data to int (day_of_year\day\month)
    :return: day_of_year(now)
    """
    return pd.to_datetime(data_frame[label]).dt.dayofyear

def categories_transform():
    """
    OneHotEncoding of the categories
    :return: have not been finished yet
    """
    pass

def string_transform(df, string):
    """
    LabelEncoding of the strings
    :return: int
    """
    le = LabelEncoder()
    labeled_columns = le.fit_transform(df[string])
    return labeled_columns

def main():
    # Load data
    filename = sys.argv[1]
    df = load_data(filename)
    string_list = list()

    # Data_transform
    for column_label in df.columns:
        string_list.append(specify_types(df, column_label))

    # Save to .csv
    num_array = np.array(string_list).transpose()
    data = pd.DataFrame(num_array, columns=list(df.columns))
    out_file = filename.split(".")[0] + "_out.csv"
    data.to_csv(out_file)


if __name__ == "__main__":
    main()