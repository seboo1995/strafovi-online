import pandas as pd


def read_data(s):


    df = pd.read_csv(s+'.csv')

    # change all dtypes to string

    data_types_dict = {}

    for i in df.columns:
        data_types_dict[i] = str

    df = df.astype(data_types_dict)

    return df

