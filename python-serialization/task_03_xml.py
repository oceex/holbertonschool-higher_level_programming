#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    root = ET.parse(filename).getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
