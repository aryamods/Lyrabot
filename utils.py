import json
import os

def load_data(file_name, default_value):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return default_value

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)