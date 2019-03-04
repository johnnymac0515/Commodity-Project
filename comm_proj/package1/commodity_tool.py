"""This module runs as a pseudo main function and data set into a dataframe. It requests the data
   path stored locally by the user"""

import sys
import pandas as pd 
import comm_proj.package1.sql_gener as sql_gener
import comm_proj.package1.load_and_clean as load_and_clean
import comm_proj.package1.plotter as plotter

def build_database(dataframe, name):
    """Builds SQLite3 database for querying commodity data and returns database object"""
    database = sql_gener.SqlDatabase(dataframe, name)
    database.create_db()
    database.create_curs()
    database.create_table()
    database.insert_data()
    
    return database

def query_data(database, location, commodity):

    data = database.select_data(select='*', Location=location, Commodity=commodity)
    return data

def select_data(df):

    while True:
    
        print("Select a location (Country/Region) from the below list\n")
        location_list = list(df["Location"].unique())
        [print(loc) for loc in location_list]
        location = input("\nLocation: ")

        if location in location_list:
            break
        elif not location:
            return 0, 0
        else:
            print("Couldn't find location. Try again\n")
            continue
  


    while True:

        print("Select a Commodity from the below list found in {}\n".format(location))
        commodity_list = list(df[df['Location']==location]["Commodity"].unique())
        [print(com) for com in commodity_list]
        commodity = input("\nCommodity: ")

        if commodity in commodity_list:
            break
        elif not commodity:
            return 0, 0
        else:
            print("Couldn't find location. Try again\n")
            continue

    return location, commodity

def main():
    """Psuedo main function."""
    #replace below with argparser at some point

    au_path = input("Enter the local file path for the Allen/Unger 'All Commodities' \
    dataset\nPath: ")

    try:
        with open(au_path, 'r'):
            pass

    except FileNotFoundError:
        print('Could not find file at that location')

    try:

        if au_path[len(au_path)-4:] != '.csv':
            raise AttributeError

    except AttributeError:
        print('Incorrect File type. File must be .csv. Try again')
        main()

    dataframe, column_names = load_and_clean.load_data(au_path)
    database = build_database(dataframe, 'commodity_database')
    
    
    while True:
        
        location, commodity = select_data(dataframe)
        
        if not location or not commodity:
            print('Goodbye')
            database.delete_database()
            sys.exit()
        
        data = query_data(database, location, commodity)
        new_dataframe = pd.DataFrame(data, columns=column_names)
        plotter.plotter(new_dataframe, location, commodity)
        
if __name__ == '__main__':
    # This construct is the entry point for the tool.
    # sys.exit(main()) TODO uncomment for release. debug only
    main()
