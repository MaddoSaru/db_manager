import mysql.connector
from utils.general_functions import select_terminal_menu_option, add_config_database
from utils.configs.general_configs import ddbb_config


def select_database() -> str:

    db = mysql.connector.connect(** ddbb_config)

    cursor = db.cursor()

    open_file = open(f'utils/queries/show_databases.sql', 'r')
    query_str = open_file.read()
    cursor.execute(query_str)
        
    ddbb_options = list(map(lambda x: (x)[0], cursor))

    db_name = select_terminal_menu_option(ddbb_options)

    return db_name


def select_table(
    database : str
) -> str:

    db = mysql.connector.connect(** 
        add_config_database(
            config = ddbb_config, 
            key = "database", 
            value = database
        )
    )

    cursor = db.cursor()

    open_file = open(f'utils/queries/show_tables.sql', 'r')
    query_str = open_file.read()
    cursor.execute(query_str)
        
    tables_options = list(map(lambda x: (x)[0], cursor))

    table_name = select_terminal_menu_option(tables_options)

    return table_name