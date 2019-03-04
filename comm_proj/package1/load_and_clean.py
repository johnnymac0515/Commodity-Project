"""Module loads a dataframe, displays and stores high level data of the frame"""
#Welp looks like no real cleaning is necessary. Very clean dataset
import pandas as pd


def load_data(path):
    """load_data takes path and loads in the dataset identified in this project into a pandas df.
     It then prints high level information about the dataframe for the users reference and returns
     this dataframe"""

    columns = ['Item Year', 'Original Value', 'Standard Value', 'Original Currency',
               'Standard Currency', 'Orignal Measure', 'Standard Measure', 'Location',
               'Commodity']
    col_type = [int, float, float, object, object, object, object, object]

    col_type_dict = dict(zip(columns, col_type))

    au_df = pd.read_csv(path, usecols=columns)
    au_df = au_df.astype(col_type_dict)
    au_df.name = 'AU_data'
    
    return au_df, columns