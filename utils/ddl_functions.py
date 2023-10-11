"""
CREATE DATABASE (CHECK)
DROP DATABASE (CHECK)
CREATE TABLE (CHECK)
DROP TABLE (CHECK)
TRUNCATE TABLE (CHECK)
ALTER TABLE (ADD COLUMN / DROP COLUMN / RENAME COLUMN / MODIFY COLUMN DATATYPE)
"""


import mysql.connector
import logging
from time import sleep
from typing import Optional
from utils.general_db_functions import (
    select_database,
    select_table,
    create_columns_config,
)
from utils.general_functions import select_terminal_menu_option, add_config_database
from utils.configs.general_configs import ddbb_config


def create_drop_database():
    action_txt = select_terminal_menu_option(["Create Database", "Drop Database"])
    action_re_txt = action_txt.replace(" ", "_").lower()

    db = mysql.connector.connect(**ddbb_config)

    cursor = db.cursor()

    if action_re_txt == "create_database":
        db_name = input("Select Database Name: ")
        attempt_msg = f"Creating {db_name} Database..."
        successfull_msg = f"Database {db_name} Created Successfully\n"

    else:
        db_name = select_database()
        attempt_msg = f"Dropping {db_name} Database..."
        successfull_msg = f"Database {db_name} Dropped Successfully\n"

    open_file = open(f"utils/queries/{action_re_txt}.sql", "r")
    query_str = open_file.read()
    format_query_str = query_str.format(db_name=db_name)

    logging.info(attempt_msg)

    cursor.execute(format_query_str)

    logging.info(successfull_msg)

    return 200


def create_truncate_drop_table(
    action_txt: Optional[str] = None,
    database: Optional[str] = None,
    table_name: Optional[str] = None,
    columns_config: Optional[str] = None,
):
    if action_txt == None:
        action_txt = select_terminal_menu_option(
            ["Create Table", "Truncate Table", "Drop Table"]
        )

    action_re_txt = action_txt.replace(" ", "_").lower()

    if database == None:
        logging.info("Select Database...\n")
        database = select_database()

    db = mysql.connector.connect(
        **add_config_database(config=ddbb_config, key="database", value=database)
    )

    cursor = db.cursor()

    open_file = open(f"utils/queries/{action_re_txt}.sql", "r")
    query_str = open_file.read()

    if action_re_txt == "create_table":
        attempt_msg = f"Creating Table {table_name} In {database} Database"
        successfull_msg = f"Table {table_name} Created Successfully"
        if table_name == None:
            table_name = input("Select Table Name: ")
        if columns_config == None:
            columns_config = create_columns_config()
        format_query_str = query_str.format(
            table_name=table_name, columns_config=columns_config
        )
    else:
        table_name = select_table(database=database)
        format_query_str = query_str.format(table_name=table_name)
        if action_re_txt == "drop_table":
            attempt_msg = f"Dropping Table {table_name} From {database} Database"
            successfull_msg = f"Table {table_name} Dropped Successfully"
        else:
            attempt_msg = f"Truncating Table {table_name} From {database} Database"
            successfull_msg = f"Table {table_name} Truncated Successfully"

    logging.info(attempt_msg)

    logging.info(format_query_str)

    cursor.execute(format_query_str)

    logging.info(successfull_msg)

    return 200
