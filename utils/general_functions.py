from simple_term_menu import TerminalMenu
from typing import List, Dict
import requests
import polars as pl
from datetime import datetime
from utils.configs.general_configs import requests_config
import logging

def camel(
    word : str
) -> str:
    return word[0].upper()+word[1:]

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

def make_request() -> pl.DataFrame:
    api_site = select_terminal_menu_option(list(map(lambda x: x, requests_config.keys())))
    data_request_type = select_terminal_menu_option(list(map(lambda x: x, requests_config[api_site]['data_type_request'].keys())))
    aggregation_type = select_terminal_menu_option(list(map(lambda x: x, requests_config[api_site]['data_type_request'][data_request_type]['aggregation'].keys())))

    variables_dict = requests_config[api_site]['data_type_request'][data_request_type]['variables']
    variables = dict()

    for variable in variables_dict:
        if variable == 'endpoint':
            variables[variable] = requests_config[api_site]['data_type_request'][data_request_type]['aggregation'][aggregation_type][variable]
            logging.info(f"{camel(variable)} value: {variables[variable]}")
        else:
            if variables_dict[variable] == 'manual_input':
                variables[variable] = input(f"Enter variable {camel(variable)} value: ")
            elif '/' in variables_dict[variable]:
                logging.info(f"Select {camel(variable)} variable input method")
                input_option = select_terminal_menu_option(variables_dict[variable].split('/'))
                if input_option == 'automatic_input':
                    variables[variable] = datetime.now().timestamp()

    url = requests_config[api_site]['data_type_request'][data_request_type]['url'].format(**variables)

    request = requests.get(url = url).json()['Data']['Data']
    output_pl_df =  pl.DataFrame(request)

    return output_pl_df

