#! /usr/bin/env python

import re
from pathlib import Path
from rich import print as pprint
import yaml
from py_load_yaml import load_yaml



def main(): 
    anta_inventory = {"anta_inventory": {"hosts": []} }
    inventory_yml_file = Path("playbooks/Ernesto_L2LS_LAB.yml")
    anta_inventory_file = Path("anta/anta_inventory.yml")
    inventory_dict = load_yaml(inventory_yml_file)

    for key, _ in inventory_dict["all"]["children"]["VEOS"]["hosts"].items():
        if key.startswith("sto"):
            if re.search(r'(?<=-)(?:bl)', key):
                anta_inventory["anta_inventory"]["hosts"].append({"host" : key, "tags": ["border", "leaf"]})
            elif re.search(r'(?<=-)(?:le)', key):
                anta_inventory["anta_inventory"]["hosts"].append({"host" : key, "tags": ["leaf"]})
            elif re.search(r'(?<=-)(?:sp)', key):
                anta_inventory["anta_inventory"]["hosts"].append({"host" : key, "tags": ["spine"]})
    with open(anta_inventory_file, 'w') as file:
        yaml.dump(anta_inventory, file, indent=2)

if __name__ == "__main__":
    main()