import os
from dotenv import load_dotenv

load_dotenv()

ddbb_config = {
    "host" : "127.0.0.1",
    "user" : "root",
    "password" : os.getenv("MYSQL_ROOT_PASS"),
}

cryptocompare_api_key = os.getenv('CRYPTOCOMPARE_API_KEY')

requests_config = {
    'cryptocompare' : {
        'data_type_request' : {
            'OHCLV' : {
                'url' : 'https://min-api.cryptocompare.com/data/v2/{endpoint}?fsym={currency}&tsym=USD&toTs={min_time}&api_key='+cryptocompare_api_key+'&limit=2000',
                'variables' : {
                    'endpoint' : 'not_manual_input',
                    'currency' : 'manual_input',
                    'min_time' : 'manual_input/not_manual_input/automatic_input',
                },
                'aggregation' : {
                    'Daily Pair OHCLV' : {
                        'endpoint' : 'histoday',
                        'columns_structure' : {
                            'time' : 'INTEGER',
                            'currency' : 'VARCHAR(255)',
                            'high' : 'DOUBLE',
                            'low' : 'DOUBLE',
                            'open' : 'DOUBLE',
                            'close' : 'DOUBLE',
                            'volumefrom' : 'DOUBLE',
                            'volumeto' : 'DOUBLE',
                            'conversionType' : 'VARCHAR(255)',
                            'conversionSymbol' : 'VARCHAR(255)'
                        }
                    },
                    'Hourly Pair OHCLV' : {
                        'endpoint' : 'histohour',
                        'columns_structure' : {
                            'time' : 'INTEGER',
                            'currency' : 'VARCHAR(255)',
                            'high' : 'DOUBLE',
                            'low' : 'DOUBLE',
                            'open' : 'DOUBLE',
                            'close' : 'DOUBLE',
                            'volumefrom' : 'DOUBLE',
                            'volumeto' : 'DOUBLE',
                            'conversionType' : 'VARCHAR(255)',
                            'conversionSymbol' : 'VARCHAR(255)'
                        }
                    },
                    'Minute Pair OHCLV' : {
                        'endpoint' : 'histominute',
                        'columns_structure' : {
                            'time' : 'INTEGER',
                            'currency' : 'VARCHAR(255)',
                            'high' : 'DOUBLE',
                            'low' : 'DOUBLE',
                            'open' : 'DOUBLE',
                            'close' : 'DOUBLE',
                            'volumefrom' : 'DOUBLE',
                            'volumeto' : 'DOUBLE',
                            'conversionType' : 'VARCHAR(255)',
                            'conversionSymbol' : 'VARCHAR(255)'
                        }
                    },
                }
            }
        }
    }
}