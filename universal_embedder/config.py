import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print("Configuration file config.yaml not found.")
        raise
    except yaml.YAMLError as exc:
        print("Error in configuration file:", exc)
        raise
