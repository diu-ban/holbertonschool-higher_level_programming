#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8"):
        json.dump(data, filename)

def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8"):
        return json.load(filename)