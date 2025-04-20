import os
import json

def load_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_file(content, filename):
    with open(filename, 'w') as json_file:
        json.dump(content, json_file, indent=4)

def remove_file(filepath):
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Deleted file: {filepath}")
        else:
            print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error deleting file {filepath}: {e}")