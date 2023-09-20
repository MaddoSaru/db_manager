from simple_term_menu import TerminalMenu
from typing import List, Dict

def select_terminal_menu_option(
    terminal_options : List
) -> str:
    terminal_menu = TerminalMenu(terminal_options)
    option_txt = terminal_options[terminal_menu.show()]
    return option_txt

def add_config_database(
    config : Dict,
    key : str,
    value : str,
) -> Dict:
    config[key] = value
    return config
