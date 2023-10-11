import os
from dotenv import load_dotenv

load_dotenv()

ddbb_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": os.getenv("MYSQL_ROOT_PASS"),
}

cryptocompare_api_key = os.getenv("CRYPTOCOMPARE_API_KEY")

requests_config = {
    "jikan": {
        "data_type_request": {
            "anime": {
                "url": "https://api.jikan.moe/v4/anime?sort_by=mal_id&page={page_number}",
                "request_data_structure": "data",
                "variables": {
                    "page_number": "manual_input"
                },
                "columns_structure": {
                    'mal_id': "INTEGER", 
                    'url': "VARCHAR(255)", 
                    'images': "VARCHAR(255)", 
                    'trailer': "VARCHAR(255)", 
                    'approved': "BOOLEAN", 
                    'titles': "VARCHAR(255)", 
                    'title': "VARCHAR(255)",
                    'title_english': "VARCHAR(255)",  
                    'title_japanese': "VARCHAR(255)", 
                    'title_synonyms': "VARCHAR(255)", 
                    'type': "VARCHAR(255)", 
                    'source': "VARCHAR(255)", 
                    'episodes': "VARCHAR(255)", 
                    'status': "VARCHAR(255)", 
                    'airing': "BOOLEAN", 
                    'aired': "VARCHAR(255)", 
                    'duration': "VARCHAR(255)", 
                    'rating': "VARCHAR(255)", 
                    'score': "DOUBLE", 
                    'scored_by': "INTEGER", 
                    'rank': "INTEGER", 
                    'popularity': "INTEGER", 
                    'members': "INTEGER", 
                    'favorites': "INTEGER", 
                    'synopsis': "VARCHAR(255)", 
                    'background': "VARCHAR(255)", 
                    'season': "VARCHAR(255)", 
                    'year': "INTEGER", 
                    'broadcast': "VARCHAR(255)", 
                    'producers': "VARCHAR(255)", 
                    'licensors': "VARCHAR(255)", 
                    'studios': "VARCHAR(255)", 
                    'genres': "VARCHAR(255)", 
                    'explicit_genres': "VARCHAR(255)", 
                    'themes': "VARCHAR(255)", 
                    'demographics': "VARCHAR(255)",
                }
            }

        }
    },
    "cryptocompare": {
        "data_type_request": {
            "OHCLV": {
                "url": "https://min-api.cryptocompare.com/data/v2/{endpoint}?fsym={currency}&tsym=USD&toTs={min_time}&api_key="
                + cryptocompare_api_key
                + "&limit=2000",
                "request_data_structure": "Data/Data",
                "variables": {
                    "endpoint": "not_manual_input",
                    "currency": "manual_input",
                    "min_time": "manual_input/not_manual_input/automatic_input",
                },
                 "columns_structure": {
                    "time": "INTEGER",
                    "currency": "VARCHAR(255)",
                    "high": "DOUBLE",
                    "low": "DOUBLE",
                    "open": "DOUBLE",
                    "close": "DOUBLE",
                    "volumefrom": "DOUBLE",
                    "volumeto": "DOUBLE",
                    "conversionType": "VARCHAR(255)",
                    "conversionSymbol": "VARCHAR(255)",
                },
                "aggregation": {
                    "Daily Pair OHCLV": {
                        "endpoint": "histoday",
                    },
                    "Hourly Pair OHCLV": {
                        "endpoint": "histohour",
                    },
                    "Minute Pair OHCLV": {
                        "endpoint": "histominute",
                    },
                },
            }
        }
    }
}
