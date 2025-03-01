import json
import os

from path_test.utils.pathutils import find_path

if __name__ == '__main__':
    config_path = find_path("resources/config.json")
    print("Current directory", os.getcwd())
    print("Config path", config_path.absolute())
    with open(config_path, "r") as f:
        print(json.load(f))

    data_path = find_path("resources/data")
    print("Data path", data_path.absolute())
    for el in data_path.iterdir():
        print("\t", el)
