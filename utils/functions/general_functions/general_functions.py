from simple_term_menu import TerminalMenu
from typing import List

def select_terminal_menu_option(
    terminal_options : List
) -> str:
    terminal_menu = TerminalMenu(terminal_options)
    option_txt = terminal_options[terminal_menu.show()]
    return option_txt