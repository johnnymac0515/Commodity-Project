"""This module runs as a pseudo main function and data set into a dataframe. It requests the data 
   path stored locally by the user"""

import pandas as pd

def load_data(path):
    """load_data takes path and loads in the dataset identified in this project into a pandas df.
     It then prints high level informatio about the dataframe for the users reference and returns 
     this dataframe"""
    
    columns = ['Item Year', 'Original Value', 'Standard Value', 'Original Currency',  
               'Standard Currency', 'Orignal Measure', 'Standard Measure', 'Location',
               'Commodity', 'Variety']
    
    au_df = pd.read_csv(path, usecols= columns)

    print(au_df.head())

if __name__ == '__main__':
    #Psuedo main function. This construct is the entry point for the tool.
    au_path = input("Enter the local file path for the Allen/Unger 'All Commodities' dataset\nPath: ")
    
    try:
        with open(au_path, 'r'): print('found')
    
    except FileNotFoundError:
        print('Could not find file at that location')

    try:
        au_path[len(au_path)-4:] == '.csv'  
    
    except AttributeError:
        print('Incorrect File type. File must be .csv')

    load_data(au_path)



