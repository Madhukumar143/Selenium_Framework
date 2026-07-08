import os
from configparser import ConfigParser

def read_configuration(category, key):
    config = ConfigParser() #reates an object that will read .ini file
    config_path = os.path.join(os.path.dirname(__file__), "../configurations/config.ini")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    config.read(config_path)
    if not config.has_section(category):
        raise ValueError(f"Section '{category}' not found in the configuration file.")
    return config.get(category, key)