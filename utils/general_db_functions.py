import mysql.connector
from utils.general_functions import select_terminal_menu_option, add_config_database
from utils.configs.general_configs import ddbb_config
from typing import Optional, Dict, List
import logging


def select_database() -> str:
    db = mysql.connector.connect(**ddbb_config)

    cursor = db.cursor()

    open_file = open(f"utils/queries/show_databases.sql", "r")
    query_str = open_file.read()
    cursor.execute(query_str)

    ddbb_options = list(map(lambda x: (x)[0], cursor))

    db_name = select_terminal_menu_option(ddbb_options)

    return db_name


def select_table(database: str) -> str:
    db = mysql.connector.connect(
        **add_config_database(config=ddbb_config, key="database", value=database)
    )

    cursor = db.cursor()

    open_file = open(f"utils/queries/show_tables.sql", "r")
    query_str = open_file.read()
    cursor.execute(query_str)

    tables_options = list(map(lambda x: (x)[0], cursor))

    table_name = select_terminal_menu_option(tables_options)

    return table_name


def show_tables_list(database: str) -> List:
    db = mysql.connector.connect(
        **add_config_database(config=ddbb_config, key="database", value=database)
    )

    cursor = db.cursor()

    open_file = open(f"utils/queries/show_tables.sql", "r")
    query_str = open_file.read()
    cursor.execute(query_str)

    tables_options = list(map(lambda x: (x)[0], cursor))

    return tables_options


def create_columns_config(columns_structure: Optional[Dict] = None):
    columns_config = ""
    if columns_structure != None:
        logging.info("Creating Columns Config From Given Column Structure...")
        for column_name in columns_structure:
            columns_config += (
                f"`{column_name}` {columns_structure[column_name]}"
                if column_name == list(columns_structure)[-1]
                else f"`{column_name}` {columns_structure[column_name]},"
            )
    else:
        logging.info("Create New Columns Config...")
        while True:
            column_name = input("Select Column Name: ")
            logging.info(
                "Select Column Type...\nInteger: Numeric exact value\nFloat: Numeric approximate value with decimals\nChar(n): String value of 'n' characters\nDatetime: Date and time parts value"
            )
            column_data_type = select_terminal_menu_option(
                ["INTEGER", "FLOAT", "CHAR(200)", "DATETIME"]
            )

            add_more_columns_txt = select_terminal_menu_option(
                ["Add Another Column", "Do Not Add More Columns"]
            )

            if add_more_columns_txt == "Do Not Add More Columns":
                columns_config += f"`{column_name}` {column_data_type}"
                break

            columns_config += f"`{column_name}` {column_data_type},\n"
    return columns_config


def table_describe_dict(database: str, table_name: str) -> Dict:
    db = mysql.connector.connect(
        **add_config_database(config=ddbb_config, key="database", value=database)
    )

    cursor = db.cursor()

    open_file = open(f"utils/queries/describe_table.sql", "r")
    query_str = open_file.read()
    format_query_str = query_str.format(table_name=table_name)

    cursor.execute(format_query_str)

    table_describe = cursor.fetchall()

    columns_structure = {}

    for column_description in table_describe:
        columns_structure[column_description[0]] = column_description[1].decode()

    return columns_structure
