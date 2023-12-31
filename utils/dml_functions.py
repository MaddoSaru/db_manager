"""
INSERT REGISTERS MANUALLY TO A TABLE (CHECK)
INSERT REGISTERS FROM A DATASET - DATAFRAME
UPDATE TABLE REGISTERS
DELETE REGISTERS
"""

import mysql.connector
from utils.general_db_functions import (
    select_database,
    show_tables_list,
    create_columns_config,
    table_describe_dict,
)
from utils.general_functions import (
    camel,
    select_terminal_menu_option,
    add_config_database,
    make_request,
)
from utils.configs.general_configs import ddbb_config, requests_config
from utils.ddl_functions import create_truncate_drop_table
import logging


def insert_update_delete_registers():
    action_txt = select_terminal_menu_option(
        ["Insert Registers", "Update Registers", "Delete Registers"]
    )
    action_re_txt = action_txt.replace(" ", "_").lower()

    logging.info("Select Database...")
    database = select_database()

    db = mysql.connector.connect(
        **add_config_database(config=ddbb_config, key="database", value=database)
    )

    cursor = db.cursor()

    open_file = open(f"utils/queries/{action_re_txt}.sql", "r")
    query_str = open_file.read()

    logging.info("Select Table...")

    tables_list = show_tables_list(database=database)
    tables_list.append("Create Table")
    table_name = select_terminal_menu_option(tables_list)

    if action_txt == "Insert Registers":
        insert_registers_action_txt = select_terminal_menu_option(
            ["Insert Manual Registers", "Insert Request Registers"]
        )

        if insert_registers_action_txt == "Insert Request Registers":
            
            api_site, data_request_type, pl_df = make_request()

            columns_structure = requests_config[api_site]["data_type_request"][data_request_type]["columns_structure"]

            if table_name == "Create Table":
                table_name = f"{api_site}_{data_request_type}"
                create_truncate_drop_table(
                    table_name=table_name, 
                    database=database, 
                    action_txt="Create Table", 
                    columns_config = create_columns_config(columns_structure = columns_structure)
                )

            values = ""
            columns = "`" + "`,`".join(pl_df.columns) + "`"
            cont = 0
            quoted_variables = ["DATETIME", "VARCHAR(255)", "JSON"]

            for row in pl_df.rows():
                cont += 1
                values += "("
                for column_index in range(len(pl_df.columns)):
                    if str(row[column_index]) == "None":
                        values += "NULL," if column_index + 1 < len(row) else "NULL"
                    else:
                        if column_index + 1 < len(row) and columns_structure.get(pl_df.columns[column_index]) in quoted_variables:
                            values += '"' + str(row[column_index]).replace('"',"'").replace("`","'")[:250] + '",'
                        elif column_index + 1 < len(row) and columns_structure.get(pl_df.columns[column_index]) not in quoted_variables:
                            values += str(row[column_index]).replace('"',"'").replace("`","'")[:250] + ","
                        elif column_index + 1 == len(row) and columns_structure.get(pl_df.columns[column_index]) in quoted_variables:
                            values += '"' + str(row[column_index]).replace('"',"'").replace("`","'")[:250] + '"'
                        elif column_index + 1 == len(row) and columns_structure.get(pl_df.columns[column_index]) not in quoted_variables:
                            values += str(row[column_index]).replace('"',"'").replace("`","'")[:250]
                values += "),\n" if cont < len(pl_df.rows()) else ");"

        elif insert_registers_action_txt == "Insert Manual Registers":
            table_describe = table_describe_dict(
                database=database, table_name=table_name
            )
            columns = ""
            values = ""

            keep_adding_values = True

            while(keep_adding_values):
                values += "("
                for column in table_describe:
                    logging.info(
                        f"Column {camel(column)} Has Data Type {table_describe[column]}"
                    )
                    value = str(input(f"Select Column {camel(column)} Value: "))
                    if column != list(table_describe)[-1]:
                        columns += column + ","
                        values += (
                            '"' + value + '",'
                            if table_describe[column] in ["datetime", "char(200)"]
                            else value + ","
                        )
                    else:
                        columns += column
                        values += (
                            '"' + value + '"'
                            if table_describe[column] in ["datetime", "char(200)"]
                            else value
                        )
                add_registers = select_terminal_menu_option(["Add Another Register", "Stop Adding Registers"])
                
                if add_registers == "Stop Adding Registers":
                    values += ")"
                    keep_adding_values = False
                else: 
                    values += "),"

        format_query_str = query_str.format(
            table_name=table_name, columns=columns, values=values
        )

    attempt_msg = f"Inserting Registers Into Table {table_name} In {database} Database"
    successfull_msg = f"Registers Inserted Into Table {table_name} Successfully"

    logging.info(attempt_msg)

    cursor.execute(format_query_str)

    db.commit()

    logging.info(successfull_msg)

    return format_query_str
