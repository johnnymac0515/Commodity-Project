"""This module runs as a pseudo main function and data set into a dataframe. It requests the data 
   path stored locally by the user"""

import pandas as pd
import sys

def load_data(path):
    """load_data takes path and loads in the dataset identified in this project into a pandas df.
     It then prints high level information about the dataframe for the users reference and returns 
     this dataframe"""
    
    columns = ['Item Year', 'Original Value', 'Standard Value', 'Original Currency',  
               'Standard Currency', 'Orignal Measure', 'Standard Measure', 'Location',
               'Commodity']
    col_type = [int, float, float, object, object, object, object, object]
    
    col_type_dict = dict(zip(columns, col_type))
   
    au_df = pd.read_csv(path, usecols= columns)
    au_df = au_df.astype(col_type_dict)
    au_df.name = 'AU_data'
    au_df_trunc = au_df.iloc[1:50]
    au_df_trunc.to_csv('/Users/johnmacnamara/Desktop/test_data2.csv')
    return au_df


def main():
    """Psuedo main function."""
    # TODO replace below with argparser at some point
        
    au_path = input("Enter the local file path for the Allen/Unger 'All Commodities' dataset\nPath: ")
    
    try:
        with open(au_path, 'r'): pass
    
    except FileNotFoundError:
        print('Could not find file at that location')

    try:

        if au_path[len(au_path)-4:] != '.csv':
            raise AttributeError 
        
    except AttributeError:
        print('Incorrect File type. File must be .csv')

    load_data(au_path) 

if __name__ == '__main__':
    # This construct is the entry point for the tool.
    # sys.exit(main())
    main()
    



