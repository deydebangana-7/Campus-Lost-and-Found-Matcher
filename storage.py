import json

def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    return data["lost_items"], data["found_items"]

def save_data(lost_items, found_items):
    data = {
        "lost_items": lost_items,
        "found_items": found_items
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)