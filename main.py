import logging
from utils.functions.mysql_functions.ddl_functions import create_drop_database, create_truncate_drop_table
from utils.functions.general_functions.general_functions import select_terminal_menu_option

logging.basicConfig(level = logging.INFO)

def main():
    while(True):
        print("\n")
        app_action = select_terminal_menu_option(
            ['Create or Drop Database', 
             'Create Truncate or Drop Table',
             'Exit']
        )
        if app_action == 'Create or Drop Database':
            create_drop_database()
        elif app_action == 'Create Truncate or Drop Table':
            create_truncate_drop_table()
        elif app_action == 'Exit':
            print('\n')
            logging.info('Thanks for using MaddoSaru database manager uwu!\n')
            break

if __name__ == "__main__":
    main()