#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")  

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)  
        item.text = str(value)  

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            key = child.tag
            value = child.text
            
            # if value.isdigit():
            #     value = int(value)
            # elif value.lower() in ['true', 'false']:
            #     value = value.lower() == 'true'
            # else:
            #     try:
            #         value = float(value)
            #     except ValueError:
            #         pass  
            

            result[key] = value

        return result

    except (FileNotFoundError, ET.ParseError):
        return None