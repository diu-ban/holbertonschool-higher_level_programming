#!/usr/bin/env python3

import json 
import csv

def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            with open("data.json", "w") as f:
                json.dump(reader, f)
        return True
    except (FileNotFoundError) as e:
        return False
