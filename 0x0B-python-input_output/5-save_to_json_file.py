#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON"""
    json_str = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(json_str)
