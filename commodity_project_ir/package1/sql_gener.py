"""This module creates a local SQL 'database' for the tools dataset.""" 


import sqlite3
from functools import reduce


def map_dftype_to_sqldtype(df):
    """Takes (at a minimum 1 row of) DataFrame object and combines the Column Name and dtype of the 
    DF that and maps them to useable column parameters and SQL types (supported by sqlite)""" 
    
    data_type_map = {'i':'INTEGER', 'f':'REAL', 'None':'NULL', 'O':'TEXT'}

    df_cols = list(df.columns)[1:]
    
    df_types_list = [ df[col].dtype.kind for col in df_cols ] 
    sql_types_list = [ data_type_map[i] for i in df_types_list ]

    #Now We need to remove white space from column names so that work as SQL Column parameters
    #A reduce, a lambda, and a list comprehension all in one line....sometime I cant help but impress myself, super unreadable though
    sql_col = [reduce((lambda a, b: a + b), col_name.split(' ')) for col_name in list(df_cols)] 

    #Now we'll create a list of strings where each element is the 'colparam DATATYPE' string
    sql_table_arg_list = [ "{name} {type}".format(name=sql_col[i], type=sql_types_list[i]) for i in list(range(len(sql_col)-1))]
    print(sql_table_arg_list)
    return sql_table_arg_list

# def sql_from_data(df):
#     """Creates a local sql dataframe using 'sqlite3'. The db is named after the passed dataframe.
#     i.e. if df.name = 'data_set' then the database is named 'data_set.db'"""
    
#     conn = sqlite3.connect("{name}.db".format(name=df.name))

#     cursor = conn.cursor()

#     column_tup = tuple(df.columns())

def table_create_str(arg_list, name):
    """Returns a sqlite3 create_table string argument from the name of the table and 
       map_dftype_to_sqldtype(map) argument list"""

    #    TODO

    return None


class sql_database(object):

    def __init__(self, df):
       self.df = df
    
    def __repr__(self):
        self.name = "SQL database class object for {dfname} dataframe".format(dfname= df.name)

    def create_db(self):
        conn = sqlite3.connect("{name}.db".format(name=df.name))

        curs = conn.cursor()

    def create_table(self):
        create_table_state = "CREATE TABLE IF NOT EXISTS au_sql_table {df_column_tuble}" 


import pandas as pd
df = pd.read_csv('/Users/johnmacnamara/Desktop/test_data2.csv')
map_dftype_to_sqldtype(df)