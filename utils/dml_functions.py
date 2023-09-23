# INSERT REGISTERS MANUALLY TO A TABLE 
# INSERT REGISTERS FROM A DATASET - DATAFRAME
# UPDATE TABLE REGISTERS
# DELETE REGISTERS

import mysql.connector
from utils.general_db_functions import select_database, select_table
from utils.general_functions import select_terminal_menu_option, add_config_database, make_request
from utils.configs.general_configs import ddbb_config
import logging

def insert_update_delete_registers():
    action_txt = select_terminal_menu_option(["Insert Registers", "Update Registers", "Delete Registers"])
    action_re_txt = action_txt.replace(" ","_").lower()

    logging.info("Select Database...")
    database = select_database()

    db = mysql.connector.connect(** 
        add_config_database(
            config = ddbb_config, 
            key = "database", 
            value = database
        )
    )

    cursor = db.cursor()

    logging.info("Select Table...")
    table_name = select_table(database = database)

    if action_txt == 'Insert Registers':
        insert_registers_action_txt = select_terminal_menu_option(['Insert Manual Registers', 'Insert Request Registers'])
        if insert_registers_action_txt == 'Insert Request Registers':
            pl_df = make_request()

    return pl_df.head(5)