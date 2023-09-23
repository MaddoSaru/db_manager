import logging
from utils.ddl_functions import create_drop_database, create_truncate_drop_table
from utils.dml_functions import insert_update_delete_registers
from utils.general_functions import select_terminal_menu_option

logging.basicConfig(level = logging.INFO, format = 'Maddosaru DB Manager: %(message)s')

def main():
    logging.info("\n\nWelcome to MaddoSaru DB Manager App\nHow can I help you?\n")
    while(True):
        app_action = select_terminal_menu_option(
            ['Create or Drop Database', 
             'Create Truncate or Drop Table',
             'Insert Update or Delete Table Registers',
             'Exit']
        )
        if app_action == 'Create or Drop Database':
            create_drop_database()
        elif app_action == 'Create Truncate or Drop Table':
            create_truncate_drop_table()
        elif app_action == 'Insert Update or Delete Table Registers':
            print(insert_update_delete_registers())
        elif app_action == 'Exit':
            break
    logging.info('Thanks for using MaddoSaru DB Manager App uwu!\n')

if __name__ == "__main__":
    main()