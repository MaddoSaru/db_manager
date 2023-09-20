from simple_term_menu import TerminalMenu
import logging
from utils.functions.mysql_functions.ddl_functions import create_drop_database

logging.basicConfig(level = logging.INFO)

def main():
    while(True):
        print("\n")
        app_options = ['Create or Drop Database', 'Exit']
        terminal_app_menu = TerminalMenu(app_options)
        app_action_ind = terminal_app_menu.show()
        app_action = app_options[app_action_ind]
        if app_action_ind == 0:
            create_drop_database()
        elif app_action == 'Exit':
            print('\n')
            logging.info('Thanks for using MaddoSaru database manager uwu\n')
            break

if __name__ == "__main__":
    main()