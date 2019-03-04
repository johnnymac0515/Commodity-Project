"""Unit testing module for sql_gener.py"""

import os
import unittest
import pandas as pd

from comm_proj.package1.sql_gener import map_dftype_to_sqldtype
from comm_proj.package1.sql_gener import table_create_str
from comm_proj.package1.sql_gener import sql_insert_str
from comm_proj.package1.sql_gener import dataframe_to_tup_list
from comm_proj.package1.sql_gener import sql_select_str


cwd = os.getcwd()
path = cwd+'/comm_proj/tests/test_data/sql_gener_testdata.csv'
test_df = pd.read_csv(path)

class TestSqlGener(unittest.TestCase):
 
    def setUp(self):
        """Setup class test data"""

        self.df_dict = {'a b c':[1,2], 'test test':[2.4,1.6], 'column':[str('testing'),str('test2')],
        'None Type': [None,None]}
        self.data_frame = pd.DataFrame.from_dict(self.df_dict, orient='columns')
    
    def test_map_spl_type(self):
        """Unittest for map_dftype_to_sqldtype"""

        arg_list, column_list = map_dftype_to_sqldtype(self.data_frame)

        self.assertEqual(column_list, ['abc', 'testtest', 'column', 'NoneType'])
        self.assertNotEqual(column_list, ['a b c', 'test test', 'column', 'NoneType'])
        self.assertEqual(arg_list, ['abc INTEGER', 'testtest REAL', 'column TEXT', 'NoneType TEXT'])

    def test_table_create_str(self):
        """Unittest for table_create_str"""
        test_arg_list = table_create_str(['id test1 TEST1', 'test2 TEST2', 'test3 TEST3'], 
        'test_name')

        test_string = "CREATE TABLE IF NOT EXISTS test_name (id test1 TEST1, test2 TEST2, test3 TEST3);"

        self.assertEqual(test_string, test_arg_list)

    def test_sql_insert_str(self):
        """Unittest for sql_insert_str"""

        test_string = 'INSERT INTO test_name VALUES (?,?,?)'
        test_insert_sql_str = sql_insert_str(3, 'test_name')
        self.assertEqual(test_string, test_insert_sql_str)

    def test_dataframe_to_tup_list(self):
        """Unittest for dataframe_to_tup_list"""

        test_tup_list = [(1, 2.4, 'testing', None), (2, 1.6, 'test2', None)]
        test_dict = dataframe_to_tup_list(self.data_frame)

        self.assertEqual(test_dict, test_tup_list)

    def test_sql_select_str(self):
        """Unittest for sql_select_str"""

        name = 'test_name'

        test_str_one = 'SELECT * FROM test_name'
        test_str_two = 'SELECT one_Column FROM test_name'
        test_str_three = 'SELECT col1 ,col2 FROM test_name'
        test_str_four = "SELECT col1, col2 FROM test_name WHERE a = 'A' and b = 'B'"

        sel_str_one = sql_select_str(name)
        sel_str_two = sql_select_str(name, select='one_Column',)
        sel_str_three = sql_select_str(name, select=['col1', 'col2'])
        sel_str_four = sql_select_str(name, select=['col1, col2'], where={'a':'A', 'b':'B'})

        self.assertEqual(test_str_one, sel_str_one)
        self.assertEqual(test_str_two, sel_str_two)
        self.assertEqual(test_str_three, sel_str_three)
        self.assertEqual(test_str_four, sel_str_four)

if __name__ == '__main__':
    #Testing remove 
    unittest.main(exit=False)
