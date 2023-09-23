# CREATE DATABASE (CHECK)
# DROP DATABASE (CHECK)
# CREATE TABLE (CHECK)
# DROP TABLE (CHECK)
# TRUNCATE TABLE (CHECK)
# ALTER TABLE (ADD COLUMN / DROP COLUMN / RENAME COLUMN / MODIFY COLUMN DATATYPE)

import mysql.connector
import logging
from time import sleep
from utils.general_db_functions import select_database, select_table
from utils.general_functions import select_terminal_menu_option, add_config_database
from utils.configs.general_configs import ddbb_config

def create_drop_database():

    action_txt = select_terminal_menu_option(["Create Database", "Drop Database"])
    action_re_txt = action_txt.replace(" ","_").lower()

    db = mysql.connector.connect(** ddbb_config)

    sleep(1)

    cursor = db.cursor()

    if action_re_txt == 'create_database':
        db_name = input("Select Database Name: ")
        attempt_msg = f'Creating {db_name} Database...'
        successfull_msg = f'Database {db_name} Created Successfully\n'
        
    else:
        db_name = select_database()
        attempt_msg = f'Dropping {db_name} Database...'
        successfull_msg = f'Database {db_name} Dropped Successfully\n'
        

    open_file = open(f'utils/queries/{action_re_txt}.sql', 'r')
    query_str = open_file.read()
    format_query_str = query_str.format(db_name = db_name)

    logging.info(attempt_msg)

    cursor.execute(format_query_str)

    sleep(1)

    logging.info(successfull_msg)
    
    return 200


def create_truncate_drop_table():

    action_txt = select_terminal_menu_option(["Create Table", "Truncate Table", "Drop Table"])
    action_re_txt = action_txt.replace(" ","_").lower()

    logging.info("Select Database...\n")
    database = select_database()

    db = mysql.connector.connect(** 
        add_config_database(
            config = ddbb_config, 
            key = "database", 
            value = database
        )
    )

    cursor = db.cursor()

    open_file = open(f'utils/queries/{action_re_txt}.sql', 'r')
    query_str = open_file.read()

    if action_re_txt == 'create_table':
        table_name = input("Select Table Name: ")
        attempt_msg = f'Creating Table {table_name} In {database} Database'
        columns_config = ''
        while(True):
            
            column_name = input("Select Column Name: ")
            logging.info("Select Column Type...\nInteger: Numeric exact value\nFloat: Numeric approximate value with decimals\nChar(n): String value of 'n' characters\nDatetime: Date and time parts value\n\n")
            column_data_type = select_terminal_menu_option(['INTEGER', 'FLOAT', 'CHAR(200)', 'DATETIME'])   
            
            add_more_columns_txt = select_terminal_menu_option(["Add Another Column", "Do Not Add More Columns"])

            if add_more_columns_txt == "Do Not Add More Columns":
                columns_config += f"{column_name} {column_data_type}"
                break

            columns_config += f"{column_name} {column_data_type},\n"
        format_query_str = query_str.format(table_name = table_name, columns_config = columns_config)
    else:
        table_name = select_table(database = database)
        format_query_str = query_str.format(table_name = table_name)
        if action_re_txt == 'drop_table':
            attempt_msg = f'Dropping Table {table_name} From {database} Database'
            successfull_msg = f'Table {table_name} Dropped Successfully'
        else:
            attempt_msg = f'Truncating Table {table_name} From {database} Database'
            successfull_msg = f'Table {table_name} Truncated Successfully'

    logging.info(attempt_msg)

    cursor.execute(format_query_str)

    sleep(1)

    logging.info(successfull_msg)
    
    return 200