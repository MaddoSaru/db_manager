# CREATE DATABASE (CHECK)
# DROP DATABASE (CHECK)
# CREATE TABLE
# DROP TABLE
# TRUNCATE TABLE
# ALTER TABLE (ADD COLUMN / DROP COLUMN / RENAME COLUMN / MODIFY COLUMN DATATYPE)

import mysql.connector
import os
import logging
from dotenv import load_dotenv
from simple_term_menu import TerminalMenu
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

    logging.info('Connecting to Database...\n')

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

    sleep(1)

    logging.info(f'Creating {db_name} Database...' if action_re_txt == 'create_database' else f'Dropping {db_name} Database...')

    cursor.execute(format_query_str)

    sleep(1)

    logging.info(f'Database {db_name} Created Successfully\n' if action_re_txt == 'create_database' else f'Database {db_name} Dropped Successfully\n')
    
    return 200

def create_drop_truncate_table():

    print("\n")

    action_txt = select_terminal_menu_option(["Create Table", "Truncate Table", "Drop Table"])
    action_re_txt = action_txt.replace(" ","_").lower()

    print("\n")

    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = os.getenv("MYSQL_ROOT_PASS")
    )

    logging.info('Connecting to Database...\n')

    sleep(1)

    cursor = db.cursor()
    
    return 200