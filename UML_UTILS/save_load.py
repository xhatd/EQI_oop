import json
import os

def save_data_to_json(data, filename):
    """Save data to a JSON file in the current directory."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}.")

def load_data_from_json(filename):
    """Load data from a JSON file, returning an empty structure if the file doesn't exist."""
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            print(f"Data loaded from {filename}.")
            return data
    else:
        print(f"{filename} not found. Returning empty data structure.")
        return {"classes": [], "relationships": []}  # Return empty structure
