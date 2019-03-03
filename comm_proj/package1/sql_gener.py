"""This module creates a local SQL 'database' for the tools dataset."""


import sqlite3
from functools import reduce

def map_dftype_to_sqldtype(d_f):
    """Takes (at a minimum 1 row of) DataFrame object and combines the Column Name and dtype of the
    DF that and maps them to useable column parameters and SQL types (supported by sqlite), Also
    returns """

    data_type_map = {'i':'INTEGER', 'f':'REAL', 'None':'NULL', 'O':'TEXT'}

    df_cols = list(d_f.columns)

    df_types_list = [d_f[col].dtype.kind for col in df_cols]
    sql_types_list = [data_type_map[i] for i in df_types_list]

    #Now We need to remove white space from column names so that work as SQL Column parameters
    #A reduce, a lambda, and a list comprehension all in one line....sometime I cant help but
    # impress myself, super unreadable though
    sql_col = [reduce((lambda a, b: a + b), col_name.split(' ')) for col_name in list(df_cols)]
    #Now we'll create a list of strings where each element is the 'colparam DATATYPE' string
    sql_table_arg_list = ["{name} {type}".format(name=sql_col[i], type=sql_types_list[i]) for i \
    in list(range(len(sql_col)))]

    return sql_table_arg_list, sql_col

def table_create_str(arg_list, name):
    """Returns a sqlite3 CREATE TABLE string argument from the name of the table and
       map_dftype_to_sqldtype(map) argument list"""

    arg_list_str = reduce((lambda a, b: a + ', ' + b), arg_list)

    sql_table_str = """CREATE TABLE IF NOT EXISTS {table_name} ({arg_str});""".format(
        table_name=name, arg_str=arg_list_str)


    return sql_table_str

def sql_insert_str(param_size, table_name):
    """Returns a sqlite3 INSERT (many) string argument from the name of the table and
       the length of necessary"""

    insert_sql_string = "INSERT INTO " + table_name + " VALUES ({})".format(
        ','.join(param_size*'?'))

    return insert_sql_string

def dataframe_to_tup_list(d_f):
    """Returns a list of tuples containg dataframe row-wise data"""
    return [tuple(row) for row in d_f.values]

def sql_select_str(tablename, select='*', *, where=None):
    """Creates a simple 'SELECT {columns} FROM {table} SQL statement. Also can add WHERE
       table_column = stuff"""

    if isinstance(select, list):
        sel_str = reduce((lambda a, b: a + ' ,' + b), select)
    else:
        sel_str = select

        select_statement = "SELECT {stuff} FROM {table}".format(stuff=sel_str, table=tablename)

    if where is not None:
        where_str = " WHERE "
        where_list = []
        for key, value in where.items():
            where_list.append("{} = '{}'".format(key, value))

        select_statement += where_str + " and ".join(where_list)

    return select_statement

class SqlDatabase():
    """This sql_database object creates sqlite3 (local) databases to be populated with a
    dataframe data"""

    def __init__(self, d_f, name):
        if d_f is None:
            raise TypeError("__init__ missing 1 required positonal argument 'df'")
        elif name is None:
            raise TypeError("__init__ missing 1 required positonal argument 'name'")
        else:
            self.d_f = d_f
            self.df_name = name
            self.__repr__()
            self.table_name = name+'_table'
            self.conn = None
            self.curs = None
            self.table_cols = None

    def __repr__(self):
        self.db_name = "SQL database class object for {dfname} dataframe".format(
            dfname=self.df_name)
        return self.db_name

    def create_db(self):
        """Member function that creates a database from passed DataFrame if no database exists"""
        self.conn = sqlite3.connect("{}.db".format(str(self.df_name)))
        print('Creating Database {}.db....'.format(self.df_name))
        return self.conn

    def create_curs(self):
        """Creates cursor attribute"""
        if self.conn is not None:
            self.curs = self.conn.cursor()
            print('Establishing Cursor...')
            return self.curs

        self.create_db()
        self.create_curs()
        return None

    def create_table(self):
        """"Creates table with DataFrame Data"""
        if self.curs is not None:
            print('Creating table...')

            type_list, self.table_cols = map_dftype_to_sqldtype(self.d_f)
            table_create_statement = table_create_str(type_list, self.table_name)
            self.curs.execute(table_create_statement)
            self.curs.fetchone()


        else:
            self.create_curs()
            self.create_table()

    def insert_data(self):
        """Inserts data into database from DataFrame"""
        df_tup_list = dataframe_to_tup_list(self.d_f)
        ins_str = sql_insert_str(self.d_f.shape[1], self.table_name)
        self.curs.executemany(ins_str, df_tup_list)

    def select_data(self, select='*', **kwargs):
        """Member function generates a SQL SELECT statement string and executes the Query"""
        select_str = sql_select_str(self.table_name, select, where=kwargs)
        selected_data = self.curs.execute(select_str)
        return selected_data

    def display(self, *, size=1):
        """Stupid display function. NEEDS IMPROVEMENT"""
        self.curs.execute('SELECT * from {}'.format(self.table_name))
        # names = [description[0] for description in self.curs.description]
        return self.curs.fetchmany(size=size)
        #Displays database name, table and names, contents of created tables (header/fetchone) and
        # other databse/table attributes


#import pandas as pd
# dataframe = pd.read_csv('/Users/johnmacnamara/Desktop/test_data3.csv', index_col=0)
# print(dataframe_to_tup_list(dataframe)[:2])
# database = SqlDatabase(dataframe, 'test_database')
# print(database.__repr__())
# database.create_db()
# database.create_curs()
# database.create_table()
# database.insert_data()
# data = database.select_data(select='*', Location='Amsterdam')
# print(data.fetchmany(size=2))
# database.select_data(Location='Aix')
# data = database.display(size=6)
# print(data)
