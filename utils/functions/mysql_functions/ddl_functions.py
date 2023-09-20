# CREATE DATABASE (CHECK)
# DROP DATABASE (CHECK)
# CREATE TABLE (CHECK)
# DROP TABLE (CHECK)
# TRUNCATE TABLE (CHECK)
# ALTER TABLE (ADD COLUMN / DROP COLUMN / RENAME COLUMN / MODIFY COLUMN DATATYPE)

import mysql.connector
import os
import logging
from dotenv import load_dotenv
from time import sleep

import sys

rel_path = os.path.dirname(__file__)
sys.path.insert(0, f'{rel_path}/../general_functions')

from general_functions import select_terminal_menu_option

load_dotenv()

def select_database() -> str:

    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = os.getenv("MYSQL_ROOT_PASS")
    )

    cursor = db.cursor()

    open_file = open(f'{os.path.dirname(__file__)}/queries/show_databases.sql', 'r')
    query_str = open_file.read()
    cursor.execute(query_str)
        
    ddbb_options = list(map(lambda x: (x)[0], cursor))

    db_name = select_terminal_menu_option(ddbb_options)

    return db_name


def select_table(
    database : str
) -> str:

    print("\n")

    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = os.getenv("MYSQL_ROOT_PASS"),
        database = database
    )

    cursor = db.cursor()

    open_file = open(f'{os.path.dirname(__file__)}/queries/show_tables.sql', 'r')
    query_str = open_file.read()
    cursor.execute(query_str)
        
    tables_options = list(map(lambda x: (x)[0], cursor))

    table_name = select_terminal_menu_option(tables_options)

    return table_name


def create_drop_database():

    print("\n")

    action_txt = select_terminal_menu_option(["Create Database", "Drop Database"])
    action_re_txt = action_txt.replace(" ","_").lower()

    print("\n")

    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = os.getenv("MYSQL_ROOT_PASS")
    )

    sleep(1)

    cursor = db.cursor()

    if action_re_txt == 'create_database':
        db_name = input("Select Database Name: ")
        print("\n")
    else:
        db_name = select_database()
        print("\n")

    open_file = open(f'{rel_path}/queries/{action_re_txt}.sql', 'r')
    query_str = open_file.read()
    format_query_str = query_str.format(db_name = db_name)

    logging.info(f'Creating {db_name} Database...' if action_re_txt == 'create_database' else f'Dropping {db_name} Database...')

    cursor.execute(format_query_str)

    sleep(1)

    logging.info(f'Database {db_name} Created Successfully\n' if action_re_txt == 'create_database' else f'Database {db_name} Dropped Successfully\n')
    
    return 200


def create_truncate_drop_table():

    print("\n")

    action_txt = select_terminal_menu_option(["Create Table", "Truncate Table", "Drop Table"])
    action_re_txt = action_txt.replace(" ","_").lower()

    print("\n")

    print("Select Database...\n")
    database = select_database()

    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = os.getenv("MYSQL_ROOT_PASS"),
        database = database
    )

    cursor = db.cursor()

    open_file = open(f'{rel_path}/queries/{action_re_txt}.sql', 'r')
    query_str = open_file.read()

    print("\n")

    if action_re_txt == 'create_table':
        table_name = input("Select Table Name: ")
        columns_config = ''
        while(True):
            print("\n")
            column_name = input("Select Column Name: ")
            print("Select Column Type...\n")
            print("Integer: Numeric exact value\n")
            print("Float: Numeric approximate value with decimals\n")
            print("Char(n): String value of 'n' characters\n")
            print("Datetime: Date and time parts value\n\n")
            column_data_type = select_terminal_menu_option(['INTEGER', 'FLOAT', 'CHAR(200)', 'DATETIME'])
            
            print("\n")
            
            add_more_columns_txt = select_terminal_menu_option(["Add Another Column", "Do Not Add More Columns"])

            if add_more_columns_txt == "Do Not Add More Columns":
                columns_config += f"{column_name} {column_data_type}"
                break

            columns_config += f"{column_name} {column_data_type},\n"
        format_query_str = query_str.format(table_name = table_name, columns_config = columns_config)
    else:
        format_query_str = query_str.format(table_name = select_table(database = database))

    print("\n")

    print(format_query_str)

    sleep(1)

    cursor.execute(format_query_str)
    
    return 200